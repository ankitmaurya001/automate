from utils.vxPython import vxConsole
from utils.jdsu import Jdsu


(node,slots) = ('10.64.106.150',[2,3,4,5,6,7])
(jdsuip,jdsuslot,jdsuports) = ('10.64.109.230',2,[1])
cards =[ vxConsole(node,'200'+repr(slot)) for slot in slots]

testset10G_1 = Jdsu('10.64.109.230',2,1)
testset40G = Jdsu('10.64.109.230',3,1)

card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x0000000,2')
testset10G_1.isTrafficUp()
card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x0000000,0')

card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x1000000,2')
testset10G_2.isTrafficUp()

card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x1000000,0')

card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x2000000,2')
testset10G_2.isTrafficUp()
card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x2000000,0')

card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x3000000,2')
card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x4000000,2')
testset40G_1.isTrafficUp()

card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x3000000,0')
card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x4000000,0')

card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x1f,1')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[6].cmd('adpt_loopback_set(adpt_get_devid(),0x1f,0')
card[6].cmd('   TpDrv "otn loop cg 3 en" ')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[6].cmd('   TpDrv "otn loop cg 3 dis" ')
### slot 6 Loopback Testing OVER #####


card[7].cmd('   TpDrv "otn loop cg 1 en" ')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[7].cmd('   TpDrv "otn loop cg 1 dis" ')

card[7].cmd('adpt_loopback_set(adpt_get_devid(),0x1,2')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[7].cmd('adpt_loopback_set(adpt_get_devid(),0x1,0')
card[7].cmd('adpt_loopback_set(adpt_get_devid(),0x0,1')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[7].cmd('adpt_loopback_set(adpt_get_devid(),0x0,0')

card[7].cmd(' in112510LD_shallow_optical_loopback 0,0')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[7].cmd('in112510LD_mission_mode 0,0')
### Slot 7 loopback Testing over ###
card[5].cmd(' in112510LD_shallow_system_loopback 0,0')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[5].cmd('in112510LD_mission_mode 0,0')


#
#card[5].cmd('   TpDrv "otn loop cg 4 en" ')
#testset10G_1.isTrafficUp()
#testset10G_2.isTrafficUp()
#testset40G_1.isTrafficUp()
#
#card[5].cmd('   TpDrv "otn loop cg 4 dis" ')
#
card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x1f,2')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x1f,0')



card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x0000000,1')
testset10G_1.isTrafficUp()
card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x0000000,0')

card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x1000000,1')
testset10G_2.isTrafficUp()

card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x1000000,0')

card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x2000000,1')
testset10G_2.isTrafficUp()
card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x2000000,0')

card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x3000000,1')
card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x4000000,1')
testset40G_1.isTrafficUp()

card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x3000000,0')
card[5].cmd('adpt_loopback_set(adpt_get_devid(),0x4000000,0')



### slot 5 Loopback Testing OVER #####


card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x0000000,2')
testset10G_1.isTrafficUp()
card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x0000000,0')

card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x1000000,2')
testset10G_2.isTrafficUp()

card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x1000000,0')

card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x2000000,2')
testset10G_2.isTrafficUp()
card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x2000000,0')

card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x3000000,2')
card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x4000000,2')
testset40G_1.isTrafficUp()

card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x3000000,0')
card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x4000000,0')

card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x1f,1')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[4].cmd('adpt_loopback_set(adpt_get_devid(),0x1f,0')
card[4].cmd('   TpDrv "otn loop cg 3 en" ')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[4].cmd('   TpDrv "otn loop cg 3 dis" ')
### slot 4 Loopback Testing OVER #####

card[2].cmd('   TpDrv "otn loop cg 0 en" ')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[2].cmd('   TpDrv "otn loop cg 0 dis" ')

card[2].cmd('adpt_loopback_set(adpt_get_devid(),0x1,2')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[2].cmd('adpt_loopback_set(adpt_get_devid(),0x1,0')
card[2].cmd('adpt_loopback_set(adpt_get_devid(),0x0,1')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[2].cmd('adpt_loopback_set(adpt_get_devid(),0x0,0')

card[2].cmd(' in112510LD_shallow_optical_loopback 0,0')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[2].cmd('in112510LD_mission_mode 0,0')
### Slot 2 loopback Testing over ###
card[3].cmd(' in112510LD_shallow_system_loopback 0,0')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[3].cmd('in112510LD_mission_mode 0,0')


#
#card[5].cmd('   TpDrv "otn loop cg 4 en" ')
#testset10G_1.isTrafficUp()
#testset10G_2.isTrafficUp()
#testset40G_1.isTrafficUp()
#
#card[5].cmd('   TpDrv "otn loop cg 4 dis" ')
#
card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x1f,2')
testset10G_1.isTrafficUp()
testset10G_2.isTrafficUp()
testset40G_1.isTrafficUp()

card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x1f,0')



card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x0000000,1')
testset10G_1.isTrafficUp()
card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x0000000,0')

card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x1000000,1')
testset10G_2.isTrafficUp()

card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x1000000,0')

card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x2000000,1')
testset10G_2.isTrafficUp()
card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x2000000,0')

card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x3000000,1')
card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x4000000,1')
testset40G_1.isTrafficUp()

card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x3000000,0')
card[3].cmd('adpt_loopback_set(adpt_get_devid(),0x4000000,0')


### Slot 3 loopback Testing over ###

