#! /usr/bin/env python


from utils.tl1 import Tl1


# initialize variables 
node  = '10.106.150.218'

sw_m15_node = '10.64.106.24'
sw_m6_node = '10.64.106.234'

hw_m6_node = '10.106.150.225'

# Establish Tl1 connection
#tl = Tl1(node)
#tl = Tl1(sw_m15_node)
#tl = Tl1(sw_m6_node)
#tl = Tl1(hw_m6_node)
#tl = Tl1('10.58.234.43')
#tl = Tl1('10.106.149.177')
#tl = Tl1('10.58.234.43')
#tl = Tl1('172.23.19.164')
#tl = Tl1('10.106.149.177')
#tl = Tl1('172.23.19.176')
#tl = Tl1('172.23.19.176')
tl = Tl1('172.23.19.167')
    
    
print tl.cmd('rtrv-inv::all:scr;')

print 20 * "*"


print tl.cmd('rtrv-eqpt::all:scr;') 
