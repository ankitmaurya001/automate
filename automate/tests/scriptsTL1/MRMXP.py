#! /usr/bin/env python

# import functions
from utils.tl1 import Tl1
from utils.jdsu import Jdsu
from utils.vxPython import vxConsole
from time import sleep
import sys
import time
import datetime
if(len(sys.argv)==4):
    (pname,node,client,server)=sys.argv
    print client
    print server
else:
    print "No/Wrong arguments recieved...Use the following format"
    print "         ./tests/lldp_jdsu.py <nodeIp> <clientSlot> <serverSlot>"
    sys.exit(6)
#initialize variables
#node  = '10.64.106.148'
class testsets:
    a=Jdsu
    b=Jdsu
def create_testsets():
    jdsuOpt = raw_input('Option(def1/man):')
    if(jdsuOpt=="def1"):
        (jdsuip1,jdsuslot1,jdsuport1) = ('10.64.109.230',1,1)
        (jdsuip2,jdsuslot2,jdsuport2) = ('10.64.109.230',2,4)
    elif(jdsuOpt=="def2"):
        (jdsuip1,jdsuslot1,jdsuport1) = ('10.64.109.230',2,1)
        (jdsuip2,jdsuslot2,jdsuport2) = ('10.64.109.230',2,2)
    elif(jdsuOpt=="def3"):
        (jdsuip1,jdsuslot1,jdsuport1) = ('10.64.109.30',2,1)
        (jdsuip2,jdsuslot2,jdsuport2) = ('10.64.109.30',4,1)
    else:
        jdsuip1=raw_input('jdsuip1:')
        jdsuslot1=raw_input('jdsuslot1:')
        jdsuport1=raw_input('jdsuport1:')
        jdsuip2=raw_input('jdsuip2:')
        jdsuslot2=raw_input('jdsuslot2:')
        jdsuport2=raw_input('jdsuport2:')
    
    testset1 = Jdsu(jdsuip1,jdsuslot1,jdsuport1)
    testset2 = Jdsu(jdsuip2,jdsuslot2,jdsuport2)
    k=testsets 
    k.a =testset1
    k.b=testset2
    return k

Vfacs =('VFAC-3-2-1','VFAC-3-3-1','VLINE-3-2-1-1','VLINE-3-2-1-2','VLINE-3-2-1-3','VLINE-3-2-1-4','VLINE-3-3-1-1','VLINE-3-3-1-2','VLINE-3-3-1-3','VLINE-3-3-1-4')
# Establish Tl1 connection
#t1=Tl1(node)
card = vxConsole(node,'')
print "reched here"
def import_test():
    print "Successfully imported"
    return "21221"

def create_ports(payload, port_num):
    print t1.cmd('ent-'+ payload +'::'+Vfacs[port_num]+':scr;')
    sleep(3)

def delete_ports(payload, port_num):
    print t1.cmd('dlt-'+payload+'::'+Vfacs[port_num]+':scr')
    sleep(3)

def ports_enable(port_name, port_num):
    print tl.cmd('ed-'+port_name+'::'+Vfacs[port_num]+':scr::::is;') 
    sleep(3)

def ports_disable(port_name, port_num):
    print t1.cmd('ed-'+port_name+'::'+Vfacs[port_num]+':scr:::CMDMDE=FRCD:OOS,DSBLD;')
    sleep(3)

def get_gcc_ip(slot):
    str = card.cmd('debugGetCardGccIpAddr (1,'+ slot+')')
    return str;
def set_gcc_ip(slot,ip):
    print card.cmd('debugSetCardGccIpAddr (1,'+ slot +', "172.16.0.'+repr(ip)+'")')

def del_gcc_ip(slot):
    print card.cmd('debugSetCardGccIpAddr (1,'+ slot +', "0x0")')

def set_dest_ip(slot,ip):
    print card.cmd('debugSetDestGccConfig (1,'+ slot +',29,1, "172.16.0.'+repr(ip)+'")')

def en_card_authonport(slot):
    print card.cmd('debugSetCardAuthOnPort(1,'+ slot +',29,1,1)')

def en_portencry_security(slot):
    print card.cmd('debugSetPortEncrySecurity(1,'+ slot +',29,1,0,0)')

def dis_card_authonport(slot):
    print card.cmd('debugSetCardAuthOnPort(1,'+slot+',29,0,0)')

