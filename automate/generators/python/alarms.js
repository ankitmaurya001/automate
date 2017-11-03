 /*
  * Copyright 2017 Cisco Systems
  */

/**
 * Generating Python for alarm blocks
 * @author ankmaury@cisco.com (Ankit Maurya)
 */

'use strict';

goog.provide('Blockly.Python.alarms');

goog.require('Blockly.Python');

Blockly.Python['alarms_synchronize'] = function(block) {
  
  var code = "print tl1.cmd('rtrv-alm-all:::c::;')" ;
  console.log("alarms_synchronize")
   return code + '\n';
};

Blockly.Python['alarms_filter'] = function(block) {
  
  var code = " 'Filter not implemented yet' ";
  console.log("alarms_filter")
   return 'print(' +  code + ')\n';
};

Blockly.Python['alarms_deleteClearedAlarms'] = function(block) {
  
  var code = " 'Delete Cleared Alarms not implemented yet' ";
  console.log("alarms_deleteClearedAlarms")
  return 'print(' + code + ')\n';
};