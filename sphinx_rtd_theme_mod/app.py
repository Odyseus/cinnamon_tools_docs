#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os

from shutil import which
from subprocess import run

_cur_dir = os.path.abspath(os.path.dirname(__file__))
_cur_working_dir = os.path.abspath(os.getcwd())

if _cur_dir != _cur_working_dir:
    raise SystemExit("ERROR: Execute app.py from inside the folder it resides!")

_comment_extraction_tags = "TRANSLATORS"
_copyright_holder = "Odyseus"
_project_name = "Read the Docs Sphinx Theme (Mod)"
_babel_cfg = "babel.cfg"
_pot_output = "sphinx_rtd_theme_mod.pot"


USAGE_DESCRIPTION = """
Helper script to update this Sphinx theme POT and PO files.
"""


def update_all_pos():
    if which("msgmerge") is None:
        raise SystemExit("ERROR: msgmerge command needs to be available in PATH!")

    for root, dirs, files in os.walk("./locales", topdown=False):
        for fname in files:
            file_path = os.path.abspath(os.path.join(root, fname))
            rel_file_path = os.path.relpath(file_path)

            if file_path.endswith(".po"):
                print("Updating %s" % rel_file_path)

                cmd = [
                    "msgmerge",
                    "--no-fuzzy-matching",      # Do not use fuzzy matching.
                    "--previous",               # Keep previous msgids of translated messages.
                    "--backup=off",             # Never make backups.
                    "--update",                 # Update .po file, do nothing if up to date.
                    file_path,                  # The .po file to update.
                    _pot_output                 # The template file to update from.
                ]

                run(cmd, stdout=None, stderr=None)


def make_pot():
    if which("pybabel") is None:
        raise SystemExit("ERROR: pybabel command needs to be available in PATH!")

    print("Generating %s tempalte..." % _pot_output)

    cmd = [
        "pybabel",
        "extract",
        "--no-wrap",
        "--copyright-holder=%s" % _copyright_holder,
        "--project=%s" % _project_name,
        # This doesn't work. But keep it in case that it magically starts working. ¬¬
        '--add-comments="%s"' % _comment_extraction_tags,
        "--mapping=%s" % _babel_cfg,
        ".",
        "--output=%s" % _pot_output
    ]

    run(cmd, stdout=None, stderr=None)


def main():
    parser = argparse.ArgumentParser(
        description=USAGE_DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-u", "--update-all-pos",
        action="store_true",
        dest="update_all_pos",
        default=False,
        help="Update from the translation template all PO files found inside the locales folder."
    )
    parser.add_argument(
        "-m", "--make-pot",
        action="store_true",
        dest="make_pot",
        default=False,
        help="Generate the translation template."
    )

    args = parser.parse_args()

    if args.update_all_pos:
        update_all_pos()
    elif args.make_pot:
        make_pot()


if __name__ == "__main__":
    raise SystemExit(main())
