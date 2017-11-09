#! /usr/bin/env python

from utils.tl1 import Tl1



# initialize variables 
node  = '10.64.106.50'

# Establish Tl1 connection
tl = Tl1(node)

#create opmode
#tl.cmd('ent-opmode::slot-2:$:::opmode=mxp-ck-100g,peerslots=slot-3,trunkports=2,peerclients=3-1;')
#define ports
port = 'aggr-6-1-1'


def test_100GE_is():
    print tl.cmd('ed-100gige::'+port+':scr::::is;') 
    print tl.cmd('ed-100gige::'+port+':scr:::cmdmde=frcd:oos,dsbld;') 

