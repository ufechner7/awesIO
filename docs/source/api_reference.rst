=============
API Reference
=============

This page provides the complete API reference for the awesIO Python package.

Core Functions
==============

validate
--------

.. py:function:: awesio.validate(input, schema_type, restrictive=True, defaults=False)

   Validate input data against an awesIO schema.
   
   :param input: Input data as a dictionary, or path to a YAML file.
   :type input: dict | str | Path
   :param schema_type: Schema type to validate against (e.g., ``"wind_resource_schema"``).
   :type schema_type: str
   :param restrictive: If True, reject additional properties not in schema.
   :type restrictive: bool
   :param defaults: If True, apply default values from schema.
   :type defaults: bool
   :returns: Validated data dictionary.
   :rtype: dict
   :raises FileNotFoundError: If schema file not found.
   :raises ValidationError: If validation fails.
   :raises ValueError: If data consistency checks fail.
   
   **Example:**
   
   .. code-block:: python
   
      from awesio import validate
      
      # Validate from file path
      data = validate("wind_resource.yaml", "wind_resource_schema")
      
      # Validate from dictionary
      data = validate(my_dict, "power_curves_schema", defaults=True)

load_yaml
---------

.. py:function:: awesio.load_yaml(filename, loader=None)

   Load a YAML file into a Python dictionary.
   
   Supports special features:
   
   * ``!include`` directive for including other YAML files
   * Automatic conversion of numpy arrays
   * NetCDF file loading via ``!include``
   
   :param filename: Path to the YAML file.
   :type filename: str | Path
   :param loader: Custom YAML loader (optional).
   :type loader: ruamel.yaml.YAML | None
   :returns: Dictionary representation of the YAML file.
   :rtype: dict
   
   **Example:**
   
   .. code-block:: python
   
      from awesio import load_yaml
      
      data = load_yaml("config.yaml")
      print(data["metadata"]["name"])

write_yaml
----------

.. py:function:: awesio.write_yaml(instance, foutput)

   Write a dictionary to a YAML file.
   
   Handles numpy arrays and maintains readable formatting.
   
   :param instance: Dictionary to write.
   :type instance: dict
   :param foutput: Output file path.
   :type foutput: str
   
   **Example:**
   
   .. code-block:: python
   
      from awesio import write_yaml
      
      data = {
          "metadata": {"name": "My Config"},
          "values": [1.0, 2.0, 3.0]
      }
      write_yaml(data, "output.yaml")

Schema Types
============

Available schema types for validation:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Schema Type
     - Description
   * - ``airborne_schema``
     - Airborne system (kite) specifications
   * - ``tether_schema``
     - Tether properties and dimensions
   * - ``ground_station_schema``
     - Ground station equipment specs
   * - ``wind_resource_schema``
     - Wind profile clusters and distributions
   * - ``power_curves_schema``
     - Power output vs wind speed data
   * - ``operational_constraints_schema``
     - Operating limits and boundaries

Validation Errors
=================

ValidationError
---------------

Raised when input data doesn't conform to the schema:

.. code-block:: python

   from jsonschema.exceptions import ValidationError
   from awesio import validate
   
   try:
       data = validate(invalid_data, "wind_resource_schema")
   except ValidationError as e:
       print(f"Validation failed: {e.message}")
       print(f"Failed at: {e.json_path}")

ValueError
----------

Raised for data consistency errors (e.g., array length mismatches):

.. code-block:: python

   try:
       data = validate(inconsistent_data, "wind_resource_schema")
   except ValueError as e:
       print(f"Consistency error: {e}")

FileNotFoundError
-----------------

Raised when schema or input file doesn't exist:

.. code-block:: python

   try:
       data = validate("missing.yaml", "wind_resource_schema")
   except FileNotFoundError as e:
       print(f"File not found: {e}")

Module Reference
================

awesio.validator
----------------

.. py:module:: awesio.validator

Main validation module.

**Functions:**

* :py:func:`validate` - Main validation function
* ``_validate_data_consistency`` - Internal consistency checks
* ``_validate_cluster_count`` - Cluster count validation
* ``_validate_wind_resource_consistency`` - Wind resource checks
* ``_validate_power_curves_consistency`` - Power curves checks

awesio.yaml
-----------

.. py:module:: awesio.yaml

YAML loading and writing utilities.

**Functions:**

* :py:func:`load_yaml` - Load YAML file to dictionary
* :py:func:`write_yaml` - Write dictionary to YAML file
* ``_get_YAML`` - Get configured YAML parser instance

awesio.schemas
--------------

.. py:module:: awesio.schemas

Schema definitions and utilities.

**Attributes:**

* ``schemaPath`` - Path to schema directory
* ``schema_validation_error_formatter`` - Error message formatter

Usage Patterns
==============

Loading and Validating Pipeline
-------------------------------

.. code-block:: python

   from awesio import validate, load_yaml
   
   # Option 1: Validate directly from file
   wind = validate("wind.yaml", "wind_resource_schema")
   power = validate("power.yaml", "power_curves_schema")
   
   # Option 2: Load first, then validate dictionary
   raw_data = load_yaml("config.yaml")
   validated = validate(raw_data, "wind_resource_schema")

Applying Schema Defaults
------------------------

.. code-block:: python

   from awesio import validate
   
   # Minimal input - defaults will be filled in
   minimal = {
       "metadata": {"name": "Test"},
       "clusters": [{"id": 1, "probability": 1.0}]
   }
   
   # Validate with defaults=True to apply schema defaults
   complete = validate(minimal, "wind_resource_schema", defaults=True)

Permissive Validation
---------------------

.. code-block:: python

   from awesio import validate
   
   # Allow extra fields not in schema
   data = validate(
       "extended_config.yaml",
       "wind_resource_schema",
       restrictive=False  # Don't reject extra properties
   )

Integration with NumPy
----------------------

.. code-block:: python

   import numpy as np
   from awesio import load_yaml, write_yaml
   
   # Load data (arrays come back as lists by default)
   data = load_yaml("data.yaml")
   
   # Convert to numpy for processing
   altitudes = np.array(data["altitudes"])
   wind_speeds = np.array(data["wind_speed_bins"]["bin_centers_m_s"])
   
   # Numpy arrays are automatically converted when writing
   data["processed_values"] = np.linspace(0, 100, 50)
   write_yaml(data, "output.yaml")
