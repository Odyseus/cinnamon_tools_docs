
*****
Usage
*****

.. only:: html

    .. hint::

        This Python application can generate a system executable with Bash completions support. See :ref:`system-executable-reference`.

.. only:: man

    Hint
    ====

    This Python application can generate a system executable with Bash completions support. See ``app.py generate``.

Synopsis
========

.. only:: html

    .. docopt-docstring:: cinnamontools

.. only:: man

    .. custom-literalinclude:: cinnamontools-usage

    .. I'm forced to do this nonsense because the absolutely retarded .. only:: directive
    .. screws up title levels when building man pages. ¬¬

    .. include:: ./00-requirements-man.restructuredtext


Detailed Usage
==============

General app.py options
----------------------

- ``-h`` or ``--help``: Display basic command line usage.
- ``--manual``: Display the application manual page.
- ``-r`` or ``--restart-cinnamon``: Restart Cinnamon's shell.

app.py menu
-----------

This command starts a |CLI| menu from which xlets and themes can be built interactively.


.. only:: html

    .. _how-to-build-xlets-reference:

app.py build
------------

This command is used to build all or specific xlets. All xlets found in Cinnamon Tools' repository aren't directly usable, they need to be *built*. *Building* an xlet just means that the *raw xlet* (as found in the repository) will be copied into another location (chosen when performing the building) and a string substitution will be done that will apply a generated UUID (``xlet_name@custom_domain_name``) to all files (files content and file names). It will also compile the ``gsettings`` files (if an xlet contains such files) and copy files common to all xlets (LICENSE.md, localizations installer script, global modules, etc.).

Options
^^^^^^^

- ``-x <name>`` or ``--xlet=<name>``: Specify one or more xlets to build.

    + Example usage: ``app.py build -x 0ArgosForCinnamon -x 0CinnamonTweaks``
    + This command will build the Argos for Cinnamon applet and the Cinnamon Tweaks extension into the default output directory.


.. only:: html

    .. _build-command-option-domain-reference:

- ``-d <domain>`` or ``--domain=<domain>``: To be able to build any xlet, it is necessary to specify a domain name. This domain name is then used to generate an xlet UUID (and other data). To avoid passing this command line option every time one builds xlets, a file named **domain_name** can be created inside a folder named **tmp** at the root of the repository whose only content should be the desired domain name. This command line option has precedence over the **domain_name** file. Which means that if this option is used, the domain name found in an existent **domain_name** file will be ignored.

    + Example usage: ``app.py build -x 0ArgosForCinnamon -d example.com``


    .. only:: html

        .. warning::

            The domain name isn't internally validated (yet). But it needs to comply with certain basic rules.

            - It cannot be empty.
            - It must contain only ASCII characters (A-Z[0-9]-.).
            - It **must not** begin nor end with a digit.
            - It **must not** begin nor end with a "." (period) character.
            - It must contain at least one "." (period) character.
            - It **must not** contain consecutive "." (period) characters.
            - It **must not** exceed 128 characters.

            These rules aren't necessarily standard rules to validate a domain name. But since the domain name is used to generate from file names to Gtk+ application IDs, I find it easier to comply with a set of general rules.


.. only:: html

    .. _build-command-option-output-reference:

- ``-o <dir>`` or ``--output=<dir>``: The output directory that will be used to save the built xlets. If not specified, the default storage location will be used.

    + Example usage: ``app.py build -x 0ArgosForCinnamon -o /home/user_name/.local/share/cinnamon``
    + This command will build the Argos for Cinnamon applet directly into Cinnamon's install location for xlets.

    .. only:: html

        .. warning::

            By using a custom output directory when building xlets, and if an xlet was previously built into the same location, the previously built xlet will be completely removed. There will be a confirmation dialog before proceeding with the deletion, except when the ``--no-confirmation`` option is used.

        .. note::

            The default storage location for all built xlets is **/tmp/CinnamonToolsTemp/YYYY-MM-DD_HH.MM.SS.MMM/xlet_type/xlet_uuid**. Successive builds will create new dated folders, so an old build can never be overwritten by a new build.

            Built xlets will always be created inside a folder named as the xlet type (applets or extensions). The exception to this are the themes. Themes will be directly built into the output directory.

