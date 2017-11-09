from utils.vxConsole import vxConsole

(ip,port) = ('fwts7',2039)
card = vxConsole(ip,port,True)
print card.cmd("eqaStat")
