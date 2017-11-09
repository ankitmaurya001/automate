#! /usr/bin/env python
import os
import sys

if os.path.realpath('/ws/marigcha-bgl/regression/utils/') not in sys.path:
    sys.path.append(os.path.realpath('/ws/marigcha-bgl/regression/utils/')) # put dir containing this file in path


import jdsu

#(jdsuip,jdsuslot,jdsuports) = ('10.64.109.65',5,[1,2,3,4])
(jdsuip,jdsuslot,jdsuports) = ('10.64.109.230',2,[1])

testsets = [jdsu.Jdsu(jdsuip , jdsuslot , jdsuport) for jdsuport in jdsuports]
#[testset.restartMeasurement() for testset in testsets]
map(jdsu.Jdsu.restartMeasurement,testsets)
