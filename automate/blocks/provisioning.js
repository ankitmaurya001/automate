
//Create ppm
Blockly.Blocks['provisioning_ppm_createppm'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("            ")
        .appendField(new Blockly.FieldImage("../media/images/Provisioning/PluggablePortModules/pluggablePortModules_createPPM.png", 80, 40, "*"));
    this.appendDummyInput()
        .appendField("Slot  ")
        .appendField(new Blockly.FieldTextInput("1"), "NAME")
        .appendField(" Card")
        .appendField(new Blockly.FieldDropdown([["MR-MXP","MR-MXP_ID"], ["WSE","WSE_ID"], ["200G-CK-LC","200G-CK-LC_ID"]]), "provisioning_ppm_createPPM_card");
    this.appendDummyInput()
        .appendField("PPM ")
        .appendField(new Blockly.FieldTextInput("1"), "ppmNo");

    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(260);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};



//Create payload 
Blockly.Blocks['provisioning_ppm_createpayload'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("             ")
        .appendField(new Blockly.FieldImage("../media/images/Provisioning/PluggablePortModules/pluggablePortModules_createPort.png", 80, 40, "*"));
    this.appendDummyInput()
        .appendField("Slot  ")
        .appendField(new Blockly.FieldTextInput("1"), "SlotName")
        .appendField(" Card")
        .appendField(new Blockly.FieldDropdown([["MR-MXP","MR-MXP_ID"], ["WSE","WSE_ID"], ["200G-CK-LC","200G-CK-LC_ID"]]), "provisioning_ppm_createpayload_card");
    this.appendDummyInput()
        .appendField("Port  ")
        .appendField(new Blockly.FieldTextInput("1"), "ppmNo")
        .appendField("Port Type ")
        .appendField(new Blockly.FieldDropdown([["TEN_GE","TEN_GE_ID"], ["OC192","OC192_ID"], ["OTU2","OTU2_ID"]]), "provisioning_ppm_createpayload_payload");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(260);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};



//Create opmode
Blockly.Blocks['card_create'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("                        ")
        .appendField(new Blockly.FieldImage("../media/images/Provisioning/Card/createOpmode.png", 120, 60, "*"));
    this.appendDummyInput()
        .appendField("Shelf ")
        .appendField(new Blockly.FieldTextInput("1"), "card_create_shelf")
        .appendField("   Slot ")
        .appendField(new Blockly.FieldTextInput("1"), "card_create_slot")
        .appendField(" Card Configurtion :")
        .appendField(new Blockly.FieldDropdown([["TXP-100G","TXP_100G_opmode"], ["RGN-100G","RGN_100G_opmode"], ["MXP-200G","MXP_200G_opmode"]]), "card_create_opmode");
    this.appendDummyInput()
        .appendField("Peer Card :")
        .appendField("Slot")
        .appendField(new Blockly.FieldDropdown([["N/A","N/A_peerCard"], ["1","1_peerCard"], ["2","2_peerCard"], ["3","3_peerCard"], ["4","4_peerCard"], ["5","5_peerCard"], ["6","6_peerCard"], ["7","7_peerCard"], ["8","8_peerCard"], ["9","9_peerCard"], ["10","10_peerCard"], ["11","11_peerCard"], ["12","12_peerCard"], ["13","13_peerCard"], ["14","14_peerCard"], ["15","15_peerCard"]] ), "card_create_peerCard")
        .appendField("            Skip Peer Card :")
        .appendField("Slot")
        .appendField(new Blockly.FieldDropdown([["N/A","N/A_skipPeerCard"], ["1","1_skipPeerCard"], ["2","2_skipPeerCard"], ["3","3_skipPeerCard"], ["4","4_skipPeerCard"], ["5","5_skipPeerCard"], ["6","6_skipPeerCard"], ["7","7_skipPeerCard"], ["8","8_skipPeerCard"], ["9","9_skipPeerCard"], ["10","10_skipPeerCard"], ["11","11_skipPeerCard"], ["12","12_skipPeerCard"], ["13","13_skipPeerCard"], ["14","14_skipPeerCard"], ["15","15_skipPeerCard"]]), "card_create_skipPeerCard");
    this.appendDummyInput()
        .appendField("Peer Card Ports  :  CPAK ")
        .appendField(new Blockly.FieldCheckbox("FALSE"), "peer_card_port_CPAK")
        .appendField("  2")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "peer_card_port_sfp1")
        .appendField("  3")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "peer_card_port_sfp2")
        .appendField("     4")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "peer_card_port_qsfp1")
        .appendField("     5")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "peer_card_port_qsfp2");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(260);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};




