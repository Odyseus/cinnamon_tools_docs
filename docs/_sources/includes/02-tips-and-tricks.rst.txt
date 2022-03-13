
************************
Cinnamon tips and tricks
************************

.. note::

    Here are listed some tips, tricks and some basic concepts related to the Cinnamon desktop environment.

.. _restart-cinnamon-reference:

Restarting Cinnamon
===================

Restarting Cinnamon doesn't mean to shutdown the computer and starting it up again. It means the restart of the ``cinnamon`` process leaving all opened applications untouched. There are several ways of restarting Cinnamon:

1. With the keyboard shortcut :kbd:`Control` + :kbd:`Alt` + :kbd:`Escape`.
2. From the **Run dialog** (opened using :kbd:`Alt` + :kbd:`F2`). Typing ``restart`` or ``r`` and then pressing :kbd:`Enter` will restart Cinnamon.
3. From any panel's context menu. The **Restart Cinnamon** item inside the **Troubleshoot** sub-menu.
4. By executing the command ``nohup cinnamon --replace > /dev/null 2>&1 &`` from a terminal.

How to recover from a frozen/locked/crashed Cinnamon
====================================================

.. note::

    I will be focusing only on trying to recover Cinnamon from a totally unresponsive state caused by xlets; not by drivers, hardware failure nor other applications.

There is one basic principle that needs to be known. Every single applet/extension/desklet installed and enabled *"becomes part of Cinnamon"*. Thus, any faulty applet/extension/desklet can freeze/lock/crash Cinnamon.

If one is *lucky*, Cinnamon will crash and start the :ref:`"fallback mode" <fallback-mode-reference>`. If one is unlucky Cinnamon will be totally unresponsive.

Step 1 - Exit the X desktop session
-----------------------------------

Summary
~~~~~~~

1. :kbd:`Control` + :kbd:`Alt` + :kbd:`F1` to go to TTY1. :ref:`Can't switch TTYs? <cannot-switch-ttys-reference>`.
2. Log in.
3. Run ``top`` or ``ps`` to see that all running applications are still running.

Details
~~~~~~~

The goal here is to safely exit the X desktop session without closing any of the applications that were running previous to Cinnamon's frozen state and then come back to it. **Do not** kill the X session with :kbd:`Control` + :kbd:`Alt` + :kbd:`Backspace`; it will kill the x session along with all opened applications.

Step 2 - Perform recovery tasks
-------------------------------

Summary
~~~~~~~

1. Terminate the ``cinnamon`` process:

     a) ``killall cinnamon`` to terminate the process.
     b) ``killall -KILL cinnamon`` to murder the process without mercy.

2. Backup log files and read them:

     a) ``cp -a ~/.cinnamon/glass.log ~/Desktop/glass.log.bak`` :ref:`About ~/.cinnamon/glass.log file <glass-log-reference>`.
     b) ``cp -a ~/.xsession-errors ~/Desktop/.xsession-errors.bak``
     c) ``nano ~/.cinnamon/glass.log``
     d) ``nano ~/.xsession-errors``

3. Fix the cause of the Cinnamon crash:

     a) Remove problematic xlet/s:

          0. ``mv ~/.local/share/cinnamon/XLET_TYPE/XLET_UUID ~/Desktop/faulty_xlet``

     c) Remove the configuration files of the problematic xlet/s.

          0. ``mv ~/.cinnamon/configs/XLET_UUID ~/Desktop/faulty_config``

     d) Install possible missing dependencies.

Details
~~~~~~~

