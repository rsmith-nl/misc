# file: ansi.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2019 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2019-07-13T12:43:16+0200
# Last modified: 2020-05-14T19:14:06+0200
"""
Predefined ANSI escape codes.

https://en.wikipedia.org/wiki/ANSI_escape_code

Example: print red text
>>> import ansi
>>> print(ansi.fgcolor.brightred+"Danger, Will Robinson!"+ansi.fgcolor.reset)
"""

from types import SimpleNamespace


# Standard ANSI colors.
fgcolor = SimpleNamespace(
    brightred="\033[1;31m",
    brightgreen="\033[1;32m",
    brightyellow="\033[1;33m",
    brightblue="\033[1;34m",
    brightmagenta="\033[1;35m",
    brightcyan="\033[1;36m",
    brightwhite="\033[1;37m",
    red="\033[31m",
    green="\033[32m",
    yellow="\033[33m",
    blue="\033[34m",
    magenta="\033[35m",
    cyan="\033[36m",
    white="\033[37m",
    reset="\033[0m",
)

bgcolor = SimpleNamespace(
    brightred="\033[1;41m",
    brightgreen="\033[1;42m",
    brightyellow="\033[1;43m",
    brightblue="\033[1;44m",
    brightmagenta="\033[1;45m",
    brightcyan="\033[1;46m",
    brightwhite="\033[1;47m",
    red="\033[41m",
    green="\033[42m",
    yellow="\033[43m",
    blue="\033[44m",
    magenta="\033[45m",
    cyan="\033[46m",
    white="\033[47m",
    reset="\033[0m",
)

control = SimpleNamespace(
    CHA="\033[1G",  # move cursor to column 1
    EL="\033[0K",  # clear to end of line
    EL2="\033[2K",  # clear whole line
    ED="\033[0J",  # clear to end of screen
    ED2="\033[2J",  # clear whole screen
    CUU="\033[1A",  # move cursor up one line
    CUD="\033[1B",  # move cursor down one line
    CUF="\033[1C",  # move cursor forward one column
    CUB="\033[1D",  # move cursor backward one column
)
