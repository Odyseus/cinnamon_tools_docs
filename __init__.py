"""Sphinx ReadTheDocs theme.

From https://github.com/ryan-roemer/sphinx-bootstrap-theme.

"""
from os import path

__version__ = '0.4.3'
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths.
    """
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir


def setup(app):
    """See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package.
    """
    app.add_html_theme("sphinx_rtd_theme_mod", path.abspath(path.dirname(__file__)))

    # For sphinx-1.8 or later.
    # Don't fail if using Sphinx <1.8.
    try:
        rtd_locales_path = path.join(path.abspath(path.dirname(__file__)), "locales")

        if path.exists(rtd_locales_path) and path.isdir(rtd_locales_path):
            app.add_message_catalog("sphinx", rtd_locales_path)
    except Exception:
        pass
