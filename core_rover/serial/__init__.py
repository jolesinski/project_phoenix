#!/usr/bin/env python 

# portable serial port access with python
# this is a wrapper module for different platform implementations
#
# (C) 2001-2010 Chris Liechti <cliechti@gmx.net>
# this is distributed under a free software license, see license.txt

VERSION = '2.5'

import sys

if not (sys.platform == 'cli'):
    import os
    # chose an implementation, depending on os
    if os.name == 'posix':
        from serialposix import *
    else:
        raise Exception("Sorry: no implementation for your platform ('%s') available" % os.name)
else:
    raise Exception("Sorry: no implementation for your platform available")
