# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.getcwd())

import pgi
pgi.install_as_gi()

from _pgi_docgen_conf import TARGET, DEPS


mname, mversion = os.path.basename(os.getcwd()).split("-", 1)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    '_ext.inheritance_diagram_fork',
    '_ext.autosummary_fork',
    '_ext.devhelp_fork',
    '_ext.toctree',
]
source_suffix = '.rst'
master_doc = 'index'
project = '%s %s - Python API' % (mname, mversion)
version = mversion
release = mversion
exclude_patterns = ['_build', 'README.rst']

intersphinx_mapping = {
    'python': ('http://docs.python.org/2.7', None),
    'cairo10': ('http://cairographics.org/documentation/pycairo/2/', None),
}

for dep_name in DEPS:
    intersph_name = dep_name.replace("-", "").replace(".", "")
    if intersph_name in intersphinx_mapping:
        # cairo
        continue

    dep = os.path.relpath(os.path.join(TARGET, dep_name))
    inv = os.path.join(dep, "objects.inv")
    if not os.path.exists(inv):
        raise SystemExit("Dependency %r not found" % dep)
    intersphinx_mapping[intersph_name] = (
        os.path.join("..", "..", "..", dep_name), inv)

html_theme_path = ['.']
html_theme = '_theme'
html_copy_source = False
html_show_sourcelink = False

inheritance_node_attrs = dict(shape='box', fontsize=7,
                              color='gray70', style='rounded')
inheritance_graph_attrs = dict(rankdir="TB", size='""', bgcolor="transparent")

autodoc_member_order = "bysource"
autodoc_docstring_signature = False
