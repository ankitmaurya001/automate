#!/usr/bin/env python

#from __future__ import print_function
import telnetlib;
#from collections import defaultdict
#import time
scpiPort = "5001"
timeout = 5
#HOST = "10.64.106.50";
#child = telnetLib.Telnet(HOST);
class Jdsu:
    """JDSU specific implementation of scpi"""

    layer2scpi = {
            b"phys" :   [b":phys:line:cst:alar?"],
            b"pcs"  :   [":pcs:cst:alar?",b":pcs:cst:err?",b":pcs:rs:cst:alar?",b":pcs:rs:cst:err?"] ,
            b"mac"  :   [b":mac:cst:err?",b":mac:payl:cst:alar:qos?",b":mac:payl:cst:err:qos?",
                b":mac:payl:cst:alar:bert?",b":mac:payl:cst:alar:bert?",b":mac:payl:cst:err:bert?"],
            }

       
    def __init__(self , ip , slot = None ,port = None):
        self.ip = ip
        self.slot = slot
        self.port = port
#        self.connection = telnetlib.Telnet(self.ip,self.scpiPort)
#        self.getPortIps()
        self.timeout = timeout
        self.scpiPort = scpiPort
        if slot and port: 
            portIps = self.getPortIps(ip,scpiPort)
            if (slot,port) in portIps:
#                print ("telnet Port for slot,port= {}".format(portIps[(int(slot),int(port))]))
                self.scpiPort = portIps[(slot,port)]
        else:
            print("no specific port Selected, Connection will be made to equipment")
        self.connection = telnetlib.Telnet(self.ip,self.scpiPort)
#        self.connection.set_debuglevel(15)

#    def __del__(self):
#        if(self.hasattr(connection)):
#           self.connection.close() 

    @staticmethod
    def getPortIps(ip,myScpiPort=scpiPort):
        """ Get the Ports avalable and their telnet PortNumbers"""
#        print "connection made to "+ ip
        n  = telnetlib.Telnet(ip,myScpiPort)
#        n.write(b"*IDN?\r")
#        print(n.read_until(b"\n").rstrip())

        n.write(b":PRTM:LIST?\r")
        s = n.read_until(b"\n").rstrip()
        n.close()

        testsetports = s.split(b',')
        portIps = {}
#        portIps = defaultdict(dict)
        for testsetport in testsetports:
            (slotPort,ipPort,dummy,protect) = testsetport.split(b':')
            (d,chassis,slot,tsPort) = slotPort.split(b'/')
            portIps[(int(slot),int(tsPort))] = int(ipPort)
#            portIps[slot][tsPort] = ipPort
        return portIps

    def query(self, cmd ):
        """ query an scpi command Timeout automatically happens at 10s if not set other wise"""
        self.connection.write(cmd)
        self.connection.write(b"\r\n")
#        time.sleep(2) 
        return self.connection.read_until(b"\n",self.timeout).rstrip()
#        return self.connection.read_eager()
    
    def getAlarm(self,cmd):
        """ Query alarm satus by alarm command it return 1,x where x is alarm status"""
        s = self.query(cmd)
        (ret,val) = s.split(b',')
#        print( cmd,s, ret ,val)
        return val

    def isLayerUp(self,layer,verbose = False):
        layerUp = True
        if layer in self.layer2scpi:
            for cmd in self.layer2scpi[layer]:
                if not (int(self.getAlarm(cmd))==0):
                    layerUp = False
#                    break
                    pass
        if(verbose):
            print( layer , layerUp)
        return layerUp

    def isTrafficUp(self,verbose = False):
        """check all the layer alarms before saying traffic up"""
        trafficUp = True
        for layer in self.layer2scpi:
            if not  self.isLayerUp(layer,verbose) :
                trafficUp = False
#                break
        return trafficUp

    def isLayerHit(self,layer,verbose = False):
        layerHit = False
        if layer in self.layer2scpi:
            for cmd in self.layer2scpi[layer]:
                hstcmd = cmd.replace('cst','hst')
                if not (int(self.getAlarm(hstcmd))==0):
                    layerHit = True
#                    break
                    pass
        if(verbose):
            print( layer , layerHit)
        return layerHit

    def isTrafficHit(self,verbose = False):
        """check all the layer alarms before saying traffic up"""
        trafficHit = False
        for layer in self.layer2scpi:
            if self.isLayerHit(layer,verbose) :
                trafficHit = True
        return trafficHit


    def whichApp(self):
       return self.query(':INST:CAT?')

    def unloadApp(self):
       current = self.whichApp()
       timeout = self.timeout
       self.timeout = 120
       s = self.query(':INST:DEL ' + current + ' ;*OPC? \r\n')
       self.timeout = timeout
       return s
    
    def restartMeasurement(self):
       timeout = self.timeout
       self.timeout = 120
       s = self.query(':ABOR;*WAI;:INIT:IMM:ALL;*OPC?' )
       self.timeout = timeout
       return s 

    def interact(self):
        self.connection.interact()
    
    def loadableApps(self):
        return self.query(':INST:LOAD? "public"')
    
    def load10GE(self):
       timeout = self.timeout
       self.timeout = 120
       #load 10GE application From public 
       #'*OPC?' is added to block till application load
       self.query(':INST:LOAD "10GE","public";' + '*OPC?')
       # Start Traffic on 10GE
       self.query(':SOUR:DATA:TEL:MAC:TRAF:STAT ON;'+ '*OPC?')
       self.timeout = timeout

if __name__ == "__main__":
    """ Called from python module if called other than import"""
#    execfile("../myCfg/myCfg.py")
    host = "10.64.109.230"
    slot = 1 
    port = 1

#    import myCfg
#    c = myCfg.myCfg()
#    host = c.get("testset","ip")
#    slot = c.get("testset","slot")
#    port = c.get("testset","port")

    import sys
#    print sys.argv
#    print len(sys.argv)
   
    if(len(sys.argv) == 2):
        host = sys.argv[1]
        print Jdsu.getPortIps(host)
        quit()
    elif(len(sys.argv) == 4):
        (progname, host,slot,port) = sys.argv
    else:
        print("Defaulting to "+repr(host) + " slot "+repr(slot) +" port "+repr(port))
  
# convert incoming argument to integers
    slot = int(slot)
    port = int(port)
    print("Running at "+repr(host) + " slot "+ repr(slot) +" port "+repr(port))
    

    j = Jdsu(host,slot, port)
    print("Current loaded application =" + j.whichApp())
#    print("Equipment : " + j.query(b"*IDN?").decode('utf-8'))
    print "Traffic for Jdsu " + repr(j.ip)+ "  slot "+ repr(j.slot)+ "  port "+ repr(j.port) + " is " +repr(j.isTrafficUp(True))
    print repr(j.isTrafficHit(True))
#    print j.getPortIps(host)