#! /usr/bin/env python
#import telnetlib
import fileinput
import telnetlib
import sys
import time
""" Global Variables """
prompt = b'->'
linesep = '\n'

class vxConsole:
    """ Find out why inbuilt telnet module is not working """
    def __init__(self,nodeip,port,console = False):
        self.t = telnetlib.Telnet(nodeip,port)
#        self.t.set_debuglevel(15)
        self.t.read_until(b"Login:")
        self.t.write(b"CISCO15\r")
        self.t.read_until("Password:");
        self.t.write(b"otbu+1\r");
        self.t.read_until(prompt);
        print("spawning session to " + cmd + "as console" if console else "")
        

    def cmd(self,cmd):
        self.t.write(cmd + linesep)
        s = self.t.read_until( prompt )
        time.sleep(0.01)
        self.t.read_eager()
        return s 
    def sendline(self,cmd):
        self.t.write(cmd + linesep)

    def expect(self,expected):
      #  print "waiting for expected "+expected
        return self.t.expect(expected)
#
#    def logfile(self,filename = sys.stdout):
#        import tempfile
#        self.t.logfile = filename 
#
#    def interact(self):
#        self.t.interact()

def main():

    import myCfg
    c = myCfg.myCfg()
    nodeip = c.get("node","ip")
    slot = c.get("node","slot")
    port = '200' +slot   
    t = vxConsole(nodeip,port)
    print  (t.cmd(b"eqaStat"))
    print  (t.cmd(b"mManufDisplay"))
#    t.sendline('mManufDisplay'+ linesep)
#    print t.expect(['number'])
#    print t.expect(['->'])
    return t

if __name__ == "__main__":
    t = main()