1. Terminating the ``cinnamon`` process is optional but in some cases is absolutely necessary. If an xlet is caught in an infinite loop and it's spouting a million lines of text per second into a log file and at the same time performing a heavy task like reloading the Cinnamon theme (this actually happened to me several times! LOL), one would want to kill the ``cinnamon`` process **ASAP**. Sometimes, the process can be terminated, but some other times the process needs to be killed by force. As a rule, I always terminate it since it will be restarted when going back to the X session anyways.
2. Backing up the log files is crucial to determine what caused Cinnamon to crash and to report the error to the author/s of the xlet/s that caused the crash. The backing up of the files is needed because they most likely will be overwritten. The ``glass.log`` file will be overwritten every time Cinnamon is restarted and the ``.xsession-errors`` is overwritten every time the X session is restarted.
3. Depending on the circumstances under which Cinnamon came to crash, different tasks would have to be performed:

    a) If Cinnamon crashed while enabling an extension, adding an applet to a panel or adding a desklet to the desktop, then remove the xlet. Removing the folder of an installed and enabled xlet will cause Cinnamon to fail to load it, but it will not crash Cinnamon (at least, that has been my experience so far).
    b) If Cinnamon crashed while changing an xlet setting, then remove that xlet settings file. The next time Cinnamon starts, it will recreate that settings file with default values.
    c) If by looking at the logs one determine that the crash could be caused by a missing dependency, install that dependency. This is unlikely to happen, since most xlets with external dependencies will safely check for the presence of such dependency and inform about how to proceed in case that it is missing.

Step 3 - Go back to the X desktop session
-----------------------------------------

Summary
~~~~~~~

1. Start Cinnamon with ``DISPLAY=:0 cinnamon-launcher &``.
2. Go back to the graphical TTY with :kbd:`Control` + :kbd:`Alt` + :kbd:`F7`.

Details
~~~~~~~

The goal here is to go back to the X desktop session that was previously frozen. Depending on the time it took to press the key combination to go back to the graphical TTY after executing the command to start Cinnamon, one could find the following scenarios:

    a) Cinnamon is still starting. In which case, wait for it to finish loading.
    b) A :ref:`"fallback mode" <fallback-mode-reference>` session and a dialog saying that Cinnamon crashed. This is most likely due to Cinnamon being started before the X session started, so it crashed. Pressing OK on the dialog should start Cinnamon normally.
    c) Cinnamon started normally.
    d) Cinnamon started and froze.

In the case that Cinnamon started normally, it is time to gather information and report the issue/s to the xlet/s author/s.

In the case that Cinnamon started and froze, more extreme measures will have to be taken. Repeat the actions described in steps 1 through 3. While on step 2 (**Perform recovery tasks**), one could reset all the enabled xlets or even try reseting all Cinnamon settings.

1. ``gsettings reset org.cinnamon enabled-desklets``: This will remove all desklets from the desktop.
2. ``gsettings reset org.cinnamon enabled-applets``: This will remove all third-party applets from the panel, leaving only the ones that came by default with Cinnamon.
3. ``gsettings reset org.cinnamon enabled-applets``: This will disable all extensions.
4. ``gsettings reset-recursively org.cinnamon``: This will reset all Cinnamon settings to their defaults. This will not only disable/remove all xlets, but every single Cinnamon setting (themes, fonts, panels, effects, **EVERYTHING**).


Melange/Looking Glass
=====================

Looking Glass is the Cinnamon's built-in JavaScript debugger and Melange is the Gtk+ 3 interface to it. It can be accessed as follows:

1. From any panel context menu (**Looking Glass** item inside the **Troubleshoot** sub-menu).
2. With the :kbd:`Super` + :kbd:`L` keyboard shortcut. The shortcut can be customized in **System Settings** > **Keyboard** > **Shortcuts** tab > **General** > **Troubleshooting** > **Toggle Looking Glass** entry.

From the Melange GUI one has access to several features:

1. Inspect elements of the Cinnamon UI (by pressing the button with the eyedropper icon).
2. See the list of opened windows and inspect their properties (**Windows** tab).
3. See the list of loaded xlets (applets/extensions/desklets) in the **Extensions** tab.
4. See the logged messages of any level (info, error, etc.) in the **Log** tab.
5. Evaluate JavaScript code from the text entry in the GUI.

Reload themes (useful for theme developers)
===========================================

Reload Cinnamon theme
---------------------

- Cinnamon provides a command to reload its theme. Just open the **Run command** dialog (:kbd:`Alt` + :kbd:`F2`), type ``rt`` and press :kbd:`Enter`.
- By restarting Cinnamon (this is overkill, but it does the job too). See :ref:`Restarting Cinnamon <restart-cinnamon-reference>`.

Reload Gtk+ 3 theme
-------------------

