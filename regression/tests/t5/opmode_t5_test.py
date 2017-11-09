#! /usr/bin/env python

# import functions
from utils.tl1 import Tl1
import itertools
from utils.jdsu import Jdsu
from utils.vxConsole import vxConsole
import sys

# initialize variables 
shelf = None
#(node,slot)  = ('10.64.106.50',3)
(node,slot)  = ('10.58.226.174',6)
(shelf,node,slot)  = (1,'10.64.104.228',5)
trunk1Ports = [1,2,3,7,8]
trunk2Ports = [4,5,6,9,10]
portNums = trunk1Ports + trunk2Ports
#subLanes = list(range(1,5))
tengLevel = ['10gige','otu2']

payload = '10gige'
#payload = 'otu2'
#import random
#mtu = random.randint(20,97)*100

#override variables
#portNums = [1,2]
#subLanes = [1,2]
#subLanes = list(range(2,5))

(ip,port,isConsole) = ('fwts7',2039,True)
#card = vxConsole(ip,port)
##card = vxConsole(node,2000+slot,timeout=100)
#card.logfile(open("/ws/marigcha-bgl/log","w"))
#
#print card.cmd('eqaStat')
ports = []

if shelf is None:
    tl1VlineSyntax = 'vline-{slot}-{portNum}-1-{subLane}'
    tl1CardSyntax = 'slot-{slot}'
    tl1AggrSyntax = 'aggr-{slot}-{portNum}-1'
else:
    tl1PortSyntax = 'vline-{shelf}-{slot}-{portNum}-1-{subLane}'   #multiShelf

def populate_ports_array(ports,portNums,subLanes):
    if len(subLanes) > 0 :
        for portNum,subLane in itertools.product(portNums,subLanes):
            ports.append(tl1VlineSyntax.format(slot=slot,portNum=portNum,subLane=subLane,shelf=shelf))
    else:
        for portNum in portNums:
            ports.append(tl1AggrSyntax.format(slot=slot,portNum=portNum))



#create Ports
tl1_10g_provCommand = "ent-{payload}::{port}:scr;"
tl1_100g_provCommand = "ENT-{payload}::{port}:scr:::NUMOFLANES=4;"
tl1unprovCommand = "dlt-{payload}::{port}:scr;"
tl1retriveCommand = "rtrv-{payload}::all:scr;"
tl1IsCommand = "ed-{payload}::{port}:scr::::is;"
tl1OosCommand = "ed-{payload}::{port}:scr:::cmdmde=frcd:oos,dsbld;"
tl1MtuCommand = "ed-10gige::{port}:scr:::mtu={mtu};"
tl1EditOpModeCommand = "ed-opmode::{card}:scr:::opmode={cardOpmode},clientsets=11/S1/{trunkOpmode},action=slice-mode"

tl1card = tl1CardSyntax.format(slot=slot)

def change_mtu(mtu):
    [tl.cmd(tl1OosCommand.format(payload=payload,port=port)) for port in ports]
    print [tl.cmd(tl1MtuCommand.format(port=port, mtu=mtu)) for port in ports]
    [tl.cmd(tl1IsCommand.format(payload=payload,port=port)) for port in ports]

def provision_ports(ports,payload):
    if payload in tengLevel:
        print tl.cmd(tl1EditOpModeCommand.format(card=tl1card,cardOpmode="MXP",trunkOpmode="OPM-10x10G",))
        res = [tl.cmd(tl1_10g_provCommand.format(payload=payload,port=port)) for port in ports]
    else:
        print tl.cmd(tl1EditOpModeCommand.format(card=tl1card,cardOpmode="MXP",trunkOpmode="OPM-100G",))
        res = [tl.cmd(tl1_100g_provCommand.format(payload=payload,port=port)) for port in ports]


    res += [tl.cmd(tl1IsCommand.format(payload=payload,port=port)) for port in ports]
    return res

