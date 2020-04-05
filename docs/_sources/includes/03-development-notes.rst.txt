
*****************
Development notes
*****************

Xlets development *commandments*
================================

- Eradicate from your thoughts the existence of Node.js. I can do infinitely more with just ten lines of Python code than with ten lines of JavaScript code that depend on 10 Node.js modules with a thousand lines of code each.
- If a Python module is required for xlets development, make it part of the Python application if possible. Otherwise, create a mechanism to install required modules.
- Try to use ``Mainloop.idle_add`` inside the initialization code of an xlet if possible. Take into account the following:

    + The ``_expandAppletContextMenu`` and the ``_bindSettings`` method calls should NOT be inside ``Mainloop.idle_add``.
    + Avoid using ``Mainloop.idle_add`` inside an extension code for obvious reasons.
    + Be aware of using ``Mainloop.idle_add`` inside a *very advanced* xlet. For example, using ``Mainloop.idle_add`` to delay the initialization of the **Window list applet** or the **System Tray applet** will inevitably break these applets initialization processes.

.. _custom-settings-framework-countermeasures-reference:

- Countermeasures for xlets that make use of the custom settings framework:

    + Applets:

        * Never use the ``external-configuration-app`` key in their metadata.json files. Cinnamon executes the application specified in this key without arguments, and the custom settings framework application needs arguments to be passed (the applet instance ID, its UUID, etc.).
        * Always override the applet's **Configure...** context menu item to force the opening of the custom settings framework application.

    + Extensions:

        * Always use the ``external-configuration-app`` key in their metadata.json files. Since I make the application for extensions purposely not to need arguments (so it can be opened from a .desktop file), specify this key so the application can be opened from the extensions manager window.
        * Always create a .desktop file to open the settings window. So one doesn't have to go all the way to the extensions manager window to open it; it can be opened directly from the applications menu.

    .. contextual-admonition::
        :context: warning
        :title: About Cinnamon's native settings system

        Up to Cinnamon 3.8.x (|IIRC|), if using an external application for an xlet settings (``external-configuration-app`` key in **metadata.json**) and at the same time inside the xlet folder exists the file **settings-schema.json**, then Cinnamon will not open the external application, it will open instead its native settings window. To overcome this, I also add a button to be displayed in the native settings system to open the *real* settings window (the one defined in ``external-configuration-app`` key). But even that will not work in certain Cinnamon versions in which buttons aren't functional. And that's why I provide the function to create a .desktop file to open the *real* settings window.


z_config.py file inside xlets directories
=========================================

This file contains a single variable called **settings** (a dictionary). These settings are read and applied when an xlet is built.

.. note::

    I was forced to implement this configuration file due to one single reason. If I manually create the symbolic links inside the xlets folders, and since I'm working directly inside a Dropbox folder, the symbolic links are constantly *resolving themselves* (a Dropbox *feature*). So I came up with the idea of creating those symbolic links when the xlets are built.

Example
-------

.. code:: python

    settings = {
        "symlinks": {
            "3.8": [
                ("../icons", "icons"),
                ("../applet.js", "applet.js"),
                ("../HELP.html", "HELP.html"),
                ("../icon.png", "icon.png"),
                ("../utils.js", "utils.js")
            ]
        }
        "make_pot_additional_files": [
            "../../__app__/data/python_modules/xlets_settings/__init__.py",
            "../../__app__/data/python_modules/xlets_settings/SettingsWidgets.py",
            "../../__app__/data/python_modules/xlets_settings/TreeListWidgets.py"
        ],
        "extra_files": [{
            "source": "__app__/data/python_modules/xlets_settings",
            "destination": "python_modules/xlets_settings"
        }]
    }


``symlinks`` key
----------------

The main use of the ``symlinks`` key is to generate symbolic links to files in the root folder of an xlet inside a *version sub-folder* to be used by **multiversion** enabled xlets.

This key is a dictionary of keys representing a sub-folder name inside an xlet directory. Each key contains a list of tuples representing the symbolic link target as its first index and the symbolic link name as its second index.

