#! /usr/bin/env python
import pexpect
import sys

prompt = b'->'
#nodeip = '10.64.106.50'
#port = '23'
nodeip = '10.64.108.116'
port = '2052'

command = "telnet " + nodeip + " " + repr(port)

t = pexpect.spawn(command)

t.logfile = open("testlog.log","w")

def cmd(self,cmd):
    self.send(cmd)
    self.send('\r')
    self.expect_exact(prompt)
    return self.before

pexpect.spawn.cmd = cmd

t.cmd("flmStat")

#for line in sys.stdin:
#    print t.cmd(line)

