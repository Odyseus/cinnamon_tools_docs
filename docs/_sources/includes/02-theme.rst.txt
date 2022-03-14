
***************************
Themes development/building
***************************

There is actually one theme in this repository, but 10 variants (accent colors) available. It is basically the **Mint-X** theme with some graphics from the **Mint-Y** theme. But with added features that were removed from the previously mentioned default themes.

Detailed differences with the Mint-X theme family
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**GTK2/GTK3 themes**

- Restored all removed scroll bars arrows. This is configurable. Scrollbar arrows can be hidden/shown.
- Restored all removed outlines from focused elements.
- Dashed lines feedback (undershoot) from scrolled views (affects GTK3/4 applications only) are configurable and can be hidden/shown.

**Cinnamon theme**

- Removed center alignment from tooltips.
- Changed the switches appearance to look like the GTK3 switches.
- Removed fixed sizes for entries inside menus.
- Removed all images that were used to create elements with gradients in favor of using CSS rules.

**All themes**

- I added accent color highlights to focused entries. I consider this a usability feature. The entries of the original Mint-X themes have almost no differences and their state is almost imperceptible from one another. Having a focused entry highlighted with the accent color makes it noticeable at first sight when there are more than one entry on screen.
- Tooltips homogenization and configuration. The background and foreground colors of the tooltips as well as their background and border opacity can be configured. By default all variants have tooltips with almost black background and almost white foreground colors.

.. only:: html

    .. _how-to-create-custom-variant-reference:

How to create a custom theme variant?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Duplicate any of the variant folders found inside **themes/_variants**. Name the duplicated folder to whatever name one wants the variant theme to have. All changes described in the following steps should be made inside the newly created folder and nowhere else.
2. Delete the content of the folder except for the file called **config.yaml**.
3. Edit the **config.yaml** file with the desired colors. This file is commented to facilitate its edition.
4. Parse the |Sass| files using the Cinnamon Tools command line application. See :ref:`app.py dev_themes parse_sass <dev-themes-command-reference>`.
5. Generate the variant theme thumbnails using the Cinnamon Tools command line application. See :ref:`app.py dev_themes generate_thumbnails <dev-themes-command-reference>`. These thumbnails are used by Cinnamon's theme selectors as themes previews. This step could be ignored, in which case the thumbnails in the theme selectors will be blank.
6. Build the themes using the Cinnamon Tools command line application. See :ref:`app.py build_themes <how-to-build-themes-reference>`.

.. note::

    - When creating a custom theme variant, always use ``--variant-name=<name>`` CLI option to avoid unnecessary modifications to the default theme variants.
    - **All newly added** files/folders inside the **themes/_variants** folder **will not be tracked by git**.


Customization options
^^^^^^^^^^^^^^^^^^^^^

Creating a custom variant of the theme has the advantage of having at ones finger tips the possibility to change certain core aspects of the theme that may otherwise be to complicated (or impossible) to change in a finished theme.

Variant configuration file example
""""""""""""""""""""""""""""""""""

The color named ``selected_bg_color`` is the one that defines what one might refer to as the accent color of the theme. The theme variant should be named (the folder name) as a description of the color defined in ``selected_bg_color``.

In the following example, the variant is called **GreybirdBlue** because it's the same blue used by the `Greybird theme <https://github.com/shimmerproject/Greybird>`__.

.. literalinclude:: ../../../themes/_variants/GreybirdBlue/config.yaml
    :language: python
    :prepend: # START GreybirdBlue/config.yaml
    :append: # END GreybirdBlue/config.yaml

Global themes configuration file example
""""""""""""""""""""""""""""""""""""""""

The options in this file can be overwritten by simply making a copy of this file inside the **cinnamon_tools_repository/tmp** folder and editing its content. Only the options that one wants to override need to be specified.

.. literalinclude:: ../../../themes/theme_config.yaml
    :language: python
    :prepend: # START theme_config.yaml
    :append: # END theme_config.yaml