- ``-e <dir>`` or ``--extra-files=<dir>``: Path to a folder containing files that will be copied into an xlet folder at build time.

    + Example usage: ``app.py build -x 0ArgosForCinnamon --extra-files=~/MyCinnamonToolsExtraFiles``
    + The folder passed to this option should have the same folder structure as the Cinnamon Tools repository.
    + Only two folders should exist inside this folder; one called **applets** and/or another called **extensions**. Any other content will be ignored.
    + Using the example at the beginning of this list, to add extra files to the built **0ArgosForCinnamon** xlet, those extra files should reside at ``~/MyCinnamonToolsExtraFiles/applets/0ArgosForCinnamon``.
    + Copied files that exist at the destination will be overwritten without confirmation.
    + Core xlet files cannot be copied/overwritten. More precisely, files ending with the following file extensions will be ignored: ``.js``, ``.py``, ``.xml``, ``.pot``, and ``.json``.


    .. only:: html

        .. contextual-admonition::
            :title: Why I added this option?

            I created this option for one simple reason. So users can create and use their own localizations for the xlets that they install without the need to modify the files inside the repository nor to learn advanced use of ``git``.
            Users that want to perform more in depth changes to the xlets or even create their own xlets using the Cinnamon Tools repository as a *framework* should take full advantage of ``git``. It is *as simple* as creating their own fork of the repository, making any kind of changes in a separated branch, rebasing from the upstream repository's master branch when needed/wanted.

- ``-i`` or ``--install-localizations``: Install xlets localizations after building xlets.

    .. only:: html

        .. note::

            Installing xlets localizations is only needed under the following conditions:

            - If a user wants the xlets localized into Spanish (which is the only localizations that I provide).
            - If a user creates her/his own localizations and wants to install them when building xlets.

- ``-n`` or ``--no-confirmation``: Do not confirm the deletion of an already built xlet when the ``--output`` option is used.
- ``-r`` or ``--restart-cinnamon``: Restart Cinnamon's shell after finishing the xlets building process.

.. only:: html

    .. _build-command-option-dry-run-reference:

- ``-y`` or ``--dry-run``: Do not perform file system changes. Only display messages informing of the actions that will be performed or commands that will be executed.

    .. only:: html

        .. warning::

            Some file system changes will be performed (e.g. temporary files creation).

.. only:: html

    .. _how-to-build-themes-reference:

app.py build_themes
-------------------

This command is used to build all the themes. Just like xlets, the themes found in Cinnamon Tools' repository aren't directly usable, they need to be *built*. The themes building process is interactive. The build process will ask for Cinnamon version, Cinnamon's theme default font size/family, GTK+ 3 version, shadows of windows with |CSD| , etc.

There is actually one theme in this repository, but infinite variants (color accents) can be created. The existent variant is called **GreybirdBlue** because it's the same blue used by the `Greybird <https://github.com/shimmerproject/Greybird>`__ theme.

Options
^^^^^^^

- ``-t <name>`` or ``--theme-name=<name>``: To be able to build the themes, it is necessary to specify a theme name. This theme name is then used to generate the full theme name (theme_name-theme_variant). To avoid passing this command line option every time one builds themes, a file named **theme_name** can be created at the root of the repository whose only content should be the desired theme name. This command line option has precedence over the **theme_name** file. Which means that if this option is used, the theme name found in an existent **theme_name** file will be ignored.
- ``-o <dir>`` or ``--output=<dir>``: The output directory that will be used to save the built themes. If not specified, the default storage location will be used. See :ref:`build command --output <build-command-option-output-reference>` option notes for more details.
- ``-n`` or ``--no-confirmation``: Do not confirm the deletion of an already built theme when the ``--output`` option is used. See :ref:`build command --output <build-command-option-output-reference>` option notes for more details.
- ``-r`` or ``--restart-cinnamon``: Restart Cinnamon's shell after finishing the themes building process.
- ``-y`` or ``--dry-run``: See :ref:`build command --dry-run <build-command-option-dry-run-reference>`.