def dis_portencry_security(slot):
    print card.cmd('debugSetPortEncrySecurity(1,'+slot+',29,0,0,0)')

def reset_master_key(slot):
    print card.cmd('debugResetMasterkey(1,'+ slot +',29)')


def send_reboot(slot,ar):
    card = vxConsole(node,'200'+slot)
    if(ar==0):
        print card.sendline("reboot")
    else:
        card.sendline("reboot 2")
    card.t.close()

def send_hadreboot(slot):
    card = vxConsole(node,'200'+slot)
    print card.sendline('reboot 2')
    card.t.close()
    
def default_config():
    print "Use any of the following options" 
    print "gcc2  auth_en enc_en auth_dis enc_dis exit"
    while(1):
        input = raw_input('Option: ')
        print input
        if(input=="exit"):
            print input + " Called!!"
            sys.exit(1)
        elif(input=="gcc2"):
            print input + " Called!!"
            set_gcc_ip(client,2)
            set_gcc_ip(server,1)
            set_dest_ip(client,1)
            set_dest_ip(server,2)
        elif(input=="auth_en"):
            print input + " Called!!"
##            en_card_authonport(server)
            en_card_authonport(client)
        elif(input=="enc_en"):
            print input + " Called!!"
            en_portencry_security(client)
            en_portencry_security(server)
        elif(input=="auth_dis"):
            print input + " Called!!"
            dis_card_authonport(server)
            dis_card_authonport(client)
        elif(input=="enc_dis"):
            print input + " Called!!"
            dis_portencry_security(server)
            dis_portencry_security(client)
        elif(input=="break"):
            break


#default_config()

def check_gcc_ips(slot,ip):
    str = get_gcc_ip(slot)
    gcc2 = str.split("\n")[1].split("= ")[1]
    if(gcc2=="172.16.0."+repr(ip)):
        return 1
    else:
        return 0


def check_tls(client,server,stat):
    sleep(50)   #min 35
    client_card = vxConsole(node,'200'+client)
    server_card = vxConsole(node,'200'+server)
    clt_log= client_card.cmd('dumpTlsStatus')
    ser_log= server_card.cmd('dumpTlsStatus')
    clt_state = clt_log.split("\n")[2].split("tls ")[1].split(" ")[0]
    ser_state = ser_log.split("\n")[2].split("tls ")[1].split(" ")[0]
    print clt_state
    print ser_state
    if(stat==1):
        if(clt_state=='Up' and ser_state=='Up'):
            return 1
        else:
            fo = open("Error.txt", "a")
            print fo.write("Error " +clt_state + " " + ser_state +"\n");
            fo.close()
            return 0
    if(stat==0):
        if(clt_state=='Down' and ser_state=='Down'):
            return 1
        else:
            fo = open("Error.txt", "a")
            print fo.write("Error " +clt_state + " " + ser_state +"\n");
            fo.close()
            return 0
    
#Encryption Full Scale Test
def softboot_test(client,server):
    (jdsuip1,jdsuslot1,jdsuport1) = ('10.64.109.30',2,1)
    (jdsuip2,jdsuslot2,jdsuport2) = ('10.64.109.30',5,1)
    testset1 = Jdsu(jdsuip1,jdsuslot1,jdsuport1)
    testset2 = Jdsu(jdsuip2,jdsuslot2,jdsuport2)
    i=0
    while(i<100):
        send_reboot(server,0)
        send_reboot(client,0)
        sleep(300)
        if(testset1.isTrafficHit() | testset2.isTrafficHit()):
            print "Traffic hit somewhere in softreboot"
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            fo = open("softReboot.txt", "a")
            print fo.write("Error " + repr(testsets.a.isTrafficHit()) + " " + repr(testsets.b.isTrafficHit()) + " " +st +"\n");
            fo.close()
        i=i+1
    print "Softboot test done"

def hardboot_test(client,server):
    (jdsuip1,jdsuslot1,jdsuport1) = ('10.64.109.30',2,1)
    (jdsuip2,jdsuslot2,jdsuport2) = ('10.64.109.30',5,1)
    testset1 = Jdsu(jdsuip1,jdsuslot1,jdsuport1)
    testset2 = Jdsu(jdsuip2,jdsuslot2,jdsuport2)
    i=0
    while(i<100):
        print repr(i)
        send_reboot(server,2)
        send_reboot(client,2)
        sleep(500)
        res1=not testset1.isTrafficUp()
        res2=not testset2.isTrafficUp()
        if(res2 | res1):
            print "Traffic down somewhere in Hardreboot"
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            fo = open("HardReboot.txt", "a")
            print fo.write("Error " + repr(testsets.a.isTrafficUp()) + " " + repr(testsets.b.isTrafficUp()) + " " +st +"\n");
            fo.close()
        i=i+1
