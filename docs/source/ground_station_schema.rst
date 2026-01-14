=====================
Ground Station Schema
=====================

The ground station schema (``ground_station_schema.yml``) defines the 
specification for AWE ground-based equipment, including winches, generators, 
and control systems.

Schema Overview
===============

The ground station schema covers:

* **Metadata** - Identification and classification
* **Winch** - Drum, motor, and speed specifications
* **Generator** - Power rating and efficiency
* **Control** - Operational limits and modes

Quick Reference
===============

Required Fields
---------------

* ``metadata.name`` - Ground station name
* ``winch.max_tether_force_n`` - Maximum tether force in Newtons
* ``generator.rated_power_w`` - Rated generator power in Watts

Example
-------

.. code-block:: yaml

   $id: example_ground_station
   $schema: ground_station_schema.yml
   
   metadata:
     name: "500kW Ground Station"
     description: "Containerized ground station unit"
   
   winch:
     drum_diameter_m: 1.2
     drum_width_m: 0.8
     max_tether_speed_m_s: 25.0
     max_tether_force_n: 150000
   
   generator:
     rated_power_w: 500000
     efficiency: 0.92
     max_torque_nm: 25000

Ground Station Types
====================

Ground-Generation (Pumping)
---------------------------

Standard ground station for pumping kite systems:

.. code-block:: yaml

   ground_station_type: "pumping"
   
   winch:
     type: "single_drum"
     drum_diameter_m: 1.2
     max_tether_speed_m_s: 25.0
     max_tether_force_n: 150000
   
   generator:
     type: "PMSG"  # Permanent Magnet Synchronous Generator
     rated_power_w: 500000

Fly-Generation Support
----------------------

Ground station for fly-gen systems (primarily tether management):

.. code-block:: yaml

   ground_station_type: "fly_gen"
   
   winch:
     type: "tensioning"
     max_tether_force_n: 80000
   
   electrical:
     type: "slip_ring"
     max_current_a: 500
     voltage_v: 1000

Full Schema Reference
=====================

.. raw:: html

   <iframe src="../_static/ground_station_schema.html" 
           width="100%" 
           height="800px" 
           frameborder="0"
           style="border: 1px solid #ddd; border-radius: 4px;">
   </iframe>

Related Schemas
===============

* :doc:`tether_schema` - Tether connected to winch
* :doc:`power_curves_schema` - Power output characteristics
* :doc:`operational_constraints_schema` - Operating limits
