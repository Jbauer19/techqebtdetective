# File: conf.py

import sys
import os

# Define the Sphinx extensions that this project will use.
# autodoc: Automatically generate API docs from docstrings.
# coverage: Check that all of your project's code is documented.
# mathjax: Render math via JavaScript.
# viewcode: Include links to the source code in API docs.
# numpydoc: Use the Numpy style in docstrings which is especially useful for data science projects.
extensions = [
    'sphinx.ext.autodoc',  
    'sphinx.ext.coverage', 
    'sphinx.ext.mathjax',  
    'sphinx.ext.viewcode', 
    'numpydoc'             
]

# Specify the path to the template files.
# These are .html or .js files which Sphinx should use for certain parts of the build process.
templates_path = ['_templates']

# Define the suffix(es) of source filenames.
source_suffix = '.rst'

# Specify the master document, i.e., the document that contains the root toctree directive.
master_doc = 'index'

# Project related information.
project = u'Greetings'
copyright = u'2014, James Hetherington'
version = '0.1'
release = '0.1'

# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
htmlhelp_basename = 'Greetingsdoc' # The name of an HTML help collection.

# Latex documentation generation set-up, latex_elements is empty dictionary with no customisations so far.
latex_elements = {
}

# This value contains list of tuples (startdocname, targetname, title, author, documentclass, toctree_only).
# They represent the documents to be included as an initial section of the document.
latex_documents = [
  ('index', 'Greetings.tex', u'Greetings Documentation',
   u'James Hetherington', 'manual'),
]

# Configuration for creating man pages
man_pages = [
    ('index', 'greetings', u'Greetings Documentation',
     [u'James Hetherington'], 1)
]

# Texinfo document configuration. Generate Texinfo documents from reStructuredText sources.
texinfo_documents = [
  ('index', 'Greetings', u'Greetings Documentation',
   u'James Hetherington', 'Greetings', 'One line description of project.',
   'Miscellaneous'),
]