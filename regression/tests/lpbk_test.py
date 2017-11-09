#! /usr/bin/env python

import os
import sys
import time

if os.path.realpath('/ws/marigcha-bgl/regression/utils/') not in sys.path:
    sys.path.append(os.path.realpath('/ws/marigcha-bgl/regression/utils/')) # put dir containing this file in path

import jdsu
import vxConsole
import tl1
# initialize variables 

(node,cardslot,portid)  = ('10.64.106.50',4,'4-2-1')
(cardConsoleIp,cardConsolePort,portid)  = ('10.64.108.116',2050,'4-2-1')
(jdsuip,jdsuslot,jdsuport) = ('10.64.109.230',2,4)

tl1Delay = 20

tnc = vxConsole.vxConsole(node,23)

#card = vxConsole.vxConsole(node, '200' + str(cardslot) )
card = vxConsole.vxConsole(cardConsoleIp, cardConsolePort,console = True) 
testset = jdsu.Jdsu(jdsuip , jdsuslot , jdsuport)
tl = tl1.Tl1(node) 

card.t.logfile = open('/tmp/cardLog','w')
print tnc.cmd('flmStat')


#print repr(testset.isTrafficUp())
assert (not testset.isTrafficUp()) ," Traffic is up with out Loopback!!!" 


print(" Traffic up test starting")
print card.cmd('mManufDisplay')
print 'configured payloads :'
print tl.cmd("rtrv-10gige::all:scr;")

#apply loopback from the Tl1
#print tl.cmd('ed-och::chan-'+portid+':scr::::oos,mt;')
#print tl.cmd('opr-lpbk-och::chan-' + portid + ':scr::,,,facility;')
tl.setFacLpbk(portid)

assert testset.isTrafficUp(), "Traffic is not up after Loopback"
#delay
#for i in range(10):
#    print "sleeping in "+repr(i) + "iteration for "+ repr(tl1Delay) +"seconds"
#    time.sleep(tl1Delay)
#    if testset.isTrafficUp():
#        break
#else:
## check sanity
#    if not testset.isTrafficUp():
#        print("please make sure traffic up before the soft reboot with loopback")
#        quit()

#remove loopback 
#print tl.cmd('rls-lpbk-och::chan-' + portid + ':scr::,,,facility;')
#print tl.cmd('ed-och::chan-'+portid+':scr::::is;')
tl.releaseFacLpbk(portid)

assert not testset.isTrafficUp(), "Traffic is not up after Reboot"

#for i in xrange(10):
#    print "sleeping in " + repr(i) + "iteration for "+ repr(tl1Delay) +"seconds"
#    time.sleep(tl1Delay)
#    if not testset.isTrafficUp():
#        break
#else:
## check sanity
#    if testset.isTrafficUp():
#        print("loopback removal failed")
#        quit()

#apply loopback from the Tl1
print "============>apply loopback from the Tl1"
#print tl.cmd('ed-och::chan-'+portid+':scr::::oos,mt;')
#print tl.cmd('opr-lpbk-och::chan-' + portid + ':scr::,,,facility;')
tl.setFacLpbk(portid)

#delay
#for i in xrange(10):
#    print "sleeping in "+repr(i) + "iteration for "+ repr(tl1Delay) +"seconds"
#    time.sleep(tl1Delay)
#    if testset.isTrafficUp():
#        break
#else:
## check sanity
#    if not testset.isTrafficUp():
#        print("please make sure traffic up before the soft reboot with loopback")
#        quit()

print "==========> rebooting line card"
card.cmd('tickGet')
card.sendline('reboot')
card.t.expect_exact('disable Linetiming',timeout = None)
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print " reboot done"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

print card.cmd('tickGet')
print "========> Checking Traffic"

assert testset.isTrafficUp(), "Traffic is not up after Reboot"
assert testset.isTrafficHit(), "Traffic is not up after Reboot"
time.sleep(10)

tl.releaseFacLpbk(portid)
time.sleep(10)
assert not testset.isTrafficUp(), "Traffic is up after removing loopback"

tl.setFacLpbk(portid)
time.sleep(10)
assert testset.isTrafficUp(), "Traffic is not up after applying loopback"

#Cold Rebooting Card
#Cold reboot card
card.cmd('tickGet')
card.sendline('reboot 2')
card.t.expect_exact('disable Linetiming',timeout = None)
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "cold reboot done"
print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

print card.cmd('tickGet')
time.sleep(10)
assert testset.isTrafficUp(), "Traffic is not up after cold rebooting card"

tl.releaseFacLpbk(portid)
time.sleep(10)
assert not testset.isTrafficUp(), "Traffic is up after removing loopback"



