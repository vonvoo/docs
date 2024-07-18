# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Vonvoo'
copyright = '2024, Vonvoo'
author = 'Vonvoo'

release = '0.1'
version = '0.1.2'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = 'images/branding/logo_vonvoo.png'
html_favicon = 'images/branding/favicon.ico'

html_theme_options = {
    #'analytics_id': 'UA-xxx',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'CadetBlue',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False

# -- Options for EPUB output
epub_show_urls = 'footnote'
