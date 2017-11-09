#! /usr/bin/env python
# test case only works if something is configured on card as "disable linetiming" only comes when card is configured
import os
import sys
import time
import random


if os.path.realpath('/ws/marigcha-bgl/regression/utils/') not in sys.path:
    sys.path.append(os.path.realpath('/ws/marigcha-bgl/regression/utils/')) # put dir containing this file in path

import vxConsole

(cardConsoleIp,cardConsolePort,portid)  = ('10.64.108.116',2048,'4-2-1')
(cardConsoleIp,cardConsolePort,portid)  = ('fwts7',2037,'4-2-1')

digiDevId = ['0x1f4','0x000101f5']
#############################################
nonfactoryModeRebootComplete = "Process Provisioning End !"
factoryModeRebootComplete = "Init process terminated"

rebootComplete = nonfactoryModeRebootComplete 

############################################
loop_poll = "adpt_warm_restart_handle {digiId}"
provision = True
firstTime = True
#########################################
card = vxConsole.vxConsole(cardConsoleIp, cardConsolePort,console = True ) 
card.t.logfile = open("result.txt","w")
card.sendline('\r')
card.cmd('eqaStat')
def card_warm_reboot(card):
    card.sendline('reboot')
    card.t.expect_exact(rebootComplete,timeout = None)
    time.sleep(2)

def card_cold_reboot(card):
    card.sendline('reboot 2')
    card.t.expect_exact(rebootComplete,timeout = None)
    time.sleep(2)

###########################################

#provision trunks 

card.cmd('eqaStat')
card_cold_reboot(card)

time.sleep(1)

for i in range(50):
    
    card.cmd("tickGet") 
    time.sleep(1)

    card.cmd("stopPolling")
    card.cmd("repeat(250000,adpt_defect_trigger,0x1f4,0x1f)")
    time.sleep(2 * random.random())
    card_warm_reboot(card)


