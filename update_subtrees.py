#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from subprocess import run

if __name__ == "__main__":
    cmd1 = "git subtree pull --prefix sphinx_extensions git@gitlab.com:Odyseus/sphinx_extensions.git master --squash"
    cmd2 = "git subtree pull --prefix sphinx_rtd_theme_mod git@gitlab.com:Odyseus/sphinx_rtd_theme_mod.git master --squash"
    cmd3 = "git subtree pull --prefix common_rest_abbreviations git@gitlab.com:Odyseus/common_rest_abbreviations.git master --squash"

    run(cmd1, shell=True)
    run(cmd2, shell=True)
    run(cmd3, shell=True)
