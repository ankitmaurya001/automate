#! /usr/bin/env python

import telnetlib
import threading

#bad place to declare a lock but init can't call cmd if any variable is shared
#mylock = threading.Lock()

verbs = {
        'ent' : 'create',
        'ed'  : 'modify',
        'dlt' : 'remove',
        'opr' : 'apply',
        'rtrv' : 'retrive',
        }

modifier1 = {
        'och' : 'circuit',
        'lpbk' : 'loopback',
        'opmode' : 'operating mode',
        }



port = 3083
timeout = 100
prompt = '\r\n>'
class Tl1:

    def __init__(self, ip,
                 user = "CISCO15", password = "otbu+1", 
                 verbose = 0):
        """Create a Tl1 telnet connection to the SC.
        """
        self.ip = ip
        self.connectionPort = port
        self.connection = telnetlib.Telnet(self.ip,self.connectionPort)
        self.timeout = timeout
        self.connection.read_until(prompt,self.timeout)
        request = "ACT-USER::%s:123::%s;" % (user,password)
        print (self.cmd(request))
        #Don't bother me with status
        self.cmd('INH-MSG-ALL:::a;')  
    

    def cmd(self,cmd):
        #        self.timer.cancel()
#        del self.timer
#        self.timer = threading.Timer(30,self.cmd, '\n')
 #       with mylock:
           self.connection.read_eager()
           self.connection.write(cmd)
           if cmd[-1] is not ";":
                self.connection.write(b";") # command should end with ; 
           self.connection.write(b"\n")
  #         self.timer.start()
           return self.connection.read_until(prompt,timeout)

    def setFacLpbk(self,portid):
        print (self.cmd('ed-och::chan-'+portid+':scr::::oos,mt;'))
        print (self.cmd('opr-lpbk-och::chan-' + portid + ':scr::,,,facility;'))

    def releaseFacLpbk(self,portid):
        print (self.cmd('rls-lpbk-och::chan-' + portid + ':scr::,,,facility;'))
        print (self.cmd('ed-och::chan-'+portid+':scr::::is;'))

    def provision10GIGE(self,port):
        mycmd = 'ent-10gige::'+port+':scr;'
        print ("provisioning port " + port +" with command " + mycmd)
        return self.cmd(mycmd)
    
    def remove10GIGE(self,port):
        mycmd = 'dlt-10gige::'+port+':scr;'
        return self.cmd(mycmd)
        

if __name__ == "__main__":
    t = Tl1('10.64.106.50')
    print ("connection made")
    print ("requesting command")
    print (t.cmd('rtrv-10gige::all:C1'))
