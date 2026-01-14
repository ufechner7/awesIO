=========
Changelog
=========

All notable changes to awesIO will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
============

Added
-----

* Initial documentation system based on windIO architecture
* Sphinx-based documentation with Read the Docs theme
* Auto-generated schema HTML reference pages
* Multi-version documentation support via sphinx-multiversion
* GitHub Pages deployment capability

[0.1.0] - 2026-01-14
====================

Added
-----

* Initial release of awesIO
* Core validation framework using jsonschema
* YAML loading utilities with ``!include`` support
* Schema definitions for:
  
  - Wind resource (``wind_resource_schema.yml``)
  - Power curves (``power_curves_schema.yml``)
  - Airborne system (``airborne_schema.yml``)
  - Ground station (``ground_station_schema.yml``)
  - Tether (``tether_schema.yml``)
  - Operational constraints (``operational_constraints_schema.yml``)

* Data consistency validation:
  
  - Cluster count matching
  - Array length consistency
  - Probability weight sum validation
  - Unique ID validation

* Example configuration files
* pip-installable package structure with pyproject.toml

Changed
-------

* N/A (initial release)

Deprecated
----------

* N/A (initial release)

Removed
-------

* N/A (initial release)

Fixed
-----

* N/A (initial release)

Security
--------

* N/A (initial release)


Migration Guide
===============

From Pre-release to 0.1.0
-------------------------

If you were using awesIO before the 0.1.0 release:

1. Update your installation:

   .. code-block:: bash

      pip install --upgrade git+https://github.com/awegroup/awesIO.git@v0.1.0

2. Schema file extensions changed from ``.yaml`` to ``.yml`` for consistency.
   Update your ``$schema`` references:

   .. code-block:: yaml

      # Old
      $schema: wind_resource_schema.yaml
      
      # New
      $schema: wind_resource_schema.yml

3. The ``validate`` function signature remains the same:

   .. code-block:: python

      from awesio import validate
      
      data = validate("config.yaml", "wind_resource_schema")
