# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Generate schema HTML before building docs
schemas:
	python schema_export.py --placeholders

# Build HTML with schema generation
html: schemas
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build multi-version documentation
multiversion:
	sphinx-multiversion "$(SOURCEDIR)" "$(BUILDDIR)/html"

# Clean build directory
clean:
	rm -rf $(BUILDDIR)/*
	rm -f _static/*_schema.html

# Serve documentation locally
serve: html
	python -m http.server -d $(BUILDDIR)/html 8000

# Generate version switcher JSON
switcher:
	python generate_switcher_json.py

# Full build for deployment
deploy: clean schemas switcher
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
