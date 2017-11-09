#! /usr/bin/env python

from utils.vxPython import vxConsole

nodeip = '10.64.106.50'
port = '2006'
t = vxConsole(nodeip,port)
for reg in range(4095):
    cmd = 'drvAD9554RegRead ' +repr(reg) 
    print  t.cmd(cmd)
