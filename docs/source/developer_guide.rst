===============
Developer Guide
===============

This guide covers contributing to awesIO, including code style, testing, 
documentation, and the release process.

Getting Started
===============

Development Setup
-----------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/awegroup/awesIO.git
      cd awesIO

2. Create a virtual environment (recommended):

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # Linux/Mac
      venv\Scripts\activate     # Windows

3. Install in development mode with dev dependencies:

   .. code-block:: bash

      pip install -e ".[dev]"

4. Verify the installation:

   .. code-block:: bash

      python -c "import awesio; print(awesio.__version__)"

Project Structure
-----------------

.. code-block:: text

   awesIO/
   ├── docs/                    # Documentation (Sphinx)
   │   ├── conf.py             # Sphinx configuration
   │   ├── index.rst           # Documentation root
   │   ├── source/             # RST source files
   │   ├── _static/            # Static files (CSS, generated HTML)
   │   └── jsfh_template/      # Schema HTML templates
   ├── examples/               # Example YAML files
   ├── src/
   │   └── awesio/
   │       ├── __init__.py
   │       ├── validator.py    # Validation functions
   │       ├── yaml.py         # YAML loading utilities
   │       └── schemas/        # YAML schema definitions
   ├── tests/                  # Test suite
   ├── pyproject.toml          # Package configuration
   └── README.md

Coding Conventions
==================

awesIO follows specific naming conventions to maintain consistency:

Naming Rules
------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Element
     - Convention
     - Example
   * - Functions
     - snake_case
     - ``validate_yaml``, ``load_schema``
   * - Variables
     - mixedCase
     - ``schemaPath``, ``validatedData``
   * - Classes
     - CamelCase
     - ``SchemaValidator``, ``YamlLoader``
   * - Methods
     - snake_case
     - ``get_schema``, ``validate_input``
   * - Constants
     - UPPER_SNAKE_CASE
     - ``DEFAULT_SCHEMA_PATH``, ``MAX_ITERATIONS``
   * - Modules
     - snake_case
     - ``validator.py``, ``schema_utils.py``
   * - Booleans
     - ``is_`` prefix for runtime variables
     - ``is_valid``, ``IS_ENABLED`` (constant)

Code Example
------------

.. code-block:: python

   """Example module following awesIO coding conventions."""
   
   from pathlib import Path
   from typing import Optional
   
   # Constants in UPPER_SNAKE_CASE
   DEFAULT_SCHEMA_VERSION = "1.0"
   MAX_VALIDATION_DEPTH = 10
   
   
   class SchemaValidator:
       """Validates YAML files against awesIO schemas.
       
       Classes use CamelCase naming.
       """
       
       def __init__(self, schemaPath: Path):
           """Initialize the validator.
           
           Args:
               schemaPath (Path): Path to the schema directory.
           """
           # Variables use mixedCase
           self.schemaPath = schemaPath
           self.loadedSchemas = {}
           self.is_initialized = False
       
       def validate_file(self, filePath: Path) -> dict:
           """Validate a YAML file against the appropriate schema.
           
           Methods use snake_case naming.
           
           Args:
               filePath (Path): Path to the YAML file.
               
           Returns:
               dict: The validated data.
           """
           # Local variables use mixedCase
           fileContent = self._load_file(filePath)
           schemaType = self._detect_schema_type(fileContent)
           validatedData = self._run_validation(fileContent, schemaType)
           
           return validatedData
       
       def _load_file(self, filePath: Path) -> dict:
           """Load a YAML file (private method)."""
           pass

Docstring Style
---------------

Use Google-style docstrings:

.. code-block:: python

   def validate(
       input: dict | str | Path,
       schema_type: str,
       restrictive: bool = True,
   ) -> dict:
       """Validate input data against an awesIO schema.
       
       Validates the provided input (either a dictionary or path to a YAML file)
       against the specified schema type.
       
       Args:
           input (dict | str | Path): Input data as a dictionary or path to
               a YAML file containing the data.
           schema_type (str): Type of schema to validate against. Must match
               a schema file in the schemas directory.
           restrictive (bool, optional): If True, reject additional properties
               not defined in the schema. Defaults to True.
       
       Returns:
           dict: The validated input data, potentially with defaults applied.
       
       Raises:
           FileNotFoundError: If the schema file is not found.
           ValidationError: If the input fails validation.
       
       Example:
           >>> from awesio import validate
           >>> data = validate("config.yaml", "wind_resource_schema")
           >>> print(data["metadata"]["name"])
       """
       pass

