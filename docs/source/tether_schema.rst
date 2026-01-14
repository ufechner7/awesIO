=============
Tether Schema
=============

The tether schema (``tether_schema.yml``) defines the specification for AWE 
tether systems, including material properties, dimensions, and aerodynamic 
characteristics.

Schema Overview
===============

The tether schema covers:

* **Metadata** - Identification and description
* **Properties** - Material, dimensions, and strength
* **Aerodynamics** - Drag coefficient
* **Segments** - Multi-segment tether definitions (optional)

Quick Reference
===============

Required Fields
---------------

* ``metadata.name`` - Tether name
* ``properties.diameter_m`` - Tether diameter in meters
* ``properties.length_m`` - Tether length in meters

Example
-------

.. code-block:: yaml

   $id: example_tether
   $schema: tether_schema.yml
   
   metadata:
     name: "UHMWPE Main Tether"
     description: "High-strength Dyneema tether"
   
   properties:
     material: "UHMWPE"
     diameter_m: 0.012
     length_m: 500.0
     density_kg_m3: 970.0
     breaking_strength_n: 180000
     youngs_modulus_pa: 1.2e11
     drag_coefficient: 1.1

Material Properties
===================

Common tether materials and typical properties:

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20 20

   * - Material
     - Density (kg/m³)
     - Strength (MPa)
     - Modulus (GPa)
     - Notes
   * - UHMWPE (Dyneema)
     - 970
     - 3000-3500
     - 100-130
     - Most common for AWE
   * - Aramid (Kevlar)
     - 1440
     - 2800-3600
     - 60-120
     - Higher temp resistance
   * - PBO (Zylon)
     - 1540
     - 5800
     - 180-270
     - Highest strength
   * - Carbon Fiber
     - 1750
     - 3500-6000
     - 230-600
     - Used for fly-gen

Full Schema Reference
=====================

.. raw:: html

   <iframe src="../_static/tether_schema.html" 
           width="100%" 
           height="800px" 
           frameborder="0"
           style="border: 1px solid #ddd; border-radius: 4px;">
   </iframe>

Related Schemas
===============

* :doc:`airborne_schema` - Connected airborne system
* :doc:`ground_station_schema` - Ground station winch
* :doc:`operational_constraints_schema` - Tether force limits
