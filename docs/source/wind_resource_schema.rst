Wind Resource Data Schema
=========================

Schema for wind resource data with clustering information.

Schema File
------------

.. code-block:: text

   src/awesio/schemas/wind_resource_schema.yml

Example File
------------

See: ``examples/wind_resource.yml``

Validation
----------

To validate a file against this schema:

.. code-block:: python

   from awesio.validator import validate
   
   # Auto-detects schema from file metadata
   data = validate("your_file.yml")

The validator automatically detects the schema type from the ``metadata.schema`` field in your YAML file.

Schema Structure
----------------

.. jsonschema:: ../../src/awesio/schemas/wind_resource_schema.yml
