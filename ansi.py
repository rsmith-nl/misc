# file: ansi.py
# vim:fileencoding=utf-8:fdm=marker:ft=python
#
# Copyright © 2019 R.F. Smith <rsmith@xs4all.nl>.
# SPDX-License-Identifier: MIT
# Created: 2019-07-13T12:43:16+0200
# Last modified: 2019-07-13T12:51:59+0200

from types import SimpleNamespace

# Standard ANSI colors.
fgcolor = SimpleNamespace(
    brightred='\033[1;31m',
    brightgreen='\033[1;32m',
    brightyellow='\033[1;33m',
    brightblue='\033[1;34m',
    brightmagenta='\033[1;35m',
    brightcyan='\033[1;36m',
    brightwhite='\033[1;37m',
    red='\033[31m',
    green='\033[32m',
    yellow='\033[33m',
    blue='\033[34m',
    magenta='\033[35m',
    cyan='\033[36m',
    white='\033[37m',
    reset='\033[0m'
)

bgcolor = SimpleNamespace(
    brightred='\033[1;41m',
    brightgreen='\033[1;42m',
    brightyellow='\033[1;43m',
    brightblue='\033[1;44m',
    brightmagenta='\033[1;45m',
    brightcyan='\033[1;46m',
    brightwhite='\033[1;47m',
    red='\033[41m',
    green='\033[42m',
    yellow='\033[43m',
    blue='\033[44m',
    magenta='\033[45m',
    cyan='\033[46m',
    white='\033[47m',
    reset='\033[0m'
)
