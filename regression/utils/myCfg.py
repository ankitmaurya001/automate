#!/usr/bin/env python

import sys
import os
import  ConfigParser

def myCfg():
    c = ConfigParser.ConfigParser()
    c.read(os.path.expanduser('~/labcfg.ini'))
    return c
