


Blockly.Blocks['node_details'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Node Ip: ")
        .appendField(new Blockly.FieldTextInput("10.64.106.188"), "node_details_ip")
        .appendField("Console ip :")
        .appendField(new Blockly.FieldTextInput("10.64.108.202"), "console_ip")
        .appendField("   port  ")
        .appendField(new Blockly.FieldTextInput("2013"), "console_port");
    this.setColour(330);
    this.setPreviousStatement(true, null);
   this.setNextStatement(true, null);
 this.setTooltip("Enter Nope ip and Console , Leave unchanged if not using");
 this.setHelpUrl("");
  }
};