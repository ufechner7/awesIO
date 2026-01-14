===============
Getting Started
===============

This guide will help you get started with awesIO for describing and validating 
Airborne Wind Energy (AWE) system configurations.

What is awesIO?
===============

awesIO is a schema specification project for AWE systems. It provides:

1. **YAML Schemas** - Formal definitions of data structures for AWE components
2. **Validation Tools** - Python utilities to validate YAML files against schemas
3. **Documentation** - Comprehensive reference for all schema fields

Why Use awesIO?
---------------

* **Standardization**: Common format for exchanging AWE system data
* **Validation**: Catch configuration errors before running simulations
* **Documentation**: Self-documenting configuration files
* **Interoperability**: Share configurations between different tools and teams

Installation
============

From Git Repository
-------------------

.. code-block:: bash

   # Install latest version
   pip install git+https://github.com/awegroup/awesIO.git

   # Install specific version
   pip install git+https://github.com/awegroup/awesIO.git@v0.1.0

   # Install specific branch
   pip install git+https://github.com/awegroup/awesIO.git@develop

Development Installation
------------------------

For contributing to awesIO or local development:

.. code-block:: bash

   git clone https://github.com/awegroup/awesIO.git
   cd awesIO
   pip install -e ".[dev]"

Basic Usage
===========

Loading YAML Files
------------------

.. code-block:: python

   from awesio import load_yaml
   
   # Load any YAML file
   data = load_yaml("my_configuration.yaml")
   
   # Access data as dictionary
   print(data["metadata"]["name"])

Validating Against Schemas
--------------------------

.. code-block:: python

   from awesio import validate
   
   # Validate a wind resource file
   validated = validate(
       "wind_resource.yaml",
       schema_type="wind_resource_schema"
   )
   
   # Validate a power curves file
   validated = validate(
       "power_curves.yaml",
       schema_type="power_curves_schema"
   )

The ``validate`` function will:

* Load the YAML file
* Check it against the specified schema
* Raise ``ValidationError`` if the file is invalid
* Return the validated data if successful

Validation with Default Values
------------------------------

Schemas can define default values for optional fields:

.. code-block:: python

   from awesio import validate
   
   # Apply default values from schema
   data = validate(
       "minimal_config.yaml",
       schema_type="power_curves_schema",
       defaults=True  # Fill in missing fields with defaults
   )

Strict vs. Permissive Validation
--------------------------------

By default, validation is strict (no extra fields allowed):

.. code-block:: python

   # Strict validation (default) - extra fields cause errors
   validate(data, schema_type="wind_resource_schema", restrictive=True)
   
   # Permissive validation - extra fields are ignored
   validate(data, schema_type="wind_resource_schema", restrictive=False)

AWE System Components
=====================

awesIO defines schemas for all major AWE components:

Airborne System
---------------

The airborne system (kite) specification includes:

* **Geometry**: Wing span, chord, area, aspect ratio
* **Aerodynamics**: Lift and drag coefficients, polar curves
* **Mass Properties**: Total mass, center of gravity, inertia
* **Structural Properties**: Material specifications, stiffness

See :doc:`airborne_schema` for the complete reference.

Tether
------

The tether specification includes:

* **Dimensions**: Length, diameter
* **Material**: Density, strength, stiffness
* **Aerodynamic**: Drag coefficient

See :doc:`tether_schema` for the complete reference.

Ground Station
--------------

The ground station specification includes:

* **Winch**: Drum dimensions, motor specifications
* **Generator**: Power rating, efficiency curves
* **Control**: Reel speed limits, force limits

See :doc:`ground_station_schema` for the complete reference.

Wind Resource
-------------

The wind resource specification includes:

* **Altitude Profile**: Wind speed vs. height
* **Clustering**: Representative wind conditions
* **Probability**: Occurrence frequency of each cluster

See :doc:`wind_resource_schema` for the complete reference.

Power Curves
------------

The power curves specification includes:

* **Power vs. Wind Speed**: For each wind profile cluster
* **Operational Phases**: Reel-out, reel-in, transition
* **Cycle Timing**: Phase durations

See :doc:`power_curves_schema` for the complete reference.

Example Workflow
================

Here's a typical workflow for using awesIO in an AWE simulation:

.. code-block:: python

   from awesio import validate, load_yaml
   
   # 1. Load and validate wind resource
   wind = validate(
       "examples/wind_resource.yml",
       schema_type="wind_resource_schema"
   )
   
   # 2. Load and validate power curves
   power = validate(
       "examples/power_curves.yml",
       schema_type="power_curves_schema"
   )
   
   # 3. Use validated data in your simulation
   for cluster in wind["clusters"]:
       cluster_id = cluster["id"]
       probability = cluster["probability"]
       
       # Find corresponding power curve
       for curve in power["power_curves"]:
           if curve["profile_id"] == cluster_id:
               cycle_power = curve["cycle_power_w"]
               # ... run simulation
   
   # 4. Calculate Annual Energy Production
   aep = sum(
       p["probability_weight"] * sum(p["cycle_power_w"])
       for p in power["power_curves"]
   )

Next Steps
==========

* :doc:`examples` - Complete example configurations
* :doc:`how_to_build_a_kite_model` - Tutorial for creating kite models
* Schema references for detailed field descriptions
