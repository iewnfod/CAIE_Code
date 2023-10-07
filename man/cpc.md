---
title: CPC
section: 1
header: User Manual
footer: cpc 0.1.3
date: September 8, 2023
---

# NAME
cpc - An interpreter for CAIE Pseudocode.

# SYNOPSIS
**cpc** [*FILE_PATHS*] [*OPTIONS*]

# DESCRIPTION
**cpc** is a simple interpreter for *C*AIE *P*seudo*c*ode written in Python3. The language regulated by CAIE has a really retro grammar and even some grammar will not benefit both developers and the interpreter. Thus, some unimportant grammars are changed in this interpreter and even some new grammars are added. For more detailed information about this, you may look at README or <https://github.com/iewnfod/CAIE_Code>.

# OPTIONS
**-gt**
: **--get-tree**
: To show the tree of the program after being parsed

**-h**
: **--help**
: To show the help page

**-k**
: **--keywords**
: To show all the keywords

**-ne**
: **--no-error**
: To remove all error messages

**-p**
: **--parse**
: To show parse information during running

**-r**
: **--recursive-limit**
: To set the recursive limit of the interpreter

**-t**
: **--time**
: To show the time for the script to run

**-u**
: **--update**
: To check or update the version (only if *cpc* is installed with git)

**-v**
: **--version**
: To show the version of installed *cpc*

## EXAMPLE
*cpc test/test.cpc test/recursive_test.cpc -r 10000 -t -gt*

# PLAYGROUND OPTIONS
**clear**
: To remove all commands before in the playground

**help**
: To show the help page

**update**
: To check or update the version (only if *cpc* is installed with git)

# AUTHOR
Iewnfod <https://github.com/iewnfod>

# LICENSE
MIT License

Copyright (c) 2023 Iewnfod

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
