Blockly.Blocks['console'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Send Console cmd :")
        .appendField(new Blockly.FieldTextInput("inetstatShow"), "console_cmd")
        .appendField("  expect ")
        .appendField(new Blockly.FieldDropdown([["->","console_arrow_id"], ["#","console_hash_id"], ["=>","console_uboot_id"]]), "console_expect")
        .appendField("  prompt ")
        .appendField("   Id ")
        .appendField(new Blockly.FieldTextInput("1"), "console_id");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("Send any console command, Please match the ID ");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['telnet'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Send Telnet cmd :")
        .appendField(new Blockly.FieldTextInput("dumpTime()"), "telnet_cmd")
        .appendField("  expect ")
        .appendField(new Blockly.FieldDropdown([["->","telnet_arrow_id"], ["#","telnet_hash_id"], ["=>","telnet_uboot_id"]]), "telnet_expect")
        .appendField("  prompt ")
        .appendField("   Id ")
        .appendField(new Blockly.FieldTextInput("1"), "telnet_id");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("Send any Tl1 command, Please match the ID");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['tl1'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Send TL1 cmd :")
        .appendField(new Blockly.FieldTextInput("rtrv-alm-all:::c::;"), "tl1_cmd")
        .appendField("  expect ")
        .appendField(new Blockly.FieldDropdown([[">","tl1_carrot_id"], ["#","tl1_hash_id"], ["=>","tl1_uboot_id"]]), "tl1_expect")
        .appendField("  prompt ")
        .appendField("   Id ")
        .appendField(new Blockly.FieldTextInput("1"), "tl1_id");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("Send any Tl1 command, Please match the ID");
 this.setHelpUrl("");
  }
};


