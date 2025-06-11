# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "multiphysics"
copyright = "2025, Multiphysics Labs, Inc"
author = "Multiphysics Labs"
language = "en"
version = "main"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

html_title = "multiphysics"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.coverage",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxemoji.sphinxemoji",
]

# sphinx_book_theme options
html_theme_options = {
    "collapse_navigation": True,
    "navigation_depth": 4,
    "repository_url": "https://github.com/multiphysicslabs/multiphysics",
    "use_repository_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/multiphysicslabs/multiphysics",
            "icon": "fa-brands fa-github",
        },
    ],
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