In the example above, the ``symlinks`` key will generate the symbolic links inside a folder called **3.8** (the folder will be created if it doesn't exists). The first tuple will be used to create a symbolic link called **icons** whose target will be **../icons** and so on.

.. warning::

    It's important to make all symbolic links targets relative, not absolute.

``make_pot_additional_files`` key
---------------------------------

A list of paths to files relative to an xlet source directory. These files are scanned for translatable strings when generating an xlet translation template.

``extra_files`` key
-------------------

A list of extra files/folders to copy into an xlet folder at build time. Each element on the list should be a dictionary with only two keys (``source`` and ``destination``). The ``source`` should be a path relative to the repository root folder and the ``destination`` should be a path relative to the xlet folder.

``min_cinnamon_version_override`` and ``max_cinnamon_version_override`` keys
----------------------------------------------------------------------------

These keys values should be a float representing the minimum/maximum Cinnamon version an xlet can be installed on. They are used to override the minimum/maximum version hardcoded in the Python application and that are used at xlet build time to generate a range of versions to be used by the ``cinnamon-version`` key found in an xlet metadata.json file.


z_create_localized_help.py file inside xlets directories
========================================================

This file is used to generate the **HELP.html** page for each xlet. The **HELP.html** file is an HTML document located at the root of an xlet folder.

.. contextual-admonition::
    :context: info
    :title: Why this method of creating the **HELP.html** file?

    I explored several ways of creating a help file with translated content. This one is the most optimal and less dependent of external tools.

    - I have the power as to what should be considered a string that needs to be translated or not.
    - I can write in basic markdown or pure HTML indistinctly. So I can write simple things as paragraphs or complex things as HTML tables without making the source code visible in the translation templates. And even if there are some markup exposed, it's just Markdown, which means that it will not break HTML rendering when *bad markup* is found.
    - The Python modules that this method depends on are very simple, one-file-only, and non dependent of third-party Python modules. So I have them integrated in the repository and I can even expand their capabilities if I need to.


.. contextual-admonition::
    :context: info
    :title: What I have considered and discarded

    - Sphinx

        - By itself, Sphinx has hundreds of moving parts (Python modules and/or external tools).
        - Its internationalization capabilities are too complex.
        - In my tests I found out that almost every single translatable string contained markup (reStructuredText), which is simply *suicidal*.
        - Generating one single HELP.html file that is at the same time self contained is practically impossible.

    - Translate Toolkit

        - None of its converters, tools, and scripts gave me the power that I get with the method that I ended up using.


Help pages HTML assets
----------------------

- `Bootstrap 4 <https://getbootstrap.com/>`__ is used as a |CSS| framework. No Bootstrap JavaScript plugins nor jQuery is used.
- Using my own Boostrap 4 theme built with `Bootstrap Themes Generator <https://gitlab.com/PythonCLIApplications/BootstrapThemesGenerator>`__ and based on `Bootswatch's <https://bootswatch.com>`__ `Flatly theme <https://bootswatch.com/flatly>`__. Only because the colors of the default Bootstrap theme are abhorrent.
- JavaScript is only used for the page localization mechanism and a smooth scroll effect when clicking in-line links.


Main class methods overview (more details in API documentation)
---------------------------------------------------------------

- **get_content_base:** Basic information about the xlet.
- **get_content_extra:** Detailed information about the xlet.
- **get_css_custom:** Additional |CSS| styles.
- **get_js_custom:** Some custom |JS| in case that the page needs it.

OpenGL shaders
==============

While developing one of my xlets, I was forced to learn an entire new programming language called GLSL (OpenGL Shading Language). Which is similar to HLSL (High Level Shading Language). **To be continued...**

JavaScript/CJS nonsense countermeasures
=======================================

Signals management
------------------

- Always use the signal manager provided by Cinnamon (/usr/share/cinnamon/js/misc/signalManager.js) when possible.
- When using the ``SignalManager``, **do not use arrow functions** for the ``callback`` parameter, and **always without exceptions** bind the callbacks.
- **Never** use the ``bind`` parameter of the ``SignalManager.connect`` method. This is just to avoid *confusion* (my own).

.. contextual-admonition::
    :title: Why?

    Because CJS is stupid enough to attempt to disconnect signals that do not exist anymore.

Xlets settings handling (/usr/share/cinnamon/js/ui/settings.js)
---------------------------------------------------------------

- For extensions using Cinnamon's native settings system, always use the JavaScript global module found at ``__app__/data/javascript_modules/xletsSettingsUtils.js`` (``CustomExtensionSettings`` class). This is to be able to use the settings from any module without the need to pass the settings object or a setting value as an argument.
- For applets/desklets, always instantiate Cinnamon's native settings system from inside the main xlet object (the one returned when ``main()`` is called). This will force to pass the xlet object or a setting value as arguments, but it is needed because for applets/desklets, an xlet instance ID needs to be used to instantiate the settings object.

GObject APIs nonsense countermeasures
=====================================

Gio
---

Abandon the use of the ``xdg-open`` command to open URLs/URIs with the default application registered to handle them in favor of calling :py:class:`Gio.AppInfo.launch_default_for_uri_async`, which isn't currently available on Ubuntu 16.04 base.

The goal is to eliminate the dependency on the ``xdg-open`` command, although it being used by Cinnamon itself, it might be removed any second from it. Furthermore, :py:class:`Gio.AppInfo.launch_default_for_uri_async` is better equipped to handle errors.

.. note::

    - Maybe create a function in the ``spawnUtils.js`` global module.
    - Handle passed paths and convert them into URIs. ¬¬
