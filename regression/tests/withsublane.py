import telnetlib
import time
import  re


def sendTL1(tn,cmd):
    tn.write(cmd)
    op=(tn.read_until(b"> "))
    print(op)
    time.sleep(5)
    return op

def connectTL1(ip,passwd='otbu+1'):
    tn = telnetlib.Telnet(ip,3083)
    print(tn.read_until(b"> "))
    tn.write(b"ACT-USER::CISCO15:A::otbu+1;")
    print(tn.read_until(b"> "))
    sendTL1(tn, b"set-attr-secudflt:::1::tmout=0,privlvl=super;")
    sendTL1(tn, b"alw-msg-dbchg:::1;")
    return tn

def clientparametermodify (tn,shelf,lcslot,clientports,lanes):
    for clientPort in clientports:
        for lane in lanes:
            sendTL1(tn, b'ed-10gige::vline-%d-%d-%d-1-%d:c:::mtu=9700;' % (shelf,lcslot, clientPort,lane))


def trunkparametermodify(tn,shelf,lcslot, trunkports):
    for trunkPort in trunkports:
        sendTL1(tn,b'ed-otu4c2::vfac-%d-%d-%d-1:c:::fec=sd-25-de-off,lossb=dwdm,freq=1561.83;' % (shelf,lcslot, trunkPort))

def clientis(tn,shelf,lcslot, clientports,lanes):
    for clientPort in clientports:
        for lane in lanes:
            sendTL1(tn,b'ed-10gige::vline-%d-%d-%d-1-%d:c::::unlocked;' % (shelf,lcslot, clientPort,lane))


def trunkis(tn,shelf,lcslot, trunkports):
    for trunkPort in trunkports:
        sendTL1(tn,b'ed-otu4c2::vfac-%d-%d-%d-1:c::::unlocked;' % (shelf,lcslot, trunkPort))



def clientoos(tn,shelf,lcslot, clientports,lanes):
    for clientPort in clientports:
        for lane in lanes:
            sendTL1(tn,b'ed-10gige::vline-%d-%d-%d-1-%d:c:::cmdmde=frcd:locked,disabled;' % (shelf,lcslot, clientPort,lane))



def trunkoos(tn,shelf,lcslot, trunkports):
    for trunkPort in trunkports:
        sendTL1(tn,b'ed-otu4c2::vfac-%d-%d-%d-1:c:::cmdmde=frcd:locked,disabled;' % (shelf,lcslot, trunkPort))

def clientdelete(tn,shelf,lcslot,clientports,lanes):
    for clientPort in clientports:
        for lane in lanes:
            sendTL1(tn,b'dlt-10gige::vline-%d-%d-%d-1-%d:c;' %(shelf,lcslot,clientPort,lane))

def cardprov(tn,shelf,lcslot):
    sendTL1(tn, b'ent-eqpt::slot-%d-%d:c::400g-xp-lc;' %(shelf,lcslot))

def ppmprovclient(tn,shelf,lcslot,clientports):
    for clientPort in clientports:
        sendTL1(tn, b'ent-eqpt::appm-%d-%d-%d:c::ppm-1;' % (shelf, lcslot, clientPort))

def ppmprovtrunk(tn,shelf,lcSlot,trunkports):
    for trunkPort in trunkports:
        sendTL1(tn, b'ent-eqpt::ppm-%d-%d-%d:c::ppm-1;' % (shelf, lcSlot, trunkPort))
def opmodedelete(tn,shelf,lcslot):
    sendTL1(tn, b'dlt-opmode::slot-%d-%d:c:::opmode=mxp;' %(shelf,lcslot))

def clientcreate(tn,shelf,lcslot,clientports,lanes):
    for clientPort in clientports:
        for lane in lanes:
            sendTL1(tn,b'ent-10gige::vline-%d-%d-%d-1-%d:c;' %(shelf,lcslot,clientPort,lane))


def cardwarmreset(tn,shelf,lcslot):
    sendTL1(tn,b'init-sys::slot-%d-%d:c;'%(shelf,lcslot))
    #time.sleep(200)
    time.sleep(300)
