# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import warnings
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'sphinx-revealjs on RTD'
copyright = '2021, Kazuya Takei'
author = 'Kazuya Takei'

# The full version, including alpha/beta/rc tags
release = '2021.9.18'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx_revealjs',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def override_builder(app, config):
    app.registry.builders["html"] = app.registry.builders["revealjs"]
    # NOTE: This is not working cachings
    # override_target = os.environ.get("TO_REVEALJS", None)
    # if not override_target:
    #     return
    # elif override_target not in app.registry.builders:
    #     warnings.warn("Ivalid target")
    #     return
    # elif "revealjs" not in app.registry.builders:
    #     warnings.warn("sphinx-revealjs is not loaded")
    #     return
    # app.registry.builders[override_target] = app.registry.builders["revealjs"]


def setup(app):
    app.connect("config-inited", override_builder)
