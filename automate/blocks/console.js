Blockly.Blocks['console'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Send Console cmd :")
        .appendField(new Blockly.FieldTextInput("inetstatShow"), "console_cmd")
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("Send any console command");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['tl1'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Send TL1 cmd :")
        .appendField(new Blockly.FieldTextInput("rtrv-alm-all:::c::;"), "tl1_cmd")
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("Send any Tl1 command");
 this.setHelpUrl("");
  }
};


