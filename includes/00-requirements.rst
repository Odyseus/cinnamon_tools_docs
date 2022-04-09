
************
Requirements
************

.. contextual-admonition::
    :context: note
    :title: Xlets/Themes building requirements

    No mayor requirements are needed to build xlets/themes other than Python 3.7+. End users can simply perform the following steps:

    1. Download the source code from Cinnamon Tools' repository or from any of its mirrors and unpack it.
    2. Open a terminal from inside the extracted source code and run the command ``./app.py menu``.
    3. The CLI menu is completely interactive, just follow instructions.

.. contextual-admonition::
    :context: warning
    :title: Development tasks requirements

    Almost all development tasks require the Cinnamon Tools' repository to be *deep cloned* to checkout all the needed sub-modules.

    .. code:: shell

        git clone --recurse-submodules --shallow-submodules <cinnamon_tools_repository_url>

    - ``--recurse-submodules`` argument will also clone the sub-modules and all sub-modules that a sub-module might have.
    - ``--shallow-submodules`` argument is to clone the sub-modules to a depth of one commit to avoid downloading a huge amount of ``git`` history.

.. contextual-admonition::
    :context: warning
    :title: ``dev_xlets update_pot_files`` command requirement

    This task requires the command ``make-cinnamon-xlet-pot-cli`` to be available on **PATH**. The command is provided by the `Make Cinnamon Xlet POT <https://gitlab.com/PythonCLIApplications/MakeCinnamonXletPOT>`__ application. This application is a drop-in replacement for the ``cinnamon-xlet-makepot`` command provided by Cinnamon, but with more features designed to assist in the development of the xlets found in the Cinnamon Tools repository.

.. contextual-admonition::
    :context: warning
    :title: Documentation building requirements

    - **Python 3.7+**
    - **sphinx>=1.8.1**: Install from your distribution repositories.

    .. note::

        Deep cloning required.

.. only:: html

    .. _parse-sass-requirement-reference:

.. contextual-admonition::
    :context: warning
    :title: Gtk 3 and Cinnamon themes building from |Sass| sources

    - **Python 3.7+**
    - **Dart Sass**: `Download the appropiate release <https://github.com/sass/dart-sass/releases>`__ and `see installation instructions <https://github.com/sass/dart-sass#standalone>`__.

.. only:: html

    .. _thumbnails-generation-requirement-reference:

.. contextual-admonition::
    :context: warning
    :title: Gtk and Cinnamon themes thumbnails generation

    - **ImageMagic**: Install from your distribution repositories.

.. contextual-admonition::
    :context: info
    :title: Xlets help pages building optional requirement

    - **pyuca**: Install from your distribution repositories.

.. contextual-admonition::
    :context: info
    :title: Python virtual environment

    A Python virtual environment can be created inside the **.venv** folder at the root of the repository. The **.venv** folder is already ignored in the repository's **.gitignore** file. The virtual environment is recommended, but not required since I designed the main Python application **to work with all Python 3 versions in existence** (or NONE AT ALL).
