
/*
  * Copyright 2017 Cisco Systems
  */

/**
 * Generating Python for alarm blocks
 * @author ankmaury@cisco.com (Ankit Maurya)
 */

'use strict';

goog.provide('Blockly.Python.provisioning');

goog.require('Blockly.Python');


 var payloads = {};
 payloads["TEN_GE_ID"] = "10GIGE";
 payloads["OC192_ID"]  = "OC192";
 payloads["OTU2_ID"]   = "OTU2";


 var opmodes = {};
 opmodes["TXP_10G_opmode"]   = "TXP-10G";
 opmodes["RGN_10G_opmode"]   = "RGN-10G";
 opmodes["TXP_100G_opmode"]  = "TXP-100G";
 opmodes["RGN_100G_opmode"]  = "RGN-100G";
 opmodes["MXP_200G_opmode"]  = "MXP-200G";

 var peerCardSlots = {};
 peerCardSlots["N/A_peerCard"]     = "0";
 peerCardSlots["1_peerCard"]       = "1";
 peerCardSlots["2_peerCard"]       = "2";
 peerCardSlots["3_peerCard"]       = "3";
 peerCardSlots["4_peerCard"]       = "4";
 peerCardSlots["5_peerCard"]       = "5";
 peerCardSlots["6_peerCard"]       = "6";
 peerCardSlots["7_peerCard"]       = "7";
 peerCardSlots["8_peerCard"]       = "8";
 peerCardSlots["9_peerCard"]       = "9";
 peerCardSlots["10_peerCard"]      = "10";
 peerCardSlots["11_peerCard"]      = "11";
 peerCardSlots["12_peerCard"]      = "12";
 peerCardSlots["13_peerCard"]      = "13";
 peerCardSlots["14_peerCard"]      = "14";
 peerCardSlots["15_peerCard"]      = "15";
 

 var skipPeerCardSlots = {};
skipPeerCardSlots["N/A_skipPeerCard"]     = "0";
skipPeerCardSlots["1_skipPeerCard"]       = "1";
skipPeerCardSlots["2_skipPeerCard"]       = "2";
skipPeerCardSlots["3_skipPeerCard"]       = "3";
skipPeerCardSlots["4_skipPeerCard"]       = "4";
skipPeerCardSlots["5_skipPeerCard"]       = "5";
skipPeerCardSlots["6_skipPeerCard"]       = "6";
skipPeerCardSlots["7_skipPeerCard"]       = "7";
skipPeerCardSlots["8_skipPeerCard"]       = "8";
skipPeerCardSlots["9_skipPeerCard"]       = "9";
skipPeerCardSlots["10_skipPeerCard"]      = "10";
skipPeerCardSlots["11_skipPeerCard"]      = "11";
skipPeerCardSlots["12_skipPeerCard"]      = "12";
skipPeerCardSlots["13_skipPeerCard"]      = "13";
skipPeerCardSlots["14_skipPeerCard"]      = "14";
skipPeerCardSlots["15_skipPeerCard"]      = "15";


Blockly.Python['provisioning_ppm_createppm'] = function(block) {
  var text_NodeId = block.getFieldValue('NodeId');
  var text_Shelf = block.getFieldValue('Shelf');
  var text_slotname = block.getFieldValue('SlotName');
  var dropdown_provisioning_ppm_createppm_card = block.getFieldValue('provisioning_ppm_createPPM_card');
  var text_ppmno = block.getFieldValue('ppmNo');
  // TODO: Assemble Python into code variable.
 var code = " 'createppm not implemented yet !!' ";
 console.log("provisioning_ppm_createppm")
return 'print(' +  code + ')\n';
};




Blockly.Python['provisioning_ppm_createpayload'] = function(block) {
  var text_NodeId = block.getFieldValue('NodeId');
  var text_Shelf = block.getFieldValue('Shelf');
  var tv_paylaod_slotName = block.getFieldValue('SlotName');
  var dd_paylaod_cardName = block.getFieldValue('provisioning_ppm_createpayload_card');
  var tv_ppmno = block.getFieldValue('ppmNo');
  var dd_paylaod_name = block.getFieldValue('provisioning_ppm_createpayload_payload');
 
  // TODO: Assemble Python into code variable.
  var code  = "#Create payload" + '\n';
  code = code + "print tl1_" + text_NodeId +".cmd('ent-" + payloads[dd_paylaod_name] +'::'+ 'VFAC-' + text_Shelf + "-" + tv_paylaod_slotName + '-' + tv_ppmno + '-1' + ":scr;')" + '\n';
  code = code + "time.sleep(3)";
  return code + '\n' + '\n';
};


  


Blockly.Python['card_create'] = function(block) {
  var tv_create_shelf = block.getFieldValue('card_create_shelf');
  var tv_create_slot = block.getFieldValue('card_create_slot');
  var dd_card_create_opmode = block.getFieldValue('card_create_opmode');
  var dd_card_create_peercard = block.getFieldValue('card_create_peerCard');
  var dd_card_create_skippeercard = block.getFieldValue('card_create_skipPeerCard');
  var cb_peer_card_port_cpak = block.getFieldValue('peer_card_port_CPAK') == 'TRUE';
  var cb_peer_card_port_sfp1 = block.getFieldValue('peer_card_port_sfp1') == 'TRUE';
  var cb_peer_card_port_sfp2 = block.getFieldValue('peer_card_port_sfp2') == 'TRUE';
  var cb_peer_card_port_qsfp1 = block.getFieldValue('peer_card_port_qsfp1') == 'TRUE';
  var cb_peer_card_port_qsfp2 = block.getFieldValue('peer_card_port_qsfp2') == 'TRUE';
  // TODO: Assemble Python into code variable. 
  var peerClients ;
  if( (cb_peer_card_port_sfp1) && (cb_peer_card_port_sfp2) && (cb_peer_card_port_qsfp1) && (cb_peer_card_port_qsfp2) ){
  	peerClients = "-2&&-5";
  }else{

  }

  var code = "#Create opmode " + '\n';
  code = code + "print tl1.cmd('ent-opmode::slot-" + tv_create_slot + ":1:::opmode=" + opmodes[dd_card_create_opmode] + ",";
  code = code + "PEERSLOTS=SLOT-" + peerCardSlots[dd_card_create_peercard] + "&SLOT-" + skipPeerCardSlots[dd_card_create_skippeercard] + ",TRUNKPORTS=2,PEERCLIENTS=";
  code = code + peerCardSlots[dd_card_create_peercard] + peerClients + "&" + skipPeerCardSlots[dd_card_create_skippeercard] + peerClients + ";')" + '\n';
  code = code + "time.sleep(3)";
  return code + '\n' + '\n'; 
};




