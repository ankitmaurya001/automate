#! /usr/bin/env python

# import functions
from utils.tl1 import Tl1
import itertools
# initialize variables 
shelf = None
#(node,slot)  = ('10.64.106.50',3)
(node,slot)  = ('10.58.226.174',6)
#(shelf,node,slot)  = (1,'10.64.104.228',7)
trunk1Ports = [1,2,3,7,8]
trunk2Ports = [4,5,6,9,10]
portNums = trunk1Ports + trunk2Ports
#subLanes = list(range(1,5))
payload = '10gige'
#payload = 'otu2'
import random
mtu = random.randint(20,97)*100

provision = True
#provision = not provision
provision = False

#override variables
portNums = [1]
subLanes = [1]
#subLanes = list(range(2,5))

ports = []

if shelf is None:
    tl1PortSyntax = 'vline-{slot}-{portNum}-1-{subLane}'
    tl1CardSyntax = 'slot-{slot}'
else:
    tl1PortSyntax = 'vline-{shelf}-{slot}-{portNum}-1-{subLane}'   #multiShelf


card = tl1CardSyntax.format(slot=slot)
for portNum,subLane in itertools.product(portNums,subLanes):
    ports.append(tl1PortSyntax.format(slot=slot,portNum=portNum,subLane=subLane,shelf=shelf))

# Establish Tl1 connection
tl = Tl1(node)


#create opmode
#print tl.cmd('ent-opmode::slot-2:scr3:::opmode=mxp-200g,peerslots=slot-3&slot-4,trunkports=2,peerclients=3-2&&-5&4-2&&-5;')
#define ports
#ports = ['vfac-3-2-1','vfac-3-3-1',
#        'vline-3-2-1-1','vline-3-2-1-2','vline-3-2-1-3','vline-3-2-1-4',
#        'vline-3-3-1-1','vline-3-3-1-2','vline-3-3-1-3','vline-3-3-1-4',
#        ]


#create Ports
tl1provCommand = "ent-{payload}::{port}:scr;"
tl1unprovCommand = "dlt-{payload}::{port}:scr;"
tl1retriveCommand = "rtrv-{payload}::all:scr;"
tl1IsCommand = "ed-{payload}::{port}:scr::::is;"
tl1OosCommand = "ed-{payload}::{port}:scr:::cmdmde=frcd:oos,dsbld;"
tl1MtuCommand = "ed-10gige::{port}:scr:::mtu={mtu};"
tl1EditOpModeCommand = "ed-opmode::{card}:scr:::opmode={cardOpmode},clientsets=11/S1/{trunkOpmode},action=slice-mode"


def change_mtu(mtu):
    [tl.cmd(tl1OosCommand.format(payload=payload,port=port)) for port in ports]
    print [tl.cmd(tl1MtuCommand.format(port=port, mtu=mtu)) for port in ports]
    [tl.cmd(tl1IsCommand.format(payload=payload,port=port)) for port in ports]

#if(provision):
#    res = [tl.cmd(tl1provCommand.format(payload=payload,port=port)) for port in ports]
#    #print ''.join(res)
#    #print res
#    change_mtu(mtu) 
#    #make ports IS
#    res = [tl.cmd(tl1IsCommand.format(payload=payload,port=port)) for port in ports]
#
#else:
##if(deprovision) :
#    #make ports oos
#    print [tl.cmd(tl1OosCommand.format(payload=payload,port=port)) for port in ports]
#    
#    #delete ports
#    print [tl.cmd(tl1unprovCommand.format(payload=payload,port=port)) for port in ports]
#
#
#print tl.cmd(tl1EditOpModeCommand.format(card=card,cardOpmode="MXP",trunkOpmode="OPM-100G",))
##print tl.cmd(tl1EditOpModeCommand.format(card=card,cardOpmode="MXP",trunkOpmode="OPM-10x10G",))


print "\n  All {} payloads on the node \n".format(payload)
print tl.cmd(tl1retriveCommand.format(payload=payload))
print tl.cmd("rtrv-opmode::all:scr;")
print tl.cmd("rtrv-pm-100gige::all:scr;")


#make channels to IS
#print [tl.cmd('ed-och::'+channel+':scr::::is;') for channel in channels]



