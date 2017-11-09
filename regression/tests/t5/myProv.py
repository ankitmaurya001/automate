#!/usr/bin/env python

import sys
import os
import  ConfigParser

def myCfg():
    c = ConfigParser.ConfigParser()
    c.read(os.path.expanduser('prv.ini'))
    return c