def unprovision_ports(ports,payload):
    #make ports oos
    res= [tl.cmd(tl1OosCommand.format(payload=payload,port=port)) for port in ports]
    
    #delete ports
    res += [tl.cmd(tl1unprovCommand.format(payload=payload,port=port)) for port in ports]
    
    if payload in tengLevel:
        print tl.cmd(tl1EditOpModeCommand.format(card=tl1card,cardOpmode="MXP",trunkOpmode="OPM-10x10G",))
    else:
        print tl.cmd(tl1EditOpModeCommand.format(card=tl1card,cardOpmode="MXP",trunkOpmode="OPM-100G",))
    
    return res


def cold_reboot_card(card):
    card.sendline("reboot 2")


def warm_reboot_card(card):
    card.sendline("reboot ")
    card.t.expect_exact('TNC path initialized',timeout = None)
    print("card Reboot Done")

def check_tarffic(mTestset, maxWait = 60, waitGrooming = 10 , stabilizeCount = 3):
    tempStabilizeCount = 0
    for i in range(maxWait):
        if(mTestset.isTrafficUp()):
            tempStabilizeCount = tempStabilizeCount +1 
            print "good Traffic up  after " +repr(i*10) +"seconds of create Port"
            if (tempStabilizeCount > stabilizeCount):
                break 
        else:
            tempStabilizeCount = 0
            sleep(waitGrooming)
    else:
        print tl.cmd("rtrv-alm-all::all:scr;")
#        card = vxConsole(node, '200' + repr(skipSlot))
        card = vxConsole(node, '200' + skipSlot)
        print card.cmd("DD 1,0")
        print card.cmd("DD 1,1")
        print card.cmd("adpt_dump_enet_alm 1008,0")
        card.t.close()
        sleep(30)
        if(mTestset.isTrafficUp()):
            print 30 * "&" +"Traffic up after issuing defect Trigger "
        else:
            assert 0,"traffic Down after " +repr(i*10) +"seconds of create Port"




### start the tests ####
from time import sleep
from colorama import init,Fore,Back,Style
init(autoreset=True)
tenGigePorts = []
hundredGigePorts = []
print(Fore.GREEN + "starting tests")
populate_ports_array(tenGigePorts,portNums,subLanes)
populate_ports_array(hundredGigePorts,[7],[])
# Establish Tl1 connection
tl = Tl1(node)

#define the order of the ports
portsList = [tenGigePorts, hundredGigePorts]

#test warmboot
def test_warm_boot(testPortsList):
    pass
#    print(Fore.CYAN + "Provisioning Ports")
#    print provision_ports( tenGigePorts,'10gige')
#    #check traffic up here
#
##    warm_reboot_card(card)
#    sleep(10)
#    print unprovision_ports( tenGigePorts,'10gige')

    #check no hit on traffic
    print provision_ports( hundredGigePorts,'100gige')
#    sleep(10)
#    #check traffic again here
#    print unprovision_ports( hundredGigePorts,'100gige')

#    warm_reboot_card(card)


#print (Fore.RED +Style.BRIGHT + 10*"=" + "cleaning up the ports " + 10*"=")
#print unprovision_ports( hundredGigePorts,'100gige')
#print unprovision_ports( tenGigePorts,'10gige')

#test_warm_boot(portsList)


#print(Fore.CYAN + "Provisioning Ports")
#print provision_ports(ports,payload)


#print(Fore.CYAN + Back.BLACK+ "Un Provisioning Ports")
#print unprovision_ports(ports,payload)


#print tl.cmd(tl1EditOpModeCommand.format(card=card,cardOpmode="MXP",trunkOpmode="OPM-100G",))
#print tl.cmd(tl1EditOpModeCommand.format(card=card,cardOpmode="MXP",trunkOpmode="OPM-10x10G",))


print(Fore.BLUE + 15*"=" + " status " + 15*"=")
print "\n  All {} payloads on the node \n".format(payload)
print tl.cmd(tl1retriveCommand.format(payload=payload))
print tl.cmd(tl1retriveCommand.format(payload='100gige'))
print tl.cmd("rtrv-opmode::all:scr;")

print tl.cmd("rtrv-pm-100gige::all:scr;")

#define channels
#make channels to IS
#print [tl.cmd('ed-och::'+channel+':scr::::is;') for channel in channels]