#softboot_test(client,server)
def enc_full(client,server):
    set_gcc_ip(server,1)
    set_gcc_ip(client,1)
    set_dest_ip(server,2)
    set_dest_ip(client,1)
    en_card_authonport(client)
    en_card_authonport(server)
    sleep(60)
    en_portencry_security(client)
    en_portencry_security(server)
    i=1
    while(testsets.a.isTrafficUp()!='True' | testsets.a.isTrafficUp()!='True'):
        print "Traffic down after "+repr(i*60)+" seconds after enabling config"    
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        fo = open("EncFullLength.txt", "a")
        print fo.write("Error after enabling config" + repr(testset.isTrafficUp()) + " " +st +"\n")
        fo.close()
        sleep(60)
        if(i>10):
            print "Critical issue exiting script"
            sys.exit(3)
    
    dis_portencry_security(server)
    dis_portencry_security(client)
    dis_card_authonport(server)
    dis_card_authonport(client)
    del_gcc_ip(client)
    del_gcc_ip(server)
    i=0
    while(testset.isTrafficUp()!='True'):
        print "Traffic down after "+repr(i*10)+" seconds after disabling config"    
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        fo = open("EncFullLength.txt", "a")
        print fo.write("Error after disabling config" + repr(testset.isTrafficUp()) + " " +st +"\n")
        fo.close()
        sleep(10)
        if(i>12):
            print "Critical issue exiting script"
            sys.exit(3)


    
##enc_full(client,server)


#AuthEnDis
def auth_regression_test(client,server):
    while(1):
        dis_card_authonport(client)
        check_tls(client,server,0)
        dis_card_authonport(server)
        check_tls(client,server,0)
        en_card_authonport(client)
        check_tls(client,server,0)
        en_card_authonport(server)
        sleep(70)   #min 35
        check_tls(client,server,1)

#EncEnDis
def enc_enable_disable(client,server):
    dis_portencry_security(client)
    dis_portencry_security(server)
    
    en_portencry_security(server)
    en_portencry_security(client)

#keyExSoak
def key_ex_soak(slot):
    testsets=create_testsets()
    while(1):
        reset_master_key(client)
        sleep(52)
        if(testsets.a.isTrafficHit() | testsets.b.isTrafficHit()):
            print "Traffic hit somewhere"
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            fo = open("KeyExError.txt", "a")
            print fo.write("Error " + repr(testsets.a.isTrafficHit()) + " " + repr(testsets.b.isTrafficHit()) + " " +st +"\n");
            fo.close()
            testsets.a.query(':ABOR;*WAI;:INIT:IMM:ALL;*WAI')
            testsets.b.query(':ABOR;*WAI;:INIT:IMM:ALL;*WAI')
            
#key_ex_soak(client)

#GCC2 IP Test Case
    
def gcc2_prov_test(slot):
    while(1):
        del_gcc_ip(slot)
        set_gcc_ip(slot,1)
        if(check_gcc_ips(slot,1) != 1):
            print "Failed!!"
            sys.exit(1)
#SOAKED 16/07
def del_crt_payload(port):
    index=0
    testset=create_testsets()
    while(1):
        create_ports("10gige",port)
        sleep(5)
        delete_ports("10gige",port)
        sleep(5)
        index=index+1
        print "dsdasadasd"+repr(index)
        if(testset.a.isTrafficHit() | testset.b.isTrafficHit()):
            print "del_crt Failed!!"
            sys.exit(2)


#auth_regression_test(client,server)












#FALCO Encryption Soak
#create_ports(10gige,3)
#ports_enable(10gige,3)
#dis_portencry_security(client)
#dis_portencry_security(server)
#print check_gcc_ips(client,4)
#dis_portencry_security(3)
#set_gcc_ip(client,4)
#set_gcc_ip(server,3)
#set_dest_ip(client,1)
#set_dest_ip(server,2)
#en_card_authonport(client)
#en_card_authonport(server)
#en_portencry_security(client)
#en_portencry_security(server)
#print "succes"

