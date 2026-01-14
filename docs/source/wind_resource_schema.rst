====================
Wind Resource Schema
====================

The wind resource schema (``wind_resource_schema.yml``) defines the 
specification for wind conditions at AWE sites, including altitude profiles 
and representative wind clusters.

Schema Overview
===============

The wind resource schema covers:

* **Metadata** - Site identification and data parameters
* **Altitudes** - Height levels for wind profiles
* **Wind Speed Bins** - Discretization of wind speed range
* **Clusters** - Representative wind profile groups

Quick Reference
===============

Required Fields
---------------

* ``metadata.name`` - Resource name
* ``metadata.n_clusters`` - Number of wind clusters
* ``altitudes`` - Array of height levels (meters)
* ``clusters`` - Array of cluster definitions

Example
-------

.. code-block:: yaml

   $id: offshore_wind_resource
   $schema: wind_resource_schema.yml
   
   metadata:
     name: "North Sea Site"
     n_clusters: 3
     n_wind_speed_bins: 15
     reference_height_m: 100
   
   altitudes: [50, 100, 150, 200, 250, 300]
   
   wind_speed_bins:
     bin_centers_m_s: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
     bin_edges_m_s: [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5]
   
   clusters:
     - id: 1
       probability: 0.50
       reference_wind_speed_m_s: 9.0
       u_normalized: [0.85, 1.0, 1.08, 1.14, 1.18, 1.21]
       v_normalized: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
     
     - id: 2
       probability: 0.35
       reference_wind_speed_m_s: 12.0
       u_normalized: [0.82, 1.0, 1.10, 1.17, 1.22, 1.26]
       v_normalized: [0.02, 0.0, -0.01, -0.02, -0.02, -0.03]
     
     - id: 3
       probability: 0.15
       reference_wind_speed_m_s: 5.5
       u_normalized: [0.88, 1.0, 1.06, 1.11, 1.14, 1.17]
       v_normalized: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

Wind Profile Clustering
=======================

Wind clustering reduces complex atmospheric data to representative profiles:

.. image:: https://via.placeholder.com/600x300?text=Wind+Clustering+Concept

Key Concepts
------------

**Normalized Profiles**: Wind speeds at each altitude are normalized by the 
reference height wind speed:

.. math::

   u_{normalized}(z) = \frac{u(z)}{u(z_{ref})}

**Probability**: Each cluster represents a fraction of annual conditions. 
Sum of all cluster probabilities must equal 1.0.

**u and v Components**: Horizontal wind components allow representation of 
wind direction variation with height (veering/backing).

Validation Rules
================

The wind resource schema enforces these consistency checks:

1. **Cluster count**: ``metadata.n_clusters`` must match ``len(clusters)``
2. **Array lengths**: ``u_normalized`` and ``v_normalized`` must match ``len(altitudes)``
3. **Unique IDs**: Cluster IDs must be unique and consecutive starting from 1
4. **Probability sum**: Sum of cluster probabilities should equal 1.0
5. **Bin consistency**: ``len(bin_edges)`` must equal ``len(bin_centers) + 1``

Full Schema Reference
=====================

.. raw:: html

   <iframe src="../_static/wind_resource_schema.html" 
           width="100%" 
           height="800px" 
           frameborder="0"
           style="border: 1px solid #ddd; border-radius: 4px;">
   </iframe>

Related Schemas
===============

* :doc:`power_curves_schema` - Power output for each wind cluster
* :doc:`operational_constraints_schema` - Wind speed operating limits
