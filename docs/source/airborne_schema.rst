======================
Airborne System Schema
======================

The airborne system schema (``airborne_schema.yml``) defines the specification 
for AWE airborne components, including kites, wings, and onboard equipment.

Schema Overview
===============

The airborne schema covers:

* **Metadata** - Identification and classification
* **Geometry** - Wing dimensions and shape
* **Mass Properties** - Weight distribution and inertia
* **Aerodynamics** - Lift, drag, and performance
* **Structural Properties** - Material and stiffness (optional)
* **Tether Attachment** - Connection point specifications

Quick Reference
===============

Required Fields
---------------

* ``metadata.name`` - Airborne system name
* ``geometry.wing_span_m`` - Wing span in meters
* ``geometry.wing_area_m2`` - Wing area in square meters
* ``mass_properties.total_mass_kg`` - Total mass in kilograms

Example
-------

.. code-block:: yaml

   $id: example_kite
   $schema: airborne_schema.yml
   
   metadata:
     name: "Example Soft Kite"
     awe_type: "ground_gen"
   
   geometry:
     wing_span_m: 25.0
     wing_area_m2: 150.0
     aspect_ratio: 4.17
   
   mass_properties:
     total_mass_kg: 450.0
   
   aerodynamics:
     cl_max: 1.4
     glide_ratio: 12.5

Full Schema Reference
=====================

The interactive schema documentation below provides complete field descriptions,
types, and constraints.

.. raw:: html

   <iframe src="../_static/airborne_schema.html" 
           width="100%" 
           height="800px" 
           frameborder="0"
           style="border: 1px solid #ddd; border-radius: 4px;">
   </iframe>

.. note::
   If the schema viewer above doesn't load, you can view the 
   `raw schema file <https://github.com/awegroup/awesIO/blob/main/src/awesio/schemas/airborne_schema.yml>`_ 
   on GitHub.

Related Schemas
===============

* :doc:`tether_schema` - Tether connected to the airborne system
* :doc:`ground_station_schema` - Ground equipment
* :doc:`operational_constraints_schema` - Operating limits
