 /*
  * Copyright 2017 Cisco Systems
  */

/**
 * Generating Python for alarm blocks
 * @author ankmaury@cisco.com (Ankit Maurya)
 */


'use strict';

goog.provide('Blockly.Python.console');

goog.require('Blockly.Python');

var consoleExpect = {};
var tl1Expect     = {};
var telnetExpect  = {};

consoleExpect["console_arrow_id"] = "cmd";
consoleExpect["console_hash_id"]  = "cmdHash";
consoleExpect["console_uboot_id"] = "cmdUboot";


tl1Expect["tl1_carrot_id"] = "cmd";
tl1Expect["tl1_hash_id"]  = "cmdHash";
tl1Expect["tl1_uboot_id"] = "cmdUboot";


telnetExpect["telnet_arrow_id"] = "cmd";
telnetExpect["telnet_hash_id"]  = "cmdHash";
telnetExpect["telnet_uboot_id"] = "cmdUboot";







Blockly.Python['console'] = function(block) {
  var text_console_cmd = block.getFieldValue('console_cmd');
  var text_console_id = block.getFieldValue('console_id');
  var dd_console_expect = block.getFieldValue('console_expect');

  // TODO: Assemble Python into code variable.
  var code  = "#Send console cmd" + '\n';
  code = code + "print cardConsole" + text_console_id +  "." + consoleExpect[dd_console_expect] + "('" + text_console_cmd + "')" + '\n';
  code = code + "time.sleep(3)";
  return code + '\n' + '\n';
};

Blockly.Python['telnet'] = function(block) {
  var text_telnet_cmd = block.getFieldValue('telnet_cmd');
  var text_telnet_id  = block.getFieldValue('telnet_id');
  var dd_telnet_expect = block.getFieldValue('telnet_expect');

  // TODO: Assemble Python into code variable.
  var code  = "#Send telnet cmd" + '\n';
  code = code + "print cardTelnet" + text_telnet_id + "." + telnetExpect[dd_telnet_expect] + "('" + text_telnet_cmd + "')" + '\n';
  code = code + "time.sleep(3)";
  return code + '\n' + '\n';
};


Blockly.Python['tl1'] = function(block) {
  var text_tl1_cmd = block.getFieldValue('tl1_cmd');
  var text_tl1_id  = block.getFieldValue('tl1_id');
  var dd_tl1_expect = block.getFieldValue('tl1_expect');

console.log(dd_tl1_expect)
  // TODO: Assemble Python into code variable.
  var code  = "#Send tl1 cmd" + '\n';
  code = code + "print tl1_" + text_tl1_id + "." + tl1Expect[dd_tl1_expect] + "('" + text_tl1_cmd + "')" + '\n';
  code = code + "time.sleep(3)";
  return code + '\n' + '\n';
};