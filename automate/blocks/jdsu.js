Blockly.Blocks['jdsu'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("../media/images/Jdsu/jdsu.png", 80, 40, "*"))
        .appendField("Ip ")
        .appendField(new Blockly.FieldTextInput("10.64.109.230"), "jdsu_ip")
        .appendField("Slot ")
        .appendField(new Blockly.FieldTextInput("3"), "jdsu_slot")
        .appendField("Port ")
        .appendField(new Blockly.FieldTextInput("3"), "jdsu_port")
        .appendField("Payload")
        .appendField(new Blockly.FieldDropdown([["10_GIGE","10_GIGE_ID"], ["OC192","OC192_ID"], ["OTU2","OTU2_ID"]]), "jdsu_payload");
        this.appendDummyInput()
        .appendField("                       Test set Id")
        .appendField(new Blockly.FieldTextInput("1"), "jdsu id");
    this.setColour(290);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
 this.setTooltip("Please change test set id ,if using multiple testsets");
 this.setHelpUrl("http://www.google.com");
  }
};



Blockly.Blocks['jdsu_traffic'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("is")
        .appendField(new Blockly.FieldDropdown([["10_GIGE","10_GIGE_ID"], ["OC192","OC192_ID"], ["OTU2","OTU2_ID"]]), "jdsu_payload_traffic")
        .appendField("traffic up ");
    this.appendDummyInput()
        .appendField("Test set Id :")
        .appendField(new Blockly.FieldTextInput("1"), "jdsu_id");
    this.setOutput(true, null);
    this.setColour(290);
 this.setTooltip("Please select the correct test Id and paylaod type");
 this.setHelpUrl("");
  }
};


 //.appendField(new Blockly.FieldImage("/Users/ankmaury/Desktop/Learning/googleBlockly/blockly/media/images/Jdsu/jdsu.png", 80, 40, "*"))