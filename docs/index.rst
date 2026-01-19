.. awesIO documentation master file

======
awesIO
======

**YAML schemas for Airborne Wind Energy systems**

awesIO is a standardized input/output specification for Airborne Wind Energy (AWE) 
systems, providing YAML schemas that define data formats for kites, tethers, ground 
stations, wind resources, and complete AWE system configurations.

.. note::
   awesIO is inspired by and follows the architecture of 
   `windIO <https://github.com/IEAWindTask37/windIO>`_, the IEA Wind Task 37 
   ontology for traditional wind turbines.

What is awesIO?
===============

awesIO provides a common language for describing AWE systems, enabling:

* **Interoperability** between different AWE simulation tools and frameworks
* **Standardized data exchange** for research collaboration
* **Validation** of input files against formal schemas
* **Documentation** of AWE system specifications

Key Features
------------

* YAML-based schemas - Human-readable, version-controllable specifications
* Built-in validation - Automatic checking of input file correctness
* Tool integration - Works with simulation frameworks like AWESPA
* Comprehensive coverage - Schemas for all major AWE subsystems

AWE System Components
=====================

awesIO defines schemas for all major components of an Airborne Wind Energy system:

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Component
     - Description
     - Schema Reference
   * - **Airborne System**
     - Kite geometry, aerodynamics, structural properties
     - :doc:`source/airborne_schema`
   * - **Tether**
     - Tether material, dimensions, drag properties
     - :doc:`source/tether_schema`
   * - **Ground Station**
     - Winch, generator, drum specifications
     - :doc:`source/ground_station_schema`
   * - **Wind Resource**
     - Wind profile clusters, probability distributions
     - :doc:`source/wind_resource_schema`
   * - **Power Curves**
     - Power output vs. wind speed relationships
     - :doc:`source/power_curves_schema`
   * - **Operational Constraints**
     - Operating limits, safety boundaries
     - :doc:`source/operational_constraints_schema`


Getting Started
===============

Installation
------------

Install awesIO directly from the git repository:

.. code-block:: bash

   pip install git+https://github.com/awegroup/awesIO.git

Or clone and install in development mode:

.. code-block:: bash

   git clone https://github.com/awegroup/awesIO.git
   cd awesIO
   pip install -e .

Quick Example
-------------

Here's a simple example of loading and validating an AWE configuration:

.. code-block:: python

   from awesio import validate, load_yaml
   
   # Load a wind resource file
   wind_data = load_yaml("wind_resource.yaml")
   
   # Validate against the schema
   validated_data = validate(
       "wind_resource.yaml",
       schema_type="wind_resource_schema"
   )
   
   # Access validated data
   print(f"Number of clusters: {validated_data['metadata']['n_clusters']}")

Table of Contents
=================

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   source/getting_started
   source/examples
   source/how_to_build_a_kite_model

.. toctree::
   :maxdepth: 2
   :caption: Schema Reference

   source/airborne_schema
   source/tether_schema
   source/ground_station_schema
   source/wind_resource_schema
   source/power_curves_schema
   source/operational_constraints_schema

.. toctree::
   :maxdepth: 2
   :caption: Development

   source/developer_guide
   source/api_reference
   source/changelog


Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Contributing
============

awesIO is developed by the AWE research community. Contributions are welcome!

* **GitHub**: https://github.com/awegroup/awesIO
* **Issues**: https://github.com/awegroup/awesIO/issues

License
=======

awesIO is released under the MIT License. See the LICENSE file for details.