//ent-opmode::slot-1-6:C:::opmode=txp-10g,trunkports=2,clientports=1;

Blockly.Python['opmode_create'] = function(block) {
  var dd_card_type = block.getFieldValue('opmode_card');
  var checkbox_port_wse   = [];
  var checkbox_port_falco = [];
  
  if(dd_card_type == 'wse_id'){
    var text_card_create_node_wse         = block.getFieldValue('card_create_node_wse');
    var text_card_create_shelf_wse        = block.getFieldValue('card_create_shelf_wse');
    var text_card_create_slot_wse         = block.getFieldValue('card_create_slot_wse');
    var dropdown_card_create_opmode_wse   = block.getFieldValue('card_create_opmode_wse');
    checkbox_port_wse[0]                  = (block.getFieldValue('port1')  == 'TRUE');
    checkbox_port_wse[1]                  = (block.getFieldValue('port2')  == 'TRUE');
    checkbox_port_wse[2]                  = (block.getFieldValue('port3')  == 'TRUE');
    checkbox_port_wse[3]                  = (block.getFieldValue('port4')  == 'TRUE');
    checkbox_port_wse[4]                  = (block.getFieldValue('port5')  == 'TRUE');
    checkbox_port_wse[5]                  = (block.getFieldValue('port6')  == 'TRUE');
    checkbox_port_wse[6]                  = (block.getFieldValue('port7')  == 'TRUE');
    checkbox_port_wse[7]                  = (block.getFieldValue('port8')  == 'TRUE');
    checkbox_port_wse[8]                  = (block.getFieldValue('port9')  == 'TRUE');
    checkbox_port_wse[9]                  = (block.getFieldValue('port10') == 'TRUE');

    var i;
    var code = "#Create wse opmode " + '\n';
    for(i = 0; i < 9 ; i = i+2 ) {    
      if(checkbox_port_wse[i] || checkbox_port_wse[i+1] ){
        code = code + "print tl1_" +text_card_create_node_wse +".cmd('ent-opmode::slot-" + text_card_create_shelf_wse + "-" + text_card_create_slot_wse + ":c:::opmode=" + opmodes[dropdown_card_create_opmode_wse] + ","; 
        code = code + "trunkports=" + (i+2) + ",clientports=" + (i+1) + ";')" + "\n";
        code = code + "time.sleep(3)" + "\n";
      }
    }
    return code + '\n' + '\n'; 
  }else if(dd_card_type == 'falco_id'){
    var text_card_create_node_wse           = block.getFieldValue('card_create_node');
    var text_card_create_shelf              = block.getFieldValue('card_create_shelf');
    var text_card_create_slot               = block.getFieldValue('card_create_slot');
    var dropdown_card_create_opmode         = block.getFieldValue('card_create_opmode');
    var dropdown_card_create_peerCard       = block.getFieldValue('card_create_peerCard');
    var dropdown_card_create_skipPeercard   = block.getFieldValue('card_create_skipPeerCard');
    checkbox_port_falco[0]                  = (block.getFieldValue('peer_card_port_CPAK') == 'TRUE');
    checkbox_port_falco[1]                  = (block.getFieldValue('peer_card_port_sfp1') == 'TRUE');
    checkbox_port_falco[2]                  = (block.getFieldValue('peer_card_port_sfp2') == 'TRUE');
    checkbox_port_falco[3]                  = (block.getFieldValue('peer_card_port_qsfp1') == 'TRUE');
    checkbox_port_falco[4]                  = (block.getFieldValue('peer_card_port_qsfp2') == 'TRUE');


    var peerClients ;
    if( (checkbox_port_falco[1]) && (checkbox_port_falco[2]) && (checkbox_port_falco[3]) && (checkbox_port_falco[4]) ){
        peerClients = "-2&&-5";

    }else{
        peerClients = "-1";

    }
    var code = "#Create opmode " + '\n';
    code = code + "print tl1_" + card_create_node +".cmd('ent-opmode::slot-" + text_card_create_shelf + "-" + text_card_create_slot +":c:::opmode=" + opmodes[dropdown_card_create_opmode] + ",";
    code = code + "PEERSLOTS=SLOT-" + peerCardSlots[dropdown_card_create_peerCard] + "&SLOT-" + skipPeerCardSlots[dropdown_card_create_skipPeercard] + ",TRUNKPORTS=2,PEERCLIENTS=";
    code = code + peerCardSlots[dropdown_card_create_peerCard] + peerClients + "&" + skipPeerCardSlots[dropdown_card_create_skipPeercard] + peerClients + ";')" + '\n';
    code = code + "time.sleep(3)";
    return code + '\n' + '\n'; 
  }else{
    return "none"
  }
};