Testing
=======

Test Structure
--------------

Tests are located in the ``tests/`` directory:

.. code-block:: text

   tests/
   ├── test_validator.py       # Validator tests
   ├── test_yaml.py            # YAML utility tests
   ├── test_schemas.py         # Schema validation tests
   └── conftest.py             # Pytest fixtures

Writing Tests
-------------

Follow these guidelines:

* Test file names start with ``test_``
* Test function names start with ``test_``
* Use descriptive names: ``test_validate_returns_data_with_defaults``
* One assertion per test (when practical)
* Use pytest fixtures for setup

.. code-block:: python

   """Tests for the validator module."""
   
   import pytest
   from pathlib import Path
   from awesio import validate
   
   
   @pytest.fixture
   def sample_wind_resource():
       """Fixture providing sample wind resource data."""
       return {
           "metadata": {
               "name": "Test Site",
               "n_clusters": 2,
           },
           "clusters": [
               {"id": 1, "probability": 0.6},
               {"id": 2, "probability": 0.4},
           ]
       }
   
   
   def test_validate_accepts_valid_wind_resource(sample_wind_resource):
       """Test that validate accepts valid wind resource data."""
       result = validate(
           sample_wind_resource,
           schema_type="wind_resource_schema"
       )
       assert result["metadata"]["name"] == "Test Site"
   
   
   def test_validate_rejects_invalid_cluster_count(sample_wind_resource):
       """Test that validate catches cluster count mismatch."""
       sample_wind_resource["metadata"]["n_clusters"] = 5  # Wrong count
       
       with pytest.raises(ValueError, match="Cluster count mismatch"):
           validate(sample_wind_resource, schema_type="wind_resource_schema")

Running Tests
-------------

.. code-block:: bash

   # Run all tests
   pytest
   
   # Run with coverage
   pytest --cov=awesio
   
   # Run specific test file
   pytest tests/test_validator.py
   
   # Run tests matching pattern
   pytest -k "test_validate"
   
   # Verbose output
   pytest -v

Schema Development
==================

Adding a New Schema
-------------------

1. Create the schema file in ``src/awesio/schemas/``:

   .. code-block:: yaml

      # new_component_schema.yml
      $schema: "http://json-schema.org/draft-07/schema#"
      $id: new_component_schema.yml
      title: New Component Schema
      description: Schema for new AWE component
      
      type: object
      required:
        - metadata
      
      properties:
        metadata:
          type: object
          properties:
            name:
              type: string
              description: Component name

2. Update ``src/awesio/schemas/__init__.py`` if needed

3. Add documentation in ``docs/source/new_component_schema.rst``

4. Add examples in ``examples/``

5. Add tests in ``tests/``

Schema Best Practices
---------------------

* Use ``$ref`` for reusable definitions
* Provide ``description`` for all properties
* Specify ``default`` values where sensible
* Use ``enum`` for constrained string values
* Include ``examples`` in property definitions

Documentation
=============

Building Documentation
----------------------

.. code-block:: bash

   cd docs
   
   # Build HTML documentation
   make html
   
   # View locally
   python -m http.server -d _build/html

Documentation Structure
-----------------------

* **index.rst** - Main landing page
* **source/*.rst** - Content pages
* **_static/** - Generated schema HTML, CSS
* **jsfh_template/** - Custom templates for schema rendering

Adding Documentation Pages
--------------------------

1. Create RST file in ``docs/source/``
2. Add to appropriate toctree in ``index.rst``
3. Rebuild documentation

Release Process
===============

Version Numbering
-----------------

awesIO uses `Semantic Versioning <https://semver.org/>`_:

* **MAJOR**: Breaking changes to schema format
* **MINOR**: New features, backward-compatible
* **PATCH**: Bug fixes, documentation updates

Creating a Release
------------------

1. Update version in ``pyproject.toml``
2. Update changelog
3. Create git tag:

   .. code-block:: bash

      git tag -a v0.2.0 -m "Release version 0.2.0"
      git push origin v0.2.0

4. Documentation will auto-deploy via GitHub Actions

Getting Help
============

* **Issues**: https://github.com/awegroup/awesIO/issues
* **Discussions**: https://github.com/awegroup/awesIO/discussions
* **Email**: awe-group@tudelft.nl
