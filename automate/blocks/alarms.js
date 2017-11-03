
//Synchronize block for getting the alarms.
Blockly.Blocks['alarms_synchronize'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("../media/images/Alarms/alarms_synchronize.png", 100, 50, "*"));
   this.setColour("#FFFFFF");
   this.setPreviousStatement(true, null);
   this.setNextStatement(true, null);
 this.setTooltip("Retrieve All Alarms");
 this.setHelpUrl("");
  }
};


//Filter the alarms.
Blockly.Blocks['alarms_filter'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("../media/images/Alarms/alarms_filter.png", 100, 50, "*"));
   this.setColour("#FFFFFF");
   this.setPreviousStatement(true, null);
   this.setNextStatement(true, null);
 this.setTooltip("Not implemented yet");
 this.setHelpUrl("");
  }
};



//Delete Cleared alarms.
Blockly.Blocks['alarms_deleteClearedAlarms'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("../media/images/Alarms/alarms_deleteClearedAlarms.png", 130, 80, "*"));
   this.setColour("#FFFFFF");
   this.setPreviousStatement(true, null);
   this.setNextStatement(true, null);
 this.setTooltip("Not implemented yet");
 this.setHelpUrl("");
  }
};