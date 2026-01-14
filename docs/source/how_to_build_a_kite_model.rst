=========================
How to Build a Kite Model
=========================

This tutorial walks you through creating a complete kite (airborne system) model 
using awesIO schemas. By the end, you'll have a fully validated YAML configuration 
ready for use in AWE simulation tools.

Overview
========

A kite model in awesIO consists of several key components:

1. **Metadata** - Name, description, and classification
2. **Geometry** - Physical dimensions of the wing
3. **Mass Properties** - Weight distribution and inertia
4. **Aerodynamics** - Lift, drag, and performance characteristics
5. **Structural Properties** - Material and stiffness (optional)

Step 1: Start with Metadata
===========================

Every awesIO file should start with schema references and metadata:

.. code-block:: yaml

   # My first kite model
   $id: my_first_kite
   $schema: airborne_schema.yml
   
   metadata:
     name: "Tutorial Kite"
     description: "A simple kite model for learning awesIO"
     awe_type: "ground_gen"
     author: "Your Name"
     date: "2026-01-14"

The ``$id`` is a unique identifier for this configuration, and ``$schema`` 
specifies which schema to validate against.

Step 2: Define Geometry
=======================

The geometry section describes the physical dimensions of your kite:

.. code-block:: yaml

   geometry:
     # Primary dimensions
     wing_span_m: 20.0          # Tip-to-tip wingspan [m]
     wing_area_m2: 100.0        # Projected wing area [m²]
     
     # Derived parameters (should be consistent!)
     aspect_ratio: 4.0          # span² / area
     mean_chord_m: 5.0          # area / span

.. tip::
   Ensure geometric consistency: ``aspect_ratio = wing_span² / wing_area`` 
   and ``mean_chord = wing_area / wing_span``

For more complex geometry:

.. code-block:: yaml

   geometry:
     wing_span_m: 20.0
     wing_area_m2: 100.0
     aspect_ratio: 4.0
     mean_chord_m: 5.0
     
     # Optional detailed geometry
     root_chord_m: 6.5
     tip_chord_m: 3.5
     taper_ratio: 0.538         # tip_chord / root_chord
     sweep_angle_deg: 15.0      # Leading edge sweep
     dihedral_angle_deg: 5.0    # Wing dihedral

Step 3: Specify Mass Properties
===============================

Mass properties are critical for dynamic simulations:

.. code-block:: yaml

   mass_properties:
     total_mass_kg: 300.0       # Total kite mass
     
     # Center of gravity location (body-fixed coordinates)
     center_of_gravity:
       x_m: 0.0                 # Positive forward
       y_m: 0.0                 # Positive starboard
       z_m: 0.3                 # Positive down (from reference)

For detailed inertia modeling:

.. code-block:: yaml

   mass_properties:
     total_mass_kg: 300.0
     center_of_gravity:
       x_m: 0.0
       y_m: 0.0
       z_m: 0.3
     
     # Moments of inertia about CoG [kg·m²]
     inertia:
       ixx: 1500.0              # Roll inertia
       iyy: 800.0               # Pitch inertia
       izz: 2000.0              # Yaw inertia
       ixy: 0.0                 # Products of inertia
       ixz: 50.0
       iyz: 0.0

Step 4: Define Aerodynamics
===========================

Aerodynamic properties determine flight performance:

Basic Aerodynamics
------------------

.. code-block:: yaml

   aerodynamics:
     # Lift characteristics
     cl_max: 1.5                # Maximum lift coefficient
     cl_design: 1.0             # Design/cruise lift coefficient
     lift_curve_slope: 5.5      # dCL/dα [1/rad]
     
     # Drag characteristics
     cd_min: 0.06               # Minimum drag coefficient
     cd_0: 0.08                 # Zero-lift drag coefficient
     
     # Performance
     glide_ratio: 12.0          # L/D at design point

Detailed Polar Curves
---------------------

For higher-fidelity modeling, include polar curve data:

.. code-block:: yaml

   aerodynamics:
     cl_max: 1.5
     cd_min: 0.06
     glide_ratio: 12.0
     
     # Polar curve data points
     polar:
       alpha_deg: [-5, 0, 5, 10, 15, 20]
       cl: [-0.2, 0.3, 0.8, 1.2, 1.45, 1.3]
       cd: [0.08, 0.06, 0.07, 0.10, 0.16, 0.25]

Step 5: Add Tether Attachment (Optional)
========================================

Define where the tether connects to the kite:

.. code-block:: yaml

   tether_attachment:
     # Main bridle attachment point
     attachment_point:
       x_m: 0.5                 # Slightly aft of CoG
       y_m: 0.0
       z_m: 0.8                 # Below wing
     
     # Bridle configuration (if applicable)
     bridle:
       type: "three_line"
       front_line_length_m: 25.0
       rear_line_length_m: 27.0

Step 6: Complete Example
========================

Here's a complete kite model combining all elements:

.. code-block:: yaml

   # Complete kite model example
   $id: tutorial_kite_complete
   $schema: airborne_schema.yml
   
   metadata:
     name: "Tutorial Soft Kite"
     description: "A complete example of a ground-gen kite model"
     awe_type: "ground_gen"
     author: "AWE Developer"
     date: "2026-01-14"
     version: "1.0"
   
   geometry:
     wing_span_m: 20.0
     wing_area_m2: 100.0
     aspect_ratio: 4.0
     mean_chord_m: 5.0
     root_chord_m: 6.5
     tip_chord_m: 3.5
     taper_ratio: 0.538
   
   mass_properties:
     total_mass_kg: 300.0
     center_of_gravity:
       x_m: 0.0
       y_m: 0.0
       z_m: 0.3
     inertia:
       ixx: 1500.0
       iyy: 800.0
       izz: 2000.0
       ixy: 0.0
       ixz: 50.0
       iyz: 0.0
   
   aerodynamics:
     cl_max: 1.5
     cl_design: 1.0
     lift_curve_slope: 5.5
     cd_min: 0.06
     cd_0: 0.08
     glide_ratio: 12.0
     polar:
       alpha_deg: [-5, 0, 5, 10, 15, 20]
       cl: [-0.2, 0.3, 0.8, 1.2, 1.45, 1.3]
       cd: [0.08, 0.06, 0.07, 0.10, 0.16, 0.25]
   
   tether_attachment:
     attachment_point:
       x_m: 0.5
       y_m: 0.0
       z_m: 0.8

Step 7: Validate Your Model
===========================

Always validate your model before using it:

.. code-block:: python

   from awesio import validate
   
   # Validate the kite model
   kite = validate(
       "my_kite_model.yaml",
       schema_type="airborne_schema"
   )
   
   print(f"Successfully loaded: {kite['metadata']['name']}")
   print(f"Wing span: {kite['geometry']['wing_span_m']} m")
   print(f"Total mass: {kite['mass_properties']['total_mass_kg']} kg")

Common Validation Errors
------------------------

**Missing required fields:**

.. code-block:: text

   ValidationError: 'wing_span_m' is a required property

*Fix: Add the missing field to your YAML file.*

**Type errors:**

.. code-block:: text

   ValidationError: 300 is not of type 'number'

*Fix: Ensure numeric values don't have quotes.*

**Consistency errors:**

.. code-block:: text

   ValueError: Aspect ratio inconsistent with span and area

*Fix: Check that derived parameters match primary dimensions.*

Best Practices
==============

1. **Start simple** - Begin with required fields, add detail as needed
2. **Use comments** - Document your assumptions and data sources
3. **Check units** - awesIO uses SI units (meters, kilograms, seconds)
4. **Validate often** - Run validation after each major change
5. **Version control** - Track changes to your configuration files

Next Steps
==========

* :doc:`examples` - More complete configuration examples
* :doc:`airborne_schema` - Full schema reference
* :doc:`tether_schema` - Define your tether system
* :doc:`ground_station_schema` - Complete the ground station
