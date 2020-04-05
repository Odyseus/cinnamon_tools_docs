
************
Requirements
************

.. contextual-admonition::
    :context: note
    :title: Xlets/Themes building requirements

    No mayor requirements are needed to build xlets/themes other than Python 3.5+.

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
    :title: Documentation building requirements

    - **Python 3.5+**
    - **sphinx>=1.8.1**: ``sudo pip3 install sphinx`` or install from your distribution repositories.

    .. note::

        Deep cloning required.

.. only:: html

    .. _parse-sass-requirement-reference:

.. contextual-admonition::
    :context: warning
    :title: Cinnamon theme building from Sass sources

    - **Python 3.5+**
    - **sass**: Either of the following implementations can be used to parse |Sass| files.

        + Dart Sass: `See installation instructions <https://github.com/sass/dart-sass/releases>`__.
        + SassC: Install from your distribution repositories.

.. contextual-admonition::
    :context: info
    :title: Xlets help pages building optional requirement

    - **pyuca**: ``sudo pip3 install pyuca``
