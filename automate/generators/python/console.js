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




Blockly.Python['console'] = function(block) {
  var text_console_cmd = block.getFieldValue('console_cmd');

  // TODO: Assemble Python into code variable.
  var code  = "#Send console cmd" + '\n';
  code = code + "print card.cmd('" + text_console_cmd + "')" + '\n';
  code = code + "time.sleep(3)";
  return code + '\n' + '\n';
};


Blockly.Python['tl1'] = function(block) {
  var text_tl1_cmd = block.getFieldValue('tl1_cmd');

  // TODO: Assemble Python into code variable.
  var code  = "#Send tl1 cmd" + '\n';
  code = code + "print tl1.cmd('" + text_tl1_cmd + "')" + '\n';
  code = code + "time.sleep(3)";
  return code + '\n' + '\n';
};