========
Examples
========

This page provides complete example YAML configurations for various AWE system 
components and use cases.

Wind Resource Example
=====================

A wind resource file describes the wind conditions at a site, organized into 
representative clusters:

.. code-block:: yaml

   # Wind resource for an example AWE site
   
   $id: wind_resource_example
   $schema: wind_resource_schema.yml
   
   metadata:
     name: "Example Offshore Site"
     description: "Representative wind conditions for AWE assessment"
     n_clusters: 3
     n_wind_speed_bins: 15
     reference_height_m: 100
   
   altitudes: [50, 100, 150, 200, 250, 300, 350, 400]
   
   wind_speed_bins:
     bin_centers_m_s: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
     bin_edges_m_s: [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5]
   
   clusters:
     - id: 1
       probability: 0.45
       reference_wind_speed_m_s: 8.5
       u_normalized: [0.85, 1.0, 1.08, 1.14, 1.18, 1.21, 1.24, 1.26]
       v_normalized: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
     
     - id: 2
       probability: 0.35
       reference_wind_speed_m_s: 11.2
       u_normalized: [0.82, 1.0, 1.10, 1.17, 1.22, 1.26, 1.29, 1.32]
       v_normalized: [0.02, 0.0, -0.01, -0.02, -0.02, -0.03, -0.03, -0.03]
     
     - id: 3
       probability: 0.20
       reference_wind_speed_m_s: 5.3
       u_normalized: [0.88, 1.0, 1.06, 1.11, 1.14, 1.17, 1.19, 1.21]
       v_normalized: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

Power Curves Example
====================

Power curves describe the power output of an AWE system as a function of wind speed:

.. code-block:: yaml

   # Power curves for a ground-gen AWE system
   
   $id: power_curves_example
   $schema: power_curves_schema.yml
   
   metadata:
     name: "Example Ground-Gen System Power Curves"
     description: "Power curves for 500kW nominal system"
     awe_type: "ground_gen"
   
   reference_wind_speeds_m_s: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
   altitudes_m: [100, 150, 200, 250, 300]
   
   power_curves:
     - profile_id: 1
       probability_weight: 0.45
       u_normalized: [1.0, 1.08, 1.14, 1.18, 1.21]
       v_normalized: [0.0, 0.0, 0.0, 0.0, 0.0]
       cycle_power_w: [0, 15000, 45000, 95000, 160000, 245000, 340000, 420000, 480000, 500000, 500000, 500000, 500000]
       reel_out_power_w: [0, 25000, 70000, 145000, 245000, 370000, 500000, 600000, 680000, 700000, 700000, 700000, 700000]
       reel_in_power_w: [0, -10000, -25000, -50000, -85000, -125000, -160000, -180000, -200000, -200000, -200000, -200000, -200000]
       cycle_time_s: [0, 60, 55, 52, 50, 48, 46, 45, 44, 43, 43, 43, 43]
       reel_out_time_s: [0, 35, 32, 30, 29, 28, 27, 26, 26, 25, 25, 25, 25]
       reel_in_time_s: [0, 25, 23, 22, 21, 20, 19, 19, 18, 18, 18, 18, 18]
     
     - profile_id: 2
       probability_weight: 0.35
       u_normalized: [1.0, 1.10, 1.17, 1.22, 1.26]
       v_normalized: [0.02, -0.01, -0.02, -0.02, -0.03]
       cycle_power_w: [0, 18000, 52000, 110000, 185000, 280000, 380000, 460000, 500000, 500000, 500000, 500000, 500000]
       reel_out_power_w: [0, 30000, 80000, 165000, 280000, 420000, 550000, 650000, 700000, 700000, 700000, 700000, 700000]
       reel_in_power_w: [0, -12000, -28000, -55000, -95000, -140000, -170000, -190000, -200000, -200000, -200000, -200000, -200000]
       cycle_time_s: [0, 58, 53, 50, 48, 46, 44, 43, 42, 42, 42, 42, 42]
       reel_out_time_s: [0, 33, 30, 28, 27, 26, 25, 25, 24, 24, 24, 24, 24]
       reel_in_time_s: [0, 25, 23, 22, 21, 20, 19, 18, 18, 18, 18, 18, 18]
     
     - profile_id: 3
       probability_weight: 0.20
       u_normalized: [1.0, 1.06, 1.11, 1.14, 1.17]
       v_normalized: [0.0, 0.0, 0.0, 0.0, 0.0]
       cycle_power_w: [0, 12000, 38000, 80000, 135000, 205000, 290000, 370000, 440000, 490000, 500000, 500000, 500000]
       reel_out_power_w: [0, 20000, 60000, 125000, 210000, 315000, 430000, 530000, 620000, 680000, 700000, 700000, 700000]
       reel_in_power_w: [0, -8000, -22000, -45000, -75000, -110000, -140000, -160000, -180000, -190000, -200000, -200000, -200000]
       cycle_time_s: [0, 62, 57, 54, 52, 50, 48, 47, 46, 45, 44, 44, 44]
       reel_out_time_s: [0, 36, 33, 31, 30, 29, 28, 27, 27, 26, 26, 26, 26]
       reel_in_time_s: [0, 26, 24, 23, 22, 21, 20, 20, 19, 19, 18, 18, 18]

Airborne System Example
=======================

An airborne system configuration describes the kite:

.. code-block:: yaml

   # Airborne system (kite) configuration
   
   $id: example_kite
   $schema: airborne_schema.yml
   
   metadata:
     name: "Example Soft Kite"
     description: "500kW class leading edge inflatable kite"
     awe_type: "ground_gen"
   
   geometry:
     wing_span_m: 25.0
     wing_area_m2: 150.0
     aspect_ratio: 4.17
     mean_chord_m: 6.0
   
   mass_properties:
     total_mass_kg: 450.0
     center_of_gravity:
       x_m: 0.0
       y_m: 0.0
       z_m: 0.5
   
   aerodynamics:
     cl_max: 1.4
     cl_design: 1.0
     cd_min: 0.08
     glide_ratio: 12.5
     lift_curve_slope: 5.5

Ground Station Example
======================

A ground station configuration:

.. code-block:: yaml

   # Ground station configuration
   
   $id: example_ground_station
   $schema: ground_station_schema.yml
   
   metadata:
     name: "Example Ground Station"
     description: "500kW class ground station with drum winch"
   
   winch:
     drum_diameter_m: 1.2
     drum_width_m: 0.8
     max_tether_speed_m_s: 25.0
     max_tether_force_n: 150000
   
   generator:
     rated_power_w: 500000
     efficiency: 0.92
     max_torque_nm: 25000

Tether Example
==============

A tether specification:

.. code-block:: yaml

   # Tether configuration
   
   $id: example_tether
   $schema: tether_schema.yml
   
   metadata:
     name: "Example UHMWPE Tether"
     description: "High-strength Dyneema tether"
   
   properties:
     material: "UHMWPE"
     diameter_m: 0.012
     length_m: 500.0
     density_kg_m3: 970.0
     breaking_strength_n: 180000
     youngs_modulus_pa: 1.2e11
     drag_coefficient: 1.1

Using Examples with Validation
==============================

Load and validate these example files:

.. code-block:: python

   from awesio import validate
   
   # Validate wind resource
   wind = validate(
       "examples/wind_resource.yml",
       schema_type="wind_resource_schema"
   )
   print(f"Loaded wind resource with {len(wind['clusters'])} clusters")
   
   # Validate power curves
   power = validate(
       "examples/power_curves.yml",
       schema_type="power_curves_schema"
   )
   print(f"Loaded {len(power['power_curves'])} power curve profiles")
   
   # Validate with defaults applied
   data = validate(
       "examples/minimal_config.yml",
       schema_type="airborne_schema",
       defaults=True
   )

AWE Architecture Examples
=========================

Ground-Generation (Pumping) System
----------------------------------

Ground-gen systems generate electricity at the ground station via a tethered kite 
performing cyclic flight patterns:

* Kite flies crosswind patterns during reel-out (power generation)
* Tether reels in during low-power phase
* Net cycle power = reel-out power - reel-in power

.. code-block:: yaml

   # Ground-gen system configuration snippet
   metadata:
     awe_type: "ground_gen"
   
   operation:
     reel_out_speed_m_s: 8.0
     reel_in_speed_m_s: 12.0
     tether_force_reel_out_n: 100000
     tether_force_reel_in_n: 30000

Fly-Generation (Onboard) System
-------------------------------

Fly-gen systems carry turbines on the kite for airborne power generation:

* Multiple turbines mounted on rigid wing
* Power transmitted via electrical cable in tether
* Continuous power generation (no pumping cycle)

.. code-block:: yaml

   # Fly-gen system configuration snippet
   metadata:
     awe_type: "fly_gen"
   
   turbines:
     n_turbines: 8
     turbine_diameter_m: 2.5
     rated_power_per_turbine_w: 75000