- If the currently in use Gtk+ 3 theme is being edited, switching temporarily to another theme and back to the current theme will update all opened applications to use the recently edited theme (:ref:`helper script <switch-gtk3-theme-reference>`). Sometimes, a Gtk+ 3 application needs to be restarted to correctly use the newly edited theme.
- A Gtk+ 3 theme developer will most likely be using the right tools:

    1. A developer should be using ``gtk3-widget-factory`` (program provided by the ``gtk-3-examples`` package on Debian based distributions). This program exemplifies every single Gtk+ 3 widget.
    2. A developer should know that a Gtk program can be started with an specific theme that not necessarily needs to be the currently used theme. Example: ``GTK_THEME=Adwaita gtk3-widget-factory``.
    3. A developer can test several themes at the same time without the need to change the global theme nor to restart an application. Running ``GTK_DEBUG=interactive gtk3-widget-factory`` will launch the ``gtk3-widget-factory`` program *"attached"* to the **Gtk+ 3 inspector**. In the **Visual** tab of the **Gtk+ 3 inspector**, one can switch the Gtk+ 3 theme of the application *"attached"* to it.

Gtk Inspector
=============

- The inspector can be launched attached to a Gtk application with the command ``GTK_DEBUG=interactive application``.
- To be able to launch the inspector with keyboard shortcuts (useful to inspect menus) , the package ``libgtk-3-dev`` (Debian-naming) or ``gtk3-devel`` (Fedora-naming) needs to be installed and the following **gsetting** needs to be activated:

    .. code-block:: shell

        gsettings set org.gtk.Settings.Debug enable-inspector-keybinding true

- Known keybindings:

    + :kbd:`Control` + :kbd:`Shift` + :kbd:`D`: Open Gtk inspector attached to the currently focused application.
    + :kbd:`Control` + :kbd:`Shift` + :kbd:`I`: Inspect the widget directly bellow the mouse cursor.

Modifying a shell ``$PATH``
===========================

- ``PATH`` is an environmental variable in Linux and other Unix-like operating systems that tells the shell which directories to search for executable files (i.e., ready-to-run programs) in response to commands issued by a user.
- When a terminal emulator is opened and a shell is instantiated, a shell initialization file is executed in which one can extend the ``PATH`` environmental variable.
- Each shell has its own initialization file:

    + Bash: ``~/.bashrc``
    + Zsh: ``~/.zshrc``
    + Any other shell: |RTFM|
- Add ``export PATH="/new_directory:$PATH"`` anywhere on the shell initialization file, where **new_directory** is the absolute path to the directory one wants to add.
- Restart any terminal emulator that was opened prior to the edit for the new ``PATH`` environmental variable to take effect.

.. note::

    Other shells may have other mechanisms to expand the ``PATH`` environmental variable. Just |RTFM|.

General notes
=============

.. _fallback-mode-reference:

.. contextual-admonition::
    :title: Fallback mode and software rendering mode.

    Do not confuse these totally different terms.

    - **Fallback mode**: Cinnamon **is not running** and in its place there is a basic environment that allows to run programs from a graphical user interface. Normally is the Mate panel, but could also be the Gnome panel or ``tint2`` if they are available. It depends on the distribution which of these environments is available.
    - **Software rendering mode**: Cinnamon **is running** but without video hardware acceleration. In this mode everything is purposely running slower because Cinnamon is only using the CPU and not the GPU.

.. _cannot-switch-ttys-reference:

.. contextual-admonition::
    :title: Can't switch TTYs?

    Search the web for the term *"can't switch TTYs with Ctrl+Alt+F(x)"*.

    .. hint::

        It could be a graphic driver problem or a distribution that is constantly trying to reinvent the wheel by changing the shortcuts.

.. _glass-log-reference:

.. contextual-admonition::
    :title: About ~/.cinnamon/glass.log file

    This file isn't used anymore in newer Cinnamon versions.

.. _switch-gtk3-theme-reference:

.. contextual-admonition::
    :title: Reload Gtk+ 3 theme

    Helper script to reload currently used Gtk+ 3 theme. Based on: `Ask Ubuntu <https://askubuntu.com/a/1110354>`__

    .. code-block:: bash

        function reload_gtk3_theme() {
            theme=$(gsettings get org.cinnamon.desktop.interface gtk-theme)
            gsettings set org.cinnamon.desktop.interface gtk-theme ''
            sleep 2
            gsettings set org.cinnamon.desktop.interface gtk-theme $theme
        }

