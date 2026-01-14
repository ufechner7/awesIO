====================
Power Curves Schema
====================

The power curves schema (``power_curves_schema.yml``) defines the specification 
for AWE power output as a function of wind speed and wind profile cluster.

Schema Overview
===============

The power curves schema covers:

* **Metadata** - System identification and type
* **Reference Data** - Wind speeds and altitudes
* **Power Curves** - Power output for each wind profile

Quick Reference
===============

Required Fields
---------------

* ``metadata.name`` - Power curves name
* ``reference_wind_speeds_m_s`` - Array of reference wind speeds
* ``power_curves`` - Array of power curve definitions

Example
-------

.. code-block:: yaml

   $id: example_power_curves
   $schema: power_curves_schema.yml
   
   metadata:
     name: "500kW System Power Curves"
     awe_type: "ground_gen"
   
   reference_wind_speeds_m_s: [3, 5, 7, 9, 11, 13, 15]
   altitudes_m: [100, 150, 200, 250]
   
   power_curves:
     - profile_id: 1
       probability_weight: 0.50
       u_normalized: [1.0, 1.08, 1.14, 1.18]
       v_normalized: [0.0, 0.0, 0.0, 0.0]
       cycle_power_w: [0, 50000, 180000, 350000, 480000, 500000, 500000]
       reel_out_power_w: [0, 80000, 270000, 510000, 680000, 700000, 700000]
       reel_in_power_w: [0, -30000, -90000, -160000, -200000, -200000, -200000]
       cycle_time_s: [0, 55, 50, 46, 44, 43, 43]
       reel_out_time_s: [0, 32, 29, 27, 26, 25, 25]
       reel_in_time_s: [0, 23, 21, 19, 18, 18, 18]

Power Curve Structure
=====================

Ground-Generation Cycles
------------------------

For pumping kite systems, power is generated in cycles:

**Reel-Out Phase** (Power Generation):

* Kite flies crosswind patterns
* High tether tension, slow reel-out
* Generator produces electricity

**Reel-In Phase** (Power Consumption):

* Kite depowered (low lift)
* Fast reel-in, low tension
* Motor consumes electricity

**Net Cycle Power**:

.. math::

   P_{cycle} = \frac{P_{out} \cdot t_{out} + P_{in} \cdot t_{in}}{t_{out} + t_{in}}

Where:

* :math:`P_{out}` = Reel-out power (positive)
* :math:`P_{in}` = Reel-in power (negative)
* :math:`t_{out}` = Reel-out time
* :math:`t_{in}` = Reel-in time

Fly-Generation Power
--------------------

For onboard generation systems:

.. code-block:: yaml

   metadata:
     awe_type: "fly_gen"
   
   power_curves:
     - profile_id: 1
       probability_weight: 1.0
       continuous_power_w: [0, 50000, 180000, 350000, 480000, 500000, 500000]

Validation Rules
================

The power curves schema enforces:

1. **Unique profile IDs**: Each ``profile_id`` must be unique
2. **Probability sum**: ``probability_weight`` values must sum to 1.0
3. **Array consistency**: Power and time arrays must match ``reference_wind_speeds_m_s`` length
4. **Profile consistency**: ``u_normalized`` and ``v_normalized`` must match ``altitudes_m`` length

Annual Energy Production
========================

Calculate AEP from power curves and wind resource:

.. code-block:: python

   from awesio import validate
   import numpy as np
   
   # Load data
   wind = validate("wind_resource.yaml", "wind_resource_schema")
   power = validate("power_curves.yaml", "power_curves_schema")
   
   # Calculate AEP
   hoursPerYear = 8760
   aep = 0.0
   
   for curve in power["power_curves"]:
       # Get probability for this profile
       prob = curve["probability_weight"]
       
       # Get power values
       cyclePower = np.array(curve["cycle_power_w"])
       
       # Simple AEP contribution (refined calculation uses Weibull)
       meanPower = np.mean(cyclePower[cyclePower > 0])
       aep += prob * meanPower * hoursPerYear
   
   print(f"Estimated AEP: {aep / 1e6:.2f} MWh/year")

Full Schema Reference
=====================

.. raw:: html

   <iframe src="../_static/power_curves_schema.html" 
           width="100%" 
           height="800px" 
           frameborder="0"
           style="border: 1px solid #ddd; border-radius: 4px;">
   </iframe>

Related Schemas
===============

* :doc:`wind_resource_schema` - Wind profiles corresponding to power curves
* :doc:`airborne_schema` - Kite specifications
* :doc:`operational_constraints_schema` - Operating limits
