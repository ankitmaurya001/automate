Blockly.Blocks['time'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Sleep")
        .appendField(new Blockly.FieldTextInput("3"), "sleep_sec")
        .appendField("secs");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(290);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};