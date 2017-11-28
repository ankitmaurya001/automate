

Blockly.Blocks['maintenance_loopback'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("NodeId:")
        .appendField(new Blockly.FieldTextInput("1"), "NodeId")
        .appendField("    Shelf:")
        .appendField(new Blockly.FieldTextInput("1"), "Shelf")
        .appendField("    Slot:")
        .appendField(new Blockly.FieldTextInput("1"), "maintenance_loopback_slot")
        .appendField("     Card:")
        .appendField(new Blockly.FieldDropdown([["MR-MXP","MR_MXP_ID"], ["WSE","WSE_ID"], ["200G-CK-LC","200G_CK_LC_ID"]]), "maintenance_loopback_card");
    this.appendDummyInput()
        .appendField("Port ")    
        .appendField("          ")
        .appendField("Payload ")    
        .appendField("        ")
        .appendField("Admin State")  
        .appendField("                     ")
        .appendField("Loopback Type")  
    this.appendDummyInput()
        .appendField(" ")
        .appendField(new Blockly.FieldTextInput("1"), "maintenance_port")
        .appendField("         ")
        .appendField(new Blockly.FieldDropdown([["TEN_GIGE","TEN_GIGE_ID"], ["OTU2","OTU2_ID"], ["OC192","OC192_ID"], ["OCH","OCH_ID"]]), "maintenance_loopback_payload")
        .appendField("           ")
        .appendField(new Blockly.FieldDropdown([["IS","IS_ID"], ["OOS,DSBLD","OOS_DSBLD_ID"], ["OOS,MT","OOS_MT_ID"], ["IS,AINS","IS_AINS_ID"],]), "maintenance_loopback_adminState")
        .appendField("                        ")
        .appendField(new Blockly.FieldDropdown([["None","lp_none_id"], ["Terminal (Inward)","lp_terminal_id"], ["Facility (Line)","lp_facility_id"]]), "loopbackType");
    this.setColour(160);
     this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};