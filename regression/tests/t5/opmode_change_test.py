#! /usr/bin/env python

# import functions
from utils.tl1 import Tl1
from utils.jdsu import Jdsu
from utils.vxPython import vxConsole
from time import sleep

# initialize variables 
node  = '10.64.106.140'

(jdsuip,jdsuslot,jdsuport) = ('10.64.109.230',2,1)
(jdsuip3,jdsuslot3,jdsuport3) = ('10.64.109.230',2,2)
(jdsuip2,jdsuslot2,jdsuport2) = ('10.64.109.65',3,1)
(trunkSlot,pairSlot,skipSlot) = ('2','3','4')


#define ports
ports = [
    'vfac-'+skipSlot +'-2-1'
    'vfac-'+skipSlot +'-3-1'
    'vline-'+skipSlot +'-2-1-1'
    'vline-'+skipSlot +'-2-1-2'
    'vline-'+skipSlot +'-2-1-3'
    'vline-'+skipSlot +'-2-1-4'
    'vline-'+skipSlot +'-3-1-1'
    'vline-'+skipSlot +'-3-1-2'
    'vline-'+skipSlot +'-3-1-3'
    'vline-'+skipSlot +'-3-1-4'
    ]
channels =[ 'CHAN-'+trunkSlot +'-2','CHAN-'+skipSlot +'-2-1',  ]  

print ports


testsetPeer = Jdsu(jdsuip,jdsuslot,jdsuport)
testsetSkip = Jdsu(jdsuip3,jdsuslot3,jdsuport3)
testset100 = Jdsu(jdsuip2,jdsuslot2,jdsuport2)

# Establish Tl1 connection
tl = Tl1(node)

#print card.cmd("eqaStat")

def create_200g_ports():
    #create falco Card
    print tl.cmd('ent-eqpt::slot-'+pairSlot +':scr::mr-mxp')
    sleep(5) 
    #create opmode
    print tl.cmd('ent-opmode::slot-'+trunkSlot +':scr3:::opmode=mxp-200g,peerslots=slot-'+skipSlot +'&slot-'+pairSlot +',trunkports=2,peerclients='+skipSlot +'-2&&-5&'+pairSlot +'-2&&-5;')
    sleep(5)
    #create Ports
    print [tl.provision10GIGE(port) for port in ports]
    
    #make ports IS
    #print [tl.cmd('ed-10gige::'+port+':scr::::is;') for port in ports]
    print [tl.cmd('ed-och::'+channel+':scr::::is;') for channel in channels]
    
    #check traffic
def create_10x10_100g_ports():
    #create falco Card
    print tl.cmd('ent-eqpt::slot-'+pairSlot +':scr::10x10g-lc')
    sleep(5) 
    #create opmode
    print tl.cmd('ent-opmode::slot-'+trunkSlot +':scr3:::opmode=mxp-10x10g-100g,peerslots=slot-'+skipSlot +'&slot-'+pairSlot +',trunkports=2,peerclients='+skipSlot +'-2&&-5&'+pairSlot +'-1&&-10;')
    sleep(5)
    #create Ports
    print [tl.provision10GIGE(port) for port in ports]
    
    #make ports IS
    #print [tl.cmd('ed-10gige::'+port+':scr::::is;') for port in ports]
    print [tl.cmd('ed-och::'+channel+':scr::::is;') for channel in channels]
 
def delete_200g_ports():
    #make ports oos
    #print [tl.cmd('ed-10gige::'+port+':scr:::cmdmde=frcd:oos,dsbld;') for port in ports]
    print [tl.cmd('ed-och::'+channel+':scr:::cmdmde=frcd:oos,dsbld') for channel in channels]
    sleep(5) 
    #delete ports
    print [tl.remove10GIGE(port) for port in ports]
    sleep(5)
    #delete Opmode
    print tl.cmd('dlt-opmode::slot-'+trunkSlot +':scr:::opmode=mxp-200g;')
    sleep(5)
    #delete Card
    print tl.cmd('dlt-eqpt::slot-'+pairSlot +':scr;')
       
