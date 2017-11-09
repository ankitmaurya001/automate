 /*
  * Copyright 2017 Cisco Systems
  */

/**
 * Generating Python for time blocks
 * @author ankmaury@cisco.com (Ankit Maurya)
 */


'use strict';

goog.provide('Blockly.Python.time');

goog.require('Blockly.Python');


Blockly.Python['time'] = function(block) {
  var text_sleep_sec = block.getFieldValue('sleep_sec');
  // TODO: Assemble Python into code variable.
  
  var code =  "time.sleep(" + text_sleep_sec + ")";
  return code + '\n' + '\n';
  
};