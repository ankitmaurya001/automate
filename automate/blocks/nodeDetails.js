


Blockly.Blocks['node_details'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("TL1 - Node Ip: ")
        .appendField(new Blockly.FieldTextInput("10.64.106.188"), "node_details_ip")
        .appendField("User Name: ")
        .appendField(new Blockly.FieldTextInput("CISCO15"), "node_user_name")
        .appendField("  Pwd: ")
        .appendField(new Blockly.FieldTextInput("otbu+1"), "node_pwd")
        .appendField("   Id ")
        .appendField(new Blockly.FieldTextInput("1"), "node_id");
    this.setColour(330);
    this.setPreviousStatement(true, null);
   this.setNextStatement(true, null);
 this.setTooltip("Enter Nope ip , Leave unchanged if not using");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['console_details'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Console ip :")
        .appendField(new Blockly.FieldTextInput("10.64.108.202"), "console_ip")
        .appendField("   port  ")
        .appendField(new Blockly.FieldTextInput("2013"), "console_port")
        .appendField("   Id ")
        .appendField(new Blockly.FieldTextInput("1"), "console_id");
    this.setColour(330);
    this.setPreviousStatement(true, null);
   this.setNextStatement(true, null);
 this.setTooltip("Enter Console details, Leave unchanged if not using");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['telnet_details'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Telnet ip :")
        .appendField(new Blockly.FieldTextInput("10.64.106.188"), "telnet_ip")
        .appendField("   port  ")
        .appendField(new Blockly.FieldTextInput("2002"), "telnet_port")
        .appendField("   Id ")
        .appendField(new Blockly.FieldTextInput("1"), "telnet_id");
    this.setColour(330);
    this.setPreviousStatement(true, null);
   this.setNextStatement(true, null);
 this.setTooltip("Enter telnet details, Leave unchanged if not using");
 this.setHelpUrl("");
  }
};