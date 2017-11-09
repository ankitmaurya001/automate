#! /usr/bin/env python
# test case only works if something is configured on card as "disable linetiming" only comes when card is configured
import os
import sys
import time
import itertools
from colorama import init,Fore,Back,Style
init(autoreset=True)

if os.path.realpath('/ws/marigcha-bgl/regression/utils/') not in sys.path:
    sys.path.append(os.path.realpath('/ws/marigcha-bgl/regression/utils/')) # put dir containing this file in path

import vxConsole

(cardConsoleIp,cardConsolePort,portid)  = ('10.64.108.116',2048,'4-2-1')

#########################################
provisionAllPorts = ""
deleteChannels_slice = "diagDigiT5_del_channels_slice {asic},{digislice}"
Digi_SliceTemplate_MXP_C_10x10G_L_4x25G_OTU4_GFEC = 4
digiInit_mxp = "diagDigiInit_mxp({asicNum}, {initType},{slice0TemplateID},{slice0},{slice1TemplateID},{slice1})"
Digi_ChTemplate_10GE_CBR_10G3_7_1_BMP = 4
digi_prov_qsfp ="diagDigiT5_config_qsfp_4x10GE {port}" 
trunk1Ports = [1,2,3,7,8]
trunk2Ports = [4,5,6,9,10]
trunk1Slices = [1,2]
trunk2Slices = [3,4]
#digiDevId = ['0x1f6','0x000101f7']
digiDevId = ['0x1f4','0x000101f5']
digis = [0,1]
#############################################
nonfactoryModeRebootComplete = "Process Provisioning End !"
factoryModeRebootComplete = "Init process terminated"

rebootComplete = nonfactoryModeRebootComplete 

############################################
ports = trunk1Ports + trunk2Ports
payload = Digi_ChTemplate_10GE_CBR_10G3_7_1_BMP
trunk1Params = {'asicNum':'0' , 'slice0TemplateID' : Digi_ChTemplate_10GE_CBR_10G3_7_1_BMP,
        'slice1TemplateID' :Digi_ChTemplate_10GE_CBR_10G3_7_1_BMP,
        'slice0' : 'SLICE1()', 'slice1' : 'SLICE2()', 'initType' : '0'}
trunk2Params = {'asicNum':'1' , 'slice0TemplateID' : Digi_ChTemplate_10GE_CBR_10G3_7_1_BMP,
        'slice1TemplateID' :Digi_ChTemplate_10GE_CBR_10G3_7_1_BMP,
        'slice0' : 'SLICE3()', 'slice1' : 'SLICE4()', 'initType' : '0'}


saveContext = "adpt_warm_restart_handle {digiId}"
provision = True
firstTime = True
#########################################
card = vxConsole.vxConsole(cardConsoleIp, cardConsolePort,console = True ) 
card.t.logfile = sys.stdout
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

card_cold_reboot(card)
card.cmd('eqaStat')

print(Fore.CYAN +"=" *10 + "> Configure trunk 0" )
#print("=" *10 + "> Configure trunk 0" )
card.cmd(digiInit_mxp.format(**trunk1Params))
time.sleep(1)
print(Fore.CYAN +"=" *10 + "> Configure trunk 1" )
card.cmd(digiInit_mxp.format(**trunk2Params))

trunk1Params.update({'initType':'2'})
trunk2Params.update({'initType':'2'})

for i in range(50):
    print(Fore.GREEN +"=" *10 + ">   Iteration " +repr(i/2) )
    
    if(provision):
        print("\n\n\ndoing Provision of payloads")
        for port in ports:
            print(Back.CYAN + "-"*50)
            time.sleep(1)
            card.cmd(digi_prov_qsfp.format(payload=payload,port=(port-1)))
            time.sleep(5)
        #print ''.join(res)
        #print res
        #change_mtu(mtu) 
        #make ports IS
       # print ([tl.cmd(tl1IsCommand.format(payload=payload,port=port)) for port in ports])
    
    else:
    #if(deprovision) :
        #make ports oos
        print("\n\n\ndoing unProvision of payloads")
       
      #  print [card.cmd(deleteChannels_slice.format(asic = asic ,digislice = digislice)) for digislice in [0,1] for asic in digis]
        for asic in digis:
            for digislice in [0,1]:
                print(Fore.RED + "-"* 10 + "> deleting channels on {asic},{digislice}".format(asic = asic ,digislice = digislice))
                card.cmd(deleteChannels_slice.format(asic = asic ,digislice = digislice))
                time.sleep(5)

    provision = not provision
    
    for asic in digis:
        print(Back.CYAN + "-"*50)
        time.sleep(1)
        card.cmd(saveContext.format(digiId = digiDevId[asic]))
    card.cmd("tickGet") 
    time.sleep(10)
    card_warm_reboot(card)
    card.cmd('eqaStat')
    print(Back.CYAN + "-"*50)
    time.sleep(1)
    card.cmd(digiInit_mxp.format(**trunk1Params))
    print(Back.CYAN + "-"*50)
    time.sleep(1)
    card.cmd(digiInit_mxp.format(**trunk2Params))
    print(Back.CYAN + "-"*50)
    time.sleep(1)


