#!/usr/bin/env python
"""Generate version switcher JSON for multi-version documentation.

This script generates a JSON file that lists all available documentation versions,
used by sphinx-multiversion and the Read the Docs theme for version switching.

Usage:
    python generate_switcher_json.py [--output PATH] [--base-url URL]

Example:
    python generate_switcher_json.py --base-url https://awegroup.github.io/awesIO
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional


def get_git_tags() -> list:
    """Get all git tags that match version pattern.
    
    Returns:
        list: List of version tags sorted by version number (descending).
    """
    try:
        result = subprocess.run(
            ["git", "tag", "-l", "v*"],
            capture_output=True,
            text=True,
            check=True
        )
        tags = result.stdout.strip().split("\n")
        tags = [t for t in tags if t and re.match(r"^v\d+\.\d+\.\d+$", t)]
        
        # Sort by version number (descending)
        tags.sort(key=lambda x: [int(n) for n in x[1:].split(".")], reverse=True)
        return tags
    except subprocess.CalledProcessError:
        return []


def get_git_branches() -> list:
    """Get relevant git branches for documentation.
    
    Returns:
        list: List of branch names (main, develop).
    """
    try:
        result = subprocess.run(
            ["git", "branch", "-r"],
            capture_output=True,
            text=True,
            check=True
        )
        branches = result.stdout.strip().split("\n")
        branches = [b.strip().replace("origin/", "") for b in branches]
        
        # Filter to relevant branches
        relevantBranches = []
        for branch in ["main", "develop"]:
            if branch in branches:
                relevantBranches.append(branch)
        
        return relevantBranches
    except subprocess.CalledProcessError:
        return ["main"]


def generate_switcher_json(
    baseUrl: str,
    outputPath: Path,
    includeDevVersions: bool = True
) -> dict:
    """Generate version switcher JSON content.
    
    Args:
        baseUrl (str): Base URL for documentation (e.g., https://awegroup.github.io/awesIO).
        outputPath (Path): Path to write the JSON file.
        includeDevVersions (bool): Whether to include development branches.
        
    Returns:
        dict: The generated switcher configuration.
    """
    versions = []
    
    # Add development versions (branches)
    if includeDevVersions:
        branches = get_git_branches()
        for branch in branches:
            versionEntry = {
                "name": branch,
                "version": branch,
                "url": f"{baseUrl}/{branch}/",
            }
            if branch == "main":
                versionEntry["preferred"] = True
            versions.append(versionEntry)
    
    # Add release versions (tags)
    tags = get_git_tags()
    for i, tag in enumerate(tags):
        versionEntry = {
            "name": tag,
            "version": tag,
            "url": f"{baseUrl}/{tag}/",
        }
        # Mark the latest release
        if i == 0:
            versionEntry["aliases"] = ["latest", "stable"]
        versions.append(versionEntry)
    
    # If no versions found, create a default entry
    if not versions:
        versions = [
            {
                "name": "main",
                "version": "main",
                "url": f"{baseUrl}/",
                "preferred": True,
            }
        ]
    
    switcherData = {
        "versions": versions
    }
    
    # Write to file
    outputPath.parent.mkdir(parents=True, exist_ok=True)
    with open(outputPath, "w", encoding="utf-8") as f:
        json.dump(switcherData, f, indent=2)
    
    print(f"Generated version switcher: {outputPath}")
    print(f"Found {len(versions)} version(s)")
    
    return switcherData


def main():
    """Main entry point for version switcher generation."""
    parser = argparse.ArgumentParser(
        description="Generate version switcher JSON for awesIO documentation"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "_static" / "switcher.json",
        help="Output path for switcher.json"
    )
    parser.add_argument(
        "--base-url",
        type=str,
        default="https://awegroup.github.io/awesIO",
        help="Base URL for documentation"
    )
    parser.add_argument(
        "--no-dev",
        action="store_true",
        help="Exclude development branches (main, develop)"
    )
    
    args = parser.parse_args()
    
    print("awesIO Documentation Version Switcher Generator")
    print("-" * 50)
    
    switcherData = generate_switcher_json(
        baseUrl=args.base_url,
        outputPath=args.output,
        includeDevVersions=not args.no_dev
    )
    
    # Print summary
    print("-" * 50)
    print("Versions included:")
    for version in switcherData["versions"]:
        preferred = " (preferred)" if version.get("preferred") else ""
        aliases = f" [{', '.join(version.get('aliases', []))}]" if version.get("aliases") else ""
        print(f"  - {version['name']}{preferred}{aliases}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
