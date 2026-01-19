===============
Developer Guide
===============

This guide covers contributing to awesIO, including code style, testing, 
documentation, and the release process.

Repository layout
=================

Key folders:

- ``src/awesio``: validation logic and schema loader
- ``src/awesio/schemas``: YAML schema files
- ``docs``: Sphinx documentation
- ``examples``: example YAML inputs
- ``scripts``: to test the schemas and validator when developing
- ``tests``: unit tests for validation logic and schemas (NEED TO BE ADDED)

Local setup
===========

Clone the repository and install dependencies:

.. code-block:: bash

	pip install -e .
	pip install -r docs/requirements.txt

Code style
==========



Testing
=======

NEED TO BE ADDED

Documentation
=============

Documentation sources are in ``docs/`` and ``docs/source/``. Build locally:

.. code-block:: bash

	cd docs
	make html

The output is written to ``docs/_build/html``.

Schema changes
==============

When updating schemas:

1. Validate against existing examples.
2. Update example files if the schema requirements change.
3. Update the schema reference pages if fields or descriptions change.

Release process
===============

1. Update version strings where relevant.
2. Update the changelog with the new version and date.
3. Tag a release following semantic versioning.