def delete_10x10g_100g_ports():
    #make ports oos
    #print [tl.cmd('ed-10gige::'+port+':scr:::cmdmde=frcd:oos,dsbld;') for port in ports]
    print [tl.cmd('ed-och::'+channel+':scr:::cmdmde=frcd:oos,dsbld') for channel in channels]
    sleep(5) 
    #delete ports
    print [tl.remove10GIGE(port) for port in ports]
    sleep(5)
    #delete Opmode
    print tl.cmd('dlt-opmode::slot-'+trunkSlot +':scr:::opmode=mxp-10x10g-100g;')
    sleep(5)
    #delete Card
    print tl.cmd('dlt-eqpt::slot-'+pairSlot +':scr;')


def delete_100ge_ports():
    print [tl.cmd('ed-och::'+channel+':scr:::cmdmde=frcd:oos,dsbld') for channel in channels]
    print tl.cmd("ED-100GIGE::AGGR-3-1-1:21:::CMDMDE=FRCD:OOS,DSBLD;")
    print tl.cmd("ED-100GIGE::AGGR-2-1-1:22:::CMDMDE=FRCD:OOS,DSBLD;")
    print tl.cmd("DLT-100GIGE::AGGR-3-1-1:23;")
    print tl.cmd("DLT-100GIGE::AGGR-2-1-1:24;")
    print tl.cmd('dlt-opmode::slot-'+trunkSlot +':scr:::opmode=mxp-ck-100g;')

def create_100ge_ports():
    print tl.cmd('ent-eqpt::slot-'+pairSlot +':scr::mr-mxp')
    print tl.cmd('ent-opmode::slot-2:scr:::opmode=mxp-ck-100g,peerslots=slot-3,trunkports=2,clientports=1,peerclients=3-1;')
    sleep(5)
    print tl.cmd("ENT-100GIGE::AGGR-3-1-1:25:::NUMOFLANES=4;")
    print tl.cmd("ENT-100GIGE::AGGR-2-1-1:26:::NUMOFLANES=4;")
    print tl.cmd("ED-100GIGE::AGGR-3-1-1:27::::IS;")
    print tl.cmd("ED-100GIGE::AGGR-2-1-1:28::::IS;")
    print [tl.cmd('ed-och::'+channel+':scr::::is;') for channel in channels]


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


#create_200g_ports()
#sleep(300)
delete_200g_ports()
#sleep(30)
#create_10x10_100g_ports()
#sleep(300)
delete_10x10g_100g_ports()
#sleep(30)
#create_200g_ports()
create_100ge_ports()   

#delete_100ge_ports()
#assert 0
#sleep(10)
iteration = 1
while (1):
#    print 20*"#" +  "      changing to Falco + Falco mode Iteration "+repr(iteration) + 5*" "+ 20*"#"
    #create 200g opmode
    create_200g_ports()
    if(iteration %30 == 0):
        print 20*"!" + " Cold rebooting the card" + 20 * "!"
        card = vxConsole(node, '200' + skipSlot)
        card.sendline("reboot 2")
        sleep(120)
       

    #check traffic
    check_tarffic(testsetSkip, maxWait = 60, waitGrooming = 10 , stabilizeCount = 3)
    check_tarffic(testsetPeer, maxWait = 60, waitGrooming = 10 , stabilizeCount = 3)
    delete_200g_ports()
    sleep(10)
    #create 10x10-100g opmode
 #   print 20*"#" +  "      changing to Falco + Carpegna mode  Iteration "+repr(iteration)+ 5*" " + 20*"#"
  #  create_10x10_100g_ports()
  #  check_tarffic(testset, maxWait = 60, waitGrooming = 10 , stabilizeCount = 3)
  #  delete_10x10g_100g_ports()
    #create 100GE opmode
    print 20*"#" +  "      changing to Falco 100GE mode  Iteration "+repr(iteration)+ 5*" " + 20*"#"
    create_100ge_ports()   
    if(iteration %30 == 0):
        print 20*"!" + " Cold rebooting the card" + 20 * "!"
        card = vxConsole(node, '200' + skipSlot)
        card.sendline("reboot 2")
        sleep(120)
 
    check_tarffic(testset100, maxWait = 60, waitGrooming = 10 , stabilizeCount = 3)
    delete_100ge_ports()
    sleep(10)
    #iteration Completed
    iteration = iteration +1
#print tl.cmd('rtrv-eqpt::slot-6:scr')
#print tl.cmd("rtrv-10gige::all:scr;")

