#!/usr/bin/env python
"""Generate HTML documentation from YAML schemas using json-schema-for-humans.

This script converts YAML schema files to interactive HTML documentation pages.
It uses the json-schema-for-humans library with custom Jinja2 templates for
consistent styling with the awesIO documentation.

Usage:
    python schema_export.py [--output-dir PATH] [--template-dir PATH]
    
Example:
    python schema_export.py
    python schema_export.py --output-dir _static --template-dir jsfh_template
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

import yaml


def get_schema_paths():
    """Get the paths to schema files and output locations.
    
    Returns:
        dict: Dictionary mapping schema names to their source and output paths.
    """
    docsDir = Path(__file__).parent
    projectRoot = docsDir.parent
    srcDir = projectRoot / "src" / "awesio" / "schemas"
    
    # Define schema mappings: name -> (source_path, output_filename)
    # These reference the actual schema locations in the awesIO project
    schemaMapping = {
        "airborne": {
            "source": srcDir / "airborne_schema.yml",
            "output": "airborne_schema.html",
            "title": "Airborne System Schema",
        },
        "ground_station": {
            "source": srcDir / "ground_station_schema.yml",
            "output": "ground_station_schema.html",
            "title": "Ground Station Schema",
        },
        "tether": {
            "source": srcDir / "tether_schema.yml",
            "output": "tether_schema.html",
            "title": "Tether Schema",
        },
        "power_curves": {
            "source": srcDir / "power_curves_schema.yml",
            "output": "power_curves_schema.html",
            "title": "Power Curves Schema",
        },
        "wind_resource": {
            "source": srcDir / "wind_resource_schema.yml",
            "output": "wind_resource_schema.html",
            "title": "Wind Resource Schema",
        },
        "operational_constraints": {
            "source": srcDir / "operational_constraints_schema.yml",
            "output": "operational_constraints_schema.html",
            "title": "Operational Constraints Schema",
        },
    }
    
    return schemaMapping


def convert_yaml_to_json_schema(yamlPath: Path) -> dict:
    """Load a YAML schema file and return as dictionary.
    
    Args:
        yamlPath (Path): Path to the YAML schema file.
        
    Returns:
        dict: The schema as a Python dictionary.
        
    Raises:
        FileNotFoundError: If the schema file does not exist.
        yaml.YAMLError: If the YAML is malformed.
    """
    if not yamlPath.exists():
        raise FileNotFoundError(f"Schema file not found: {yamlPath}")
    
    with open(yamlPath, "r", encoding="utf-8") as f:
        schema = yaml.safe_load(f)
    
    return schema


def generate_schema_html(
    schemaPath: Path,
    outputPath: Path,
    title: str,
    templateDir: Optional[Path] = None
) -> bool:
    """Generate HTML documentation from a YAML schema file.
    
    Args:
        schemaPath (Path): Path to the input YAML schema file.
        outputPath (Path): Path for the output HTML file.
        title (str): Title for the generated documentation page.
        templateDir (Optional[Path]): Path to custom Jinja2 templates.
        
    Returns:
        bool: True if generation succeeded, False otherwise.
    """
    try:
        from json_schema_for_humans.generate import generate_from_filename
        from json_schema_for_humans.generation_configuration import GenerationConfiguration
    except ImportError:
        print("Error: json-schema-for-humans not installed.")
        print("Install with: pip install json-schema-for-humans")
        return False
    
    if not schemaPath.exists():
        print(f"Warning: Schema file not found: {schemaPath}")
        return False
    
    # Ensure output directory exists
    outputPath.parent.mkdir(parents=True, exist_ok=True)
    
    # Configure generation options
    configOptions = {
        "description_is_markdown": True,
        "expand_buttons": True,
        "show_breadcrumbs": True,
        "collapse_long_descriptions": True,
        "collapse_long_examples": True,
        "link_to_reused_ref": True,
        "show_toc": True,
        "examples_as_yaml": True,
        "template_name": "js",  # Use JavaScript template for interactivity
    }
    
    # Note: Custom template support disabled due to json-schema-for-humans limitations
    # The built-in "js" template provides good interactivity
    
    try:
        config = GenerationConfiguration(**configOptions)
        generate_from_filename(str(schemaPath), str(outputPath), config=config)
        print(f"Generated: {outputPath}")
        return True
    except Exception as e:
        print(f"Error generating {outputPath}: {e}")
        return False


def generate_all_schemas(outputDir: Path, templateDir: Optional[Path] = None) -> int:
    """Generate HTML documentation for all defined schemas.
    
    Args:
        outputDir (Path): Directory for output HTML files.
        templateDir (Optional[Path]): Path to custom Jinja2 templates.
        
    Returns:
        int: Number of schemas successfully generated.
    """
    schemaMapping = get_schema_paths()
    successCount = 0
    
    for schemaName, schemaInfo in schemaMapping.items():
        sourcePath = schemaInfo["source"]
        outputPath = outputDir / schemaInfo["output"]
        title = schemaInfo["title"]
        
        print(f"Processing {schemaName} schema...")
        
        if generate_schema_html(sourcePath, outputPath, title, templateDir):
            successCount += 1
    
    return successCount


def create_placeholder_html(outputDir: Path) -> None:
    """Create placeholder HTML files for schemas that don't exist yet.
    
    This is useful during initial development when schema files may not
    be complete.
    
    Args:
        outputDir (Path): Directory for output HTML files.
    """
    schemaMapping = get_schema_paths()
    
    placeholderTemplate = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - awesIO</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .placeholder {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }}
        h1 {{ color: #333; }}
        p {{ color: #666; line-height: 1.6; }}
        .status {{ 
            display: inline-block;
            background: #ffc107;
            color: #333;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="placeholder">
        <h1>{title}</h1>
        <p>This schema documentation is being generated.</p>
        <p>The schema file may not exist yet or is still under development.</p>
        <span class="status">🚧 Under Construction</span>
    </div>
</body>
</html>
"""
    
    outputDir.mkdir(parents=True, exist_ok=True)
    
    for schemaName, schemaInfo in schemaMapping.items():
        outputPath = outputDir / schemaInfo["output"]
        sourcePath = schemaInfo["source"]
        
        # Only create placeholder if source doesn't exist and output doesn't exist
        if not sourcePath.exists() and not outputPath.exists():
            html = placeholderTemplate.format(title=schemaInfo["title"])
            with open(outputPath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Created placeholder: {outputPath}")


def main():
    """Main entry point for schema export script."""
    parser = argparse.ArgumentParser(
        description="Generate HTML documentation from awesIO YAML schemas"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent / "_static",
        help="Output directory for generated HTML files"
    )
    parser.add_argument(
        "--template-dir",
        type=Path,
        default=Path(__file__).parent / "jsfh_template",
        help="Directory containing custom Jinja2 templates"
    )
    parser.add_argument(
        "--placeholders",
        action="store_true",
        help="Create placeholder HTML for missing schemas"
    )
    
    args = parser.parse_args()
    
    print(f"awesIO Schema Export")
    print(f"Output directory: {args.output_dir}")
    print(f"Template directory: {args.template_dir}")
    print("-" * 50)
    
    # Create placeholders first if requested
    if args.placeholders:
        create_placeholder_html(args.output_dir)
    
    # Generate schema documentation
    successCount = generate_all_schemas(args.output_dir, args.template_dir)
    
    schemaMapping = get_schema_paths()
    totalCount = len(schemaMapping)
    
    print("-" * 50)
    print(f"Generated {successCount}/{totalCount} schema documents")
    
    if successCount < totalCount:
        print("Note: Some schemas may not exist yet. Use --placeholders to create stubs.")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
