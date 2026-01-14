==============================
Operational Constraints Schema
==============================

The operational constraints schema (``operational_constraints_schema.yml``) 
defines operating limits and safety boundaries for AWE systems.

Schema Overview
===============

The operational constraints schema covers:

* **Wind Limits** - Cut-in, rated, and cut-out wind speeds
* **Tether Limits** - Force and speed constraints
* **Altitude Limits** - Operating height boundaries
* **Safety Margins** - Derating factors and reserves

Quick Reference
===============

Required Fields
---------------

* ``metadata.name`` - Constraint set name
* ``wind_limits.cut_in_m_s`` - Cut-in wind speed
* ``wind_limits.cut_out_m_s`` - Cut-out wind speed

Example
-------

.. code-block:: yaml

   $id: example_constraints
   $schema: operational_constraints_schema.yml
   
   metadata:
     name: "Standard Operating Envelope"
     description: "Operational limits for 500kW system"
   
   wind_limits:
     cut_in_m_s: 3.0
     rated_m_s: 11.0
     cut_out_m_s: 25.0
     survival_m_s: 50.0
   
   tether_limits:
     max_force_n: 150000
     min_force_n: 5000
     max_speed_m_s: 25.0
   
   altitude_limits:
     min_altitude_m: 50.0
     max_altitude_m: 500.0
     restricted_zones: []
   
   safety_margins:
     force_safety_factor: 2.0
     power_derating: 0.95

Operating Envelope
==================

Wind Speed Regions
------------------

.. code-block:: text

   Power
     ^
     |          ___________
     |         /           \
     |        /             \
     |       /               \
     |______/                 \______
     |     |    |         |   |
     +-----+----+---------+---+------> Wind Speed
        cut-in rated   cut-out

**Region 1**: Below cut-in
  - System parked or in standby
  - No power generation

**Region 2**: Cut-in to rated
  - Optimal power tracking
  - Power increases with wind speed

**Region 3**: Rated to cut-out
  - Power regulation active
  - Constant rated power output

**Region 4**: Above cut-out
  - System shutdown or storm mode
  - Safety priority

Altitude Constraints
--------------------

.. code-block:: yaml

   altitude_limits:
     min_altitude_m: 50.0       # Obstacle clearance
     max_altitude_m: 500.0      # Regulatory / tether limit
     
     # Optional: restricted zones
     restricted_zones:
       - name: "Airport approach"
         min_altitude_m: 0
         max_altitude_m: 150
         azimuth_start_deg: 45
         azimuth_end_deg: 135

Tether Constraints
------------------

.. code-block:: yaml

   tether_limits:
     # Force limits
     max_force_n: 150000        # Derated from breaking strength
     min_force_n: 5000          # Avoid slack tether
     
     # Speed limits
     max_reel_out_speed_m_s: 15.0
     max_reel_in_speed_m_s: 25.0
     
     # Length limits
     min_length_m: 100.0
     max_length_m: 600.0

Safety Factors
==============

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Parameter
     - Typical Value
     - Description
   * - Tether safety factor
     - 2.0 - 3.0
     - Breaking strength / max operating force
   * - Power derating
     - 0.90 - 0.98
     - Account for losses and margins
   * - Wind gust factor
     - 1.2 - 1.5
     - Peak/mean wind ratio

Full Schema Reference
=====================

.. raw:: html

   <iframe src="../_static/operational_constraints_schema.html" 
           width="100%" 
           height="800px" 
           frameborder="0"
           style="border: 1px solid #ddd; border-radius: 4px;">
   </iframe>

Related Schemas
===============

* :doc:`tether_schema` - Tether specifications
* :doc:`ground_station_schema` - Ground station limits
* :doc:`power_curves_schema` - Power output affected by constraints
