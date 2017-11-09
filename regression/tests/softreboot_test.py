#! /usr/bin/env python
# test case only works if something is configured on card as "disable linetiming" only comes when card is configured
import os
import sys
import time

if os.path.realpath('/ws/marigcha-bgl/regression/utils/') not in sys.path:
    sys.path.append(os.path.realpath('/ws/marigcha-bgl/regression/utils/')) # put dir containing this file in path

import vxConsole

(cardConsoleIp,cardConsolePort,portid)  = ('10.64.108.116',2050,'4-2-1')

card = vxConsole.vxConsole(cardConsoleIp, cardConsolePort) 
card.t.logfile = sys.stdout
card.sendline('reboot')
card.t.expect_exact('disable Linetiming',timeout = None)
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "one reboot done"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
