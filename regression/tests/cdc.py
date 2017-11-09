#! /usr/bin/env python


from utils.tl1 import Tl1


# initialize variables 
#node  = '10.106.150.225'
node  = '173.23.200.160'




# Establish Tl1 connection
tl = Tl1(node)
    


print tl.cmd('rtrv-inv::all:scr;')

print tl.cmd('rtrv-usbp::all:scr;')
print 40 * "*"
#print tl.cmd('ent-eqpt::pshelf-20:c::pshelf-mf10-6ru')
#print tl.cmd('ent-eqpt::pshelf-30:c::pshelf-mf10-6ru')
#print tl.cmd('ent-eqpt::pshelf-70:c::pshelf-mf10-6ru')
#print tl.cmd('ent-eqpt::pshelf-80:c::pshelf-mf10-6ru')
#for m15
print tl.cmd('ed-eqpt::pshelf-30:c:::usb=usbport-1-18-13')
print tl.cmd('ed-eqpt::pshelf-20:c:::usb=usbport-1-18-14')
#for m15
#print tl.cmd('ed-eqpt::pshelf-20:c:::usb=USBP-1-A-5')
#print tl.cmd('ed-eqpt::pshelf-30:c:::usb=USBP-1-B-5')


#print tl.cmd('ed-eqpt::pshelf-70:c:::usb=PSUSB-20-11')
#print tl.cmd('ed-eqpt::pshelf-80:c:::usb=PSUSB-30-11')




print 40 * "*"

print tl.cmd('rtrv-eqpt::all:scr;') 