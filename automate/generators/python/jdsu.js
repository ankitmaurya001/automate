/*
  * Copyright 2017 Cisco Systems
  */

/**
 * Generating Python for alarm blocks
 * @author ankmaury@cisco.com (Ankit Maurya)
 */

'use strict';

goog.provide('Blockly.Python.jdsu');

goog.require('Blockly.Python');




 var payloads_jdsu = {};
 payloads_jdsu["10_GIGE_ID"]  = "isTrafficUp()";
 payloads_jdsu["OC192_ID"]    = "isTrafficUp_OC192()";
 payloads_jdsu["OTU2_ID"]     = "isTrafficUp_otu2()";



Blockly.Python['jdsu'] = function(block) {
  var tv_jdsu_ip = block.getFieldValue('jdsu_ip');
  var tv_jdsu_slot = block.getFieldValue('jdsu_slot');
  var tv_jdsu_port = block.getFieldValue('jdsu_port');
  var dd_jdsu_payload = block.getFieldValue('jdsu_payload');
  var tv_jdsu_id = block.getFieldValue('jdsu id');
  // TODO: Assemble Python into code variable.
  var code ;
  code = "(jdsuip" + tv_jdsu_id +"," + "jdsuslot" + tv_jdsu_id +"," + "jdsuport" + tv_jdsu_id +")" + "= ('" + tv_jdsu_ip + "'," + tv_jdsu_slot + "," + tv_jdsu_port + ")" + '\n';
  code = code + "testset" + tv_jdsu_id + " = jdsu.Jdsu(jdsuip" + tv_jdsu_id +"," + "jdsuslot" + tv_jdsu_id +"," + "jdsuport" + tv_jdsu_id +")";
  return code + '\n' + '\n';
};



Blockly.Python['jdsu_traffic'] = function(block) {
  var dd_jdsu_payload_traffic = block.getFieldValue('jdsu_payload_traffic');
  var text_jdsu_id = block.getFieldValue('jdsu_id');
  // TODO: Assemble Python into code variable.
  console.log(dd_jdsu_payload_traffic)
  console.log(text_jdsu_id)
  var code ;
  // TODO: Change ORDER_NONE to the correct strength.
  code = "testset" + text_jdsu_id + "."  + payloads_jdsu[dd_jdsu_payload_traffic] ;
  return [code, Blockly.Python.ORDER_NONE];
};

