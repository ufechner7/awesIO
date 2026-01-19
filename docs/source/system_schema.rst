AWE System Schema
==================================

Complete schema for AWE system configurations with type-dependent validation. Validates wing, bridle, control system, tether, and ground station components.

Schema File
-----------

.. code-block:: text

   src/awesio/schemas/system_schema.yml

Example File
------------

See: ``examples/ground_gen/soft_kite_pumping_ground_gen_system.yml``

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

.. jsonschema:: ../../src/awesio/schemas/system_schema.yml
