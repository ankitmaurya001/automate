#! /usr/bin/env python
#import telnetlib
import fileinput
import pexpect
import sys
""" Global Variables """
prompt = b'->'

class vxConsole:
    """ Find out why inbuilt telnet module is not working """
    def __init__(self,nodeip,port,console = False):
#        self.t = telnetlib.Telnet(nodeip,port)
#        self.t.set_debuglevel(15)
#        self.t.read_until(b"Login:")
#        self.t.write(b"CISCO15\r")
#        self.t.read_until("Password:");
#        self.t.write(b"otbu+1\r");
#        self.t.read_until(prompt);
        cmd = "telnet " + nodeip + " " + repr(port)
        print("spawning session to " + cmd + "as console" if console else "")
#        self.t = pexpect.spawn("telnet 10.64.106.50\r");
        self.t = pexpect.spawn(cmd);
#        self.t.logfile = sys.stdout
        self.console = console
        if not self.console:
        #auto determine if console or not if Login prompt not given within 10 sec try it as console
            try:
                self.t.expect_exact(b"Login:",10);
                self.t.send(b"CISCO15\r");
                self.t.expect_exact(b"Password:");
                self.t.send(b"otbu+1\r");
                self.t.expect_exact(prompt);
            except pexpect.TIMEOUT:
                print ("Login prompt not found probably a console")
                self.console = True
                self.t.send(b'\r')
                self.t.expect_exact(prompt)

    def cmd(self,cmd):
#        self.t.write(cmd)
#        self.t.write(b'\r')
        self.t.send(cmd)
        self.t.send('\r')
        self.t.expect_exact(prompt)
        return self.t.before
        #return self.t.read_until(prompt)

    def sendline(self,cmd):
        self.t.sendline(cmd)

    def expect(self,string):
        self.t.expect_exact(string)

    def logfile(self,filename = sys.stdout):
        import tempfile
        self.t.logfile = filename 

    def interact(self):
        self.t.interact()

if __name__ == "__main__":
    import myCfg
    c = myCfg.myCfg()
#    nodeip = "10.64.109.230"
#    slot = 2 
#    port = 4
    nodeip = c.get("node","ip")
    slot = c.get("node","slot")
#    port = c.get("node","port")
    port = '200' +slot   
    #t = pexpect.spawn(nodeip,port)

    t = vxConsole(nodeip,port)
#    t = vxConsole('10.64.108.116','2050')
    #print  t.sendcmd(b"")
    print  t.cmd(b"eqaStat")
    print  t.cmd(b"mManufDisplay")

#    for line in fileinput.input():
#        #    print(line)
#        print (t.sendcmd(line.rstrip()))

