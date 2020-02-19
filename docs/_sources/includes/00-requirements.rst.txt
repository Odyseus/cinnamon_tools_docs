
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

        git clone --recurse-submodules --shallow-submodules git_repository_url

    ``--shallow-submodules`` argument is to clone the sub-modules to a depth of one commit. This is to avoid downloading a lot of unnecessary data (bootstrap 100MB+ and bootswatch 50MB+).

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
    :title: Cinnamon theme building from SASS sources

    - **Python 3.5+**
    - **sass**: Either of the following implementations can be used to parse SASS files.

        + Dart Sass: `See installation instructions <https://github.com/sass/dart-sass/releases>`__.
        + SassC: Install from your distribution repositories.

.. contextual-admonition::
    :context: info
    :title: Xlets help pages building optional requirement

    - **pyuca**: ``sudo pip3 install pyuca``
