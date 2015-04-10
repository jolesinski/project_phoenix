#!/usr/bin/env/ python
# =============================================================================
# File name: run.py
# Authors: Bartlomiej Lisiecki
# Python version: 2.7
# =============================================================================

from core.dispatcher import application
from werkzeug.serving import run_simple

if __name__ == '__main__':
    run_simple('localhost', 8383, application)
