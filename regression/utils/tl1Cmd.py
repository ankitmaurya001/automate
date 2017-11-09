#! /usr/bin/env python


import tl1


t = tl1.Tl1('10.64.106.50')
verbCmds = {}
for cmd in tl1.verbs:
    verbCmds[cmd] = t.cmd(cmd + '-?')


print verbCmds
