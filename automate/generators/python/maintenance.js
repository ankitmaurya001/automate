
 /*
  * Copyright 2017 Cisco Systems
  */

/**
 * Generating Python for maintenance blocks
 * @author ankmaury@cisco.com (Ankit Maurya)
 */

'use strict';

goog.provide('Blockly.Python.maintenance');

goog.require('Blockly.Python');

var maintenance_payloads = {};
maintenance_payloads["TEN_GIGE_ID"] = "10GIGE";
maintenance_payloads["OC192_ID"]    = "OC192";
maintenance_payloads["OTU2_ID"]     = "OTU2";
maintenance_payloads["OCH_ID"]      = "OCH";


var dd_adminstate = {};
dd_adminstate["IS_ID"]		     = ":IS";
dd_adminstate["OOS_DSBLD_ID"]    = "CMDMDE=FRCD:OOS,DSBLD" ;
dd_adminstate["OOS_MT_ID"]       = "CMDMDE=FRCD:OOS,MT" ;
dd_adminstate["IS_AINS_ID"]      = "CMDMDE=FRCD:IS,AINS" ;


Blockly.Python['maintenance_loopback'] = function(block) {
  var text_NodeId = block.getFieldValue('NodeId');
  var text_Shelf  = block.getFieldValue('Shelf');
  var tv_maintenance_loopback_slot = block.getFieldValue('maintenance_loopback_slot');
  var dd_maintenance_loopback_card = block.getFieldValue('maintenance_loopback_card');
  var tv_maintenance_port = block.getFieldValue('maintenance_port');
  var dd_loopback_payload = block.getFieldValue('maintenance_loopback_payload');
  var dd_adminstate_val = block.getFieldValue('maintenance_loopback_adminState');
  var dd_loopbacktype_val = block.getFieldValue('loopbackType');
  // TODO: Assemble Python into code variable.
  var code = "#Change port state" + '\n';
  var portState ;
  var aid ;
  console.log(dd_adminstate_val);
  portState = dd_adminstate[dd_adminstate_val];
  console.log(portState);
  if(maintenance_payloads[dd_loopback_payload] == "OCH"){
  	aid = "CHAN-" + text_Shelf + "-" + tv_maintenance_loopback_slot + "-" + tv_maintenance_port;
  }else{
  	aid = "VFAC-" + text_Shelf + "-" + tv_maintenance_loopback_slot + "-" + tv_maintenance_port + "-1";
  }

  code = code + "print tl1_" + text_NodeId +".cmd('ed-" + maintenance_payloads[dd_loopback_payload] + "::" + aid ;
  code = code + ":scr:::" + portState + ";')"  + '\n';
  code = code + "time.sleep(3)";
  return code + '\n' + '\n';
};