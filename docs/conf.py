# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

"""Sphinx configuration for awesIO documentation.

This configuration follows the windIO documentation architecture, adapted for
Airborne Wind Energy (AWE) systems. Key features:
- Auto-generation of HTML schema reference pages from YAML schemas
- Multi-version documentation support via sphinx-multiversion
- GitHub Pages deployment compatibility
- Read the Docs theme integration
"""

import os
import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------
# Add the project root to the path for autodoc to find modules
projectRoot = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(projectRoot / "src"))
sys.path.insert(0, str(projectRoot / "docs"))

# -- Project information -----------------------------------------------------
project = "awesIO"
copyright = "2026, AWE Research Community"
author = "AWE Research Community"
release = "0.1.0"
version = "0.1"

# Project description for meta tags
description = "YAML schemas for Airborne Wind Energy systems"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_multiversion",
]

# Templates path
templates_path = ["_templates"]

# Patterns to exclude from source files
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The master toctree document
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

# Theme options for sphinx_rtd_theme
html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Static files path (custom CSS, generated schema HTML, etc.)
html_static_path = ["_static"]

# Custom CSS
html_css_files = [
    "custom.css",
]

# HTML context for templates
html_context = {
    "display_github": True,
    "github_user": "awegroup",
    "github_repo": "awesIO",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# -- Options for sphinx-multiversion -----------------------------------------
# Whitelist pattern for tags (x.y.z)
smv_tag_whitelist = r"^v\d+\.\d+\.\d+$"

# Whitelist pattern for branches
smv_branch_whitelist = r"^(main|develop)$"

# Whitelist pattern for remotes
smv_remote_whitelist = r"^origin$"

# Pattern for released versions
smv_released_pattern = r"^refs/tags/v\d+\.\d+\.\d+$"

# Format for versioned output directories
smv_outputdir_format = "{ref.name}"

# -- Options for intersphinx -------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# -- Napoleon settings -------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# -- Autodoc settings --------------------------------------------------------
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

# -- Build hooks for schema generation ---------------------------------------
def setup(app):
    """Set up Sphinx build hooks.
    
    This function is called by Sphinx during initialization. It registers
    a hook to auto-generate HTML schema documentation before the build starts.
    
    Args:
        app: The Sphinx application object.
    """
    app.connect("builder-inited", generate_schema_docs)


def generate_schema_docs(app):
    """Generate HTML documentation from YAML schemas.
    
    This hook runs before the documentation build and generates HTML reference
    pages from the YAML schema files using json-schema-for-humans.
    
    Args:
        app: The Sphinx application object.
    """
    import subprocess
    
    docsDir = Path(__file__).parent
    schemaExportScript = docsDir / "schema_export.py"
    
    if schemaExportScript.exists():
        print("Generating schema HTML documentation...")
        try:
            result = subprocess.run(
                [sys.executable, str(schemaExportScript)],
                cwd=str(docsDir),
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                print(f"Warning: Schema export returned non-zero: {result.stderr}")
            else:
                print("Schema HTML generation complete.")
        except Exception as e:
            print(f"Warning: Could not generate schema docs: {e}")
    else:
        print(f"Warning: schema_export.py not found at {schemaExportScript}")
