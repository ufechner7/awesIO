Operational Constraints Schema
==============================

Schema for AWES operational constraints with terrain-based azimuth zones. Supports type-specific constraints for different system types.

Schema File
------------

.. code-block:: text

   src/awesio/schemas/operational_constraints_schema.yml

Example File
------------

See: ``examples/ground_gen/soft_kite_pumping_ground_gen_operational_constraints.yml``

Validation
----------

To validate a file against this schema:

.. code-block:: python

   from awesio.validator import validate
   
   # Auto-detects schema from file metadata
   data = validate("your_file.yml")

The validator automatically detects the schema type from the ``metadata.schema`` field in your YAML file.
