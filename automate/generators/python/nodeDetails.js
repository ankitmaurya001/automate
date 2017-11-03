 /*
  * Copyright 2017 Cisco Systems
  */

/**
 * Generating Python for alarm blocks
 * @author ankmaury@cisco.com (Ankit Maurya)
 */

'use strict';

goog.provide('Blockly.Python.nodeDetails');

goog.require('Blockly.Python');

//card = vxConsole.vxConsole(cardConsoleIp, cardConsolePort,console = True) 

// If any new block imports any library, add that library name here.
Blockly.Python.addReservedWords('math,random,Number,node');

//'#! /usr/bin/env python' + '\n' + '\n' 
Blockly.Python['node_details'] = function(block) {
  var tv_ip         = block.getFieldValue('node_details_ip');
  var console_ip    = block.getFieldValue('console_ip');
  var console_port  = block.getFieldValue('console_port');

  var code1 ;
  code1 = 'import os' + '\n' + 'import sys' + '\n' + 'import time' + '\n' +'import math' + '\n' + 'from numbers import Number' + '\n' +'\n' + '\n';
  code1 = code1 + "if os.path.realpath('/ws/ankmaury-bgl/regression/utils/') not in sys.path:" + '\n';
  code1 = code1 + "	" + "sys.path.append(os.path.realpath('/ws/ankmaury-bgl/regression/utils/')) # put dir containing this file in path"
  code1 = code1 + '\n' + '\n' ;
  code1 = code1 + 'import tl1' + '\n' + 'import jdsu' + '\n' + 'import vxConsole' + '\n' + '\n';
  code1 = code1 + '# initialize variables' + '\n' + '\n';
  code1 = code1 + 'node1 =' + '"' + tv_ip + '"'  + '\n';
  code1 = code1 + 'tl1 = tl1.Tl1(node1)';
  code1 = code1 + '\n' + '\n';
  code1 = code1 + '# Create console object' + '\n'
  code1 = code1 + "card = vxConsole.vxConsole('" + console_ip + "', '" + console_port + "', " + 'console = True)';
  code1 = code1 + '\n' + '\n';

  //var code = '\n' + '\n';

 Blockly.Python.definitions_['import_node'] = code1;
  return '\n';

};