def opmodecreate(tn,shelf,lcslot):
    sendTL1(tn,b'ent-opmode::slot-%d-%d:c:::opmode=mxp,trunkopmode=11/m-200g&12/m-200g,clientsets=11/s1/opm-10x10g&11/s2/opm-10x10g&12/s3/opm-10x10g&12/s4/opm-10x10g;' %(shelf,lcslot))

tn=connectTL1("10.64.105.29")
shelfId=50
lcSlot=5
clientPorts = [1,2,3,4,5,7,8,9,10]
subLanes=[1,2,3,4]
lanes=[1,3,4]
clientjdsu=[6]
trunkPorts = [11,12]
iterationcount=2
i=0
'''
cardprov(tn,shelfId,lcSlot)
time.sleep(30)
ppmprovtrunk(tn,shelfId,lcSlot,trunkPorts)
time.sleep(30)
ppmprovclient(tn,shelfId,lcSlot,clientPorts)
time.sleep(30)
opmodecreate(tn,shelfId,lcSlot)
time.sleep(30)
clientcreate(tn,shelfId,lcSlot,clientPorts)
time.sleep(60)
op = sendTL1(tn, b'rtrv-cond-all:::1;')
clientparametermodify(tn, shelfId, lcSlot, clientPorts)
time.sleep(60)
op = sendTL1(tn, b'rtrv-cond-all:::1;')
trunkparametermodify(tn,shelfId,lcSlot,trunkPorts)
time.sleep(60)
op = sendTL1(tn, b'rtrv-cond-all:::1;')
clientis(tn,shelfId, lcSlot, clientPorts)
time.sleep(60)
op = sendTL1(tn, b'rtrv-cond-all:::1;')
trunkis(tn,shelfId, lcSlot, trunkPorts)
time.sleep(60)
op = sendTL1(tn, b'rtrv-cond-all:::1;')
'''

while i < 20:
    clientoos(tn,shelfId,lcSlot,clientPorts,subLanes)
    clientoos(tn,shelfId,lcSlot,clientjdsu,lanes)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    time.sleep(120)
    cardwarmreset(tn,shelfId, lcSlot)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    trunkoos(tn,shelfId,lcSlot,trunkPorts)
    time.sleep(120)
    cardwarmreset(tn,shelfId, lcSlot)
    clientdelete(tn,shelfId,lcSlot,clientPorts,subLanes)
    clientdelete(tn,shelfId,lcSlot,clientjdsu,lanes)
    time.sleep(120)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    opmodedelete(tn,shelfId,lcSlot)
    time.sleep(120)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    cardwarmreset(tn, shelfId, lcSlot)
    opmodecreate(tn,shelfId,lcSlot)
    time.sleep(60)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    trunkparametermodify(tn,shelfId,lcSlot,trunkPorts)
    time.sleep(30)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    cardwarmreset(tn, shelfId, lcSlot)
    clientcreate(tn, shelfId, lcSlot, clientPorts,subLanes)
    clientcreate(tn,shelfId,lcSlot,clientjdsu,lanes)
    time.sleep(120)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    cardwarmreset(tn,shelfId,lcSlot)
    clientparametermodify(tn, shelfId, lcSlot, clientPorts,subLanes)
    clientparametermodify(tn,shelfId,lcSlot,clientjdsu,lanes)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    time.sleep(30)
    cardwarmreset(tn,shelfId, lcSlot)
    clientis(tn,shelfId, lcSlot, clientPorts,subLanes)
    clientis(tn,shelfId,lcSlot,clientjdsu,lanes)
    time.sleep(120)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    cardwarmreset(tn,shelfId,lcSlot)
    trunkis(tn,shelfId, lcSlot, trunkPorts)
    time.sleep(60)
    op = sendTL1(tn, b'rtrv-cond-all:::1;')
    cardwarmreset(tn,shelfId, lcSlot)
    op=sendTL1(tn,b'rtrv-cond-all:::1;')
    i=i+1
    print('iteration number = %d' %i)
    time.sleep(60)
