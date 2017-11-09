#! /usr/bin/env python


from utils.tl1 import Tl1
# initialize variables 


node  = '10.64.106.140'


# Establish Tl1 connection
tl = Tl1(node)
#create opmode
print tl.cmd('ent-opmode::slot-2:scr3:::opmode=mxp-200g,peerslots=slot-3&slot-4,trunkports=2,peerclients=3-2&&-5&4-2&&-5;')
#define ports
ports = ['vfac-3-2-1','vfac-3-3-1',
        'vline-3-2-1-1','vline-3-2-1-2','vline-3-2-1-3','vline-3-2-1-4',
        'vline-3-3-1-1','vline-3-3-1-2','vline-3-3-1-3','vline-3-3-1-4',
        ]

#create Ports
print [tl.provision10GIGE(port) for port in ports]

#delete ports
#print [tl.remove10GIGE(port) for port in ports]

print tl.cmd("rtrv-10gige::all:scr;")
#make ports IS
#[tl.cmd('ed-10gige::'+port+':scr::::is;') for port in ports]


#define channels
channels =[   
        'CHAN-2-2',
        'CHAN-3-2-1',
        'CHAN-3-3-1',
        'VCHAN-3-2-1-1',
        'VCHAN-3-2-1-2',
        'VCHAN-3-2-1-3',
        'VCHAN-3-2-1-4',
        'VCHAN-3-3-1-1',
        'VCHAN-3-3-1-2',
        'VCHAN-3-3-1-3',
        'VCHAN-3-3-1-4',
        ]


#make channels to IS
#print [tl.cmd('ed-och::'+channel+':scr::::is;') for channel in channels]




