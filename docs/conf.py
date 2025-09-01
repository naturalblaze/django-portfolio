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
import sys
import tomli
from datetime import date

base_path = os.path.split(os.path.join(os.path.abspath(os.path.dirname(__name__))))[0]
sys.path.append(base_path)
sys.path.append(os.path.join(base_path, "docs", "_ext"))

# Reads pyproject.toml and converts to python objects
with open(os.path.join(base_path, "pyproject.toml"), "r", encoding="utf-8") as file:
    toml = file.read()
pyproject_toml = tomli.loads(toml)


# -- Project information -----------------------------------------------------

release = pyproject_toml["project"]["version"]
project = f"{pyproject_toml['project']['name']} v{release}"
copyright = f"Copyright (c) {date.today().year}, {pyproject_toml['project']['authors'][0]['name']}"

# Reads authors from pyproject.toml and adds name to list
authors = []
for author_name in pyproject_toml["project"]["authors"]:
    authors.append(author_name.get("name"))

author = ",".join(authors)


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "myst_parser",
    "sphinxcontrib.mermaid",
    "jinja2_rendering",  # My custom extension
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
if html_theme == "alabaster":
    html_theme_options = {
        "description": f"{pyproject_toml['project']['description']}",
        "page_width": "95%",
        "body_max_width": "95%",
        "fixed_sidebar": "true",
        "github_banner": "true",
        "github_user": "naturalblaze",
        "github_repo": pyproject_toml["project"]["name"],
    }
elif html_theme == "sphinx_rtd_theme":
    html_theme_options = {
        # 'analytics_id': 'G-XXXXXXXXXX',
        # 'analytics_anonymize_ip': False,
        "logo_only": False,
        "display_version": True,
        "prev_next_buttons_location": "bottom",
        "style_external_links": False,
        "vcs_pageview_mode": "",
        "style_nav_header_background": "#2980B9",
        # Toc options
        "collapse_navigation": True,
        "sticky_navigation": True,
        "navigation_depth": 4,
        "includehidden": True,
        "titles_only": False,
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_style = "css/my_theme.css"
# Uncomment to lock mermaid version
# mermaid_version = '10.5.0'
# Allow Zoom on all mermaid diagrams
mermaid_d3_zoom = True

# This is used for render markdown using myst-parser
# see https://www.sphinx-doc.org/en/master/usage/markdown.html
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