.. only:: html

    .. _how-to-create-custom-variant-reference:

    .. contextual-admonition::
        :title: How to create a custom theme variant?

        1. Duplicate the folder called **GreybirdBlue** inside **themes/_variants**. Name the duplicated folder to whatever name one wants the variant theme to have. All changes described in the following steps should be made inside the newly created folder and nowhere else.
        2. Delete the folder called **_version_sensitive**. This folder will be recreated when parsing the |Sass| files.
        3. Edit the file called **config.py** with the desired colors. This file is commented to facilitate its edition.
        4. Parse the |Sass| files using the Cinnamon Tools command line application. See :ref:`app.py parse_sass <parse-sass-command-reference>`.
        5. Build the themes using the Cinnamon Tools command line application. See :ref:`app.py build_themes <how-to-build-themes-reference>`.
        6. Optionally generate the theme thumbnails. As of now, the folder **VariantName/_version_insensitive** only contains thumbnails for the Cinnamon and Gtk2/Gtk3 themes. These thumbnails are used by Cinnamon's theme selectors as themes previews. The folder **VariantName/_version_insensitive** could be ignored/removed, in which case the Cinnamon's theme selectors will use blank/generic images.

             a) The thumbnail for the Gtk2/Gtk3 theme can be created with the command ``cinnamon-preview-gtk-theme ThemeName``. The theme needs to be built and installed for the previous command to display a window using the desired theme. What remains now is to take a screenshot of the displayed window and crop it to 120x35 pixels and then copy the image to **VariantName/_version_insensitive/gtk-3.0** folder.
             b) The thumbnail for the Cinnamon theme can be any image of any size that displays the look of the Cinnamon theme in use.

            .. contextual-admonition::
                :context: warning
                :title: Note

                Needless to say, the themes need to be rebuilt after creating and placing the thumbnails into their respective places.

    .. contextual-admonition::
        :title: Detailed differences with the Mint-X theme family

        The theme is basically the **Mint-X** theme with some graphics from the **Mint-Y** theme. But with added features that were removed from the previously mentioned default themes.

        **GTK2/GTK3 themes**

        - Restored all removed scroll bars arrows.
        - Restored all removed outlines from focused elements.
        - Removed dashed lines feedback from scrolled views (affects GTK3 applications only).
        - Changed the tooltips appearance of the GTK2 theme to look like the GTK3 tooltips.

        **Cinnamon theme**

        - Changed the tooltips appearance to look like the GTK3 tooltips.
        - Removed center alignment from tooltips.
        - Changed the switches appearance to look like the GTK3 switches.
        - Removed fixed sizes for entries inside menus.
        - Removed all images that were used to create elements with gradients in favor of using CSS rules.

.. only:: html

    .. _parse-sass-command-reference:

app.py parse_sass
-----------------

This command parses the |Sass| files needed to create the themes found in this repository. It's only usefull for people that wants to create their own themes variants. See :ref:`requirements <parse-sass-requirement-reference>`.

Options
^^^^^^^

- ``-y`` or ``--dry-run``: See :ref:`build command --dry-run <build-command-option-dry-run-reference>`.

app.py dev
----------

This command is used to perform development tasks.

Options
^^^^^^^

- ``-x <name>`` or ``--xlet=<name>``: Specify one or more xlets to perform development tasks on. Without specifying any xlet, all xlets will be handled.

Sub-commands
^^^^^^^^^^^^

- ``generate_meta_file``: Generates a unified metadata file with the content of the metadata.json file from all xlets. It also contains extra data for all xlets to facilitate their development.
- ``create_localized_help``: Generates the localized **HELP.html** file for all xlets. This file is a standalone HTML file that contains detailed a description and usage instructions for each xlet. It also contains their change logs and list of contributors/mentions.
- ``generate_trans_stats``: Generates a simple table with information about missing translated strings inside the PO files.
- ``update_pot_files``: It re-generates all xlets' POT files to reflect the changes made to the translatable strings on them.
- ``update_spanish_localizations``: It updates the **es.po** files from all xlets from their respective POT files.
- ``create_changelogs``: Generates *human readable* change logs from the Git history of changes for each xlet.

.. only:: html

    .. _system-executable-reference:

app.py generate
---------------

Sub-commands
^^^^^^^^^^^^

- ``system_executable``: Create an executable for the ``app.py`` application on the system PATH to be able to run it from anywhere.

    + The system executable creation process will ask for an executable name (the default is **cinnamon-tools-cli**) and the absolute path to store the executable file (the default is **$HOME/.local/bin**).
    + It will also ask for bash completions creation.

- ``docs``: Generate this documentation page.
- ``docs_no_api``: Generate this documentation page without extracting Python modules docstrings.
- ``base_xlet``: Interactively generate a *skeleton* xlet.


Options for ``docs`` and ``docs_no_api`` sub-commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``-f`` or ``--force-clean-build``: Clear doctree cache and destination folder when building the documentation.
- ``-u`` or ``--update-inventories``: Update inventory files from their on-line resources when building the documentation. Inventory files will be updated automatically if they don't already exist.

app.py repo
-----------

Command to perform tasks in the Cinnamon Tool's Git repository. These tasks where directly integrated into this application to avoid fatal errors (a simple error could mangle the local Git repository).

Sub-commands
^^^^^^^^^^^^

- ``submodules``: Manage sub-modules.

    + ``init``: Initialize sub-modules. Only needed if the Cinnamon Tools' repository wasn't *deep cloned*.
    + ``update``: This is needed only to merge the changes done on the upstream sub-modules.

- ``subtrees``: Manage repositories handled by the subtree merge strategy.

    + ``init``: Setup sub-trees added to the Cinnamon Tools' repository.
    + ``update``: This is needed only to merge the changes done on the upstream repositories added as a sub-trees.
