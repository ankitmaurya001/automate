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
//Blockly.Python.addReservedWords('math,random,Number,node');

//'#! /usr/bin/env python' + '\n' + '\n' 
Blockly.Python['node_details'] = function(block) {
  var node_ip         = block.getFieldValue('node_details_ip');
  var node_id    = block.getFieldValue('node_id');

  var code1 ;
  /*
  code1 = 'import os' + '\n' + 'import sys' + '\n' + 'import time' + '\n' +'import math' + '\n' + 'from numbers import Number' + '\n' +'\n' + '\n';
  code1 = code1 + "if os.path.realpath('/ws/ankmaury-bgl/regression/utils/') not in sys.path:" + '\n';
  code1 = code1 + "	" + "sys.path.append(os.path.realpath('/ws/ankmaury-bgl/regression/utils/')) # put dir containing this file in path"
  code1 = code1 + '\n' + '\n' ;
  code1 = code1 + 'import tl1' + '\n' + 'import jdsu' + '\n' + 'import vxConsole' + '\n' + '\n';
  */
  code1 = '# initialize variables' + '\n' + '\n';
  code1 = code1 + 'node' + node_id +  ' =' + '"' + node_ip + '"'  + '\n';
  code1 = code1 + 'tl1_' + node_id +  '= tl1.Tl1(node' + node_id+ ')';
  code1 = code1 + '\n' + '\n';
  /*
  code1 = code1 + '# Create console object' + '\n'
  code1 = code1 + "card = vxConsole.vxConsole('" + console_ip + "', '" + console_port + "', " + 'console = True)';
  code1 = code1 + '\n' + '\n';
  */

  //var code = '\n' + '\n';

 //Blockly.Python.definitions_['import_node'] = code1;
 // return '\n';
 return code1 + '\n' ;
 

};





Blockly.Python['console_details'] = function(block) {
  var console_ip         = block.getFieldValue('console_ip');
  var console_port       = block.getFieldValue('console_port');
  var console_id         = block.getFieldValue('console_id');

  var code1 ;
 
 
  code1 = '# Create console object' + '\n'
  code1 = code1 + "cardConsole" + console_id +  " = vxConsole.vxConsole('" + console_ip + "', '" + console_port + "', " + 'console = True)';
  code1 = code1 + '\n' ;

 return code1 + '\n' ;
 

};



Blockly.Python['telnet_details'] = function(block) {
  var telnet_ip           = block.getFieldValue('telnet_ip');
  var telnet_port         = block.getFieldValue('telnet_port');
  var telnet_id           = block.getFieldValue('telnet_id');

  var code1 ;
 
 
  code1 = '# Create telnet object' + '\n'
  code1 = code1 + "cardTelnet" + telnet_id +  " = vxConsole.vxConsole('" + telnet_ip + "', '" + telnet_port + "', " + 'console = False)';
  code1 = code1 + '\n' ;

  return code1 + '\n' ;
 

};


