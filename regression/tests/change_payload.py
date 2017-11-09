#! /usr/bin/env python

# import functions
from utils.tl1 import Tl1
from time import sleep

# initialize variables 
node  = '10.64.106.50'

shelf = '1'

(jdsuip,jdsuslot,jdsuport) = ('10.64.109.230',2,1)
testset = Jdsu(jdsuip,jdsuslot,jdsuport)

# Establish Tl1 connection
tl = Tl1(node)

if shelf is None:
    tl1PortSyntax = 'vline-{slot}-{portNum}-1-{subLane}'
    tl1CardSyntax = 'slot-{slot}'
else:
    tl1PortSyntax = 'vline-{shelf}-{slot}-{portNum}-1-{subLane}'   #multiShelf


#tl1 commands
tl1provCommand = "ent-{payload}::{port}:scr;"
tl1unprovCommand = "dlt-{payload}::{port}:scr;"
tl1retriveCommand = "rtrv-{payload}::all:scr;"
tl1IsCommand = "ed-{payload}::{port}:scr::::is;"
tl1OosCommand = "ed-{payload}::{port}:scr:::cmdmde=frcd:oos,dsbld;"
tl1MtuCommand = "ed-10gige::{port}:scr:::mtu={mtu};"
tl1EditOpModeCommand = "ed-opmode::{card}:scr:::opmode={cardOpmode},clientsets=11/S1/{trunkOpmode},action=slice-mode"



#create opmode
#print tl.cmd('ent-opmode::slot-2:scr3:::opmode=mxp-200g,peerslots=slot-3&slot-4,trunkports=2,peerclients=3-2&&-5&4-2&&-5;')
#define ports
ports = ['vfac-3-2-1','vfac-3-3-1',
        'vline-3-2-1-1','vline-3-2-1-2','vline-3-2-1-3','vline-3-2-1-4',
        'vline-3-3-1-1','vline-3-3-1-2','vline-3-3-1-3','vline-3-3-1-4',
        ]

nearport = tl1PortSyntax.format(slot=3,portNum=3,subLane=1,shelf=shelf)
farport = tl1PortSyntax.format(slot=6,portNum=3,subLane=1,shelf=shelf)

port = nearport

print tl.cmd(tl1OosCommand.format(payload='oc192',port=port))
sleep(2)
print tl.cmd(tl1unprovCommand.format(payload='oc192',port=port))
sleep(2)
print tl.cmd(tl1provCommand.format(payload='otu2',port=port))
sleep(10)
print tl.cmd(tl1unprovCommand.format(payload='otu2',port=port))
sleep(10)
print tl.cmd(tl1provCommand.format(payload='oc192',port=port))
sleep(2)
print tl.cmd(tl1IsCommand.format(payload='oc192',port=port))


port = farport

print tl.cmd(tl1OosCommand.format(payload='oc192',port=port))
sleep(2)
print tl.cmd(tl1unprovCommand.format(payload='oc192',port=port))
sleep(2)
print tl.cmd(tl1provCommand.format(payload='otu2',port=port))
sleep(10)
print tl.cmd(tl1unprovCommand.format(payload='otu2',port=port))
sleep(10)
print tl.cmd(tl1provCommand.format(payload='oc192',port=port))
sleep(2)
print tl.cmd(tl1IsCommand.format(payload='oc192',port=port))


