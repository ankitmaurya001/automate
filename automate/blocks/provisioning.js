

'use strict';
goog.provide('Blockly.Constants.Provisioning');

goog.require('Blockly.Blocks');

//Create ppm
Blockly.Blocks['provisioning_ppm_createppm'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("            ")
        .appendField(new Blockly.FieldImage("../media/images/Provisioning/PluggablePortModules/pluggablePortModules_createPPM.png", 80, 40, "*"));
    this.appendDummyInput()
        .appendField("NodeId:")
        .appendField(new Blockly.FieldTextInput("1"), "NodeId")
        .appendField("  Shelf:")
        .appendField(new Blockly.FieldTextInput("1"), "Shelf")
        .appendField("  Slot:")
        .appendField(new Blockly.FieldTextInput("1"), "NAME")
        .appendField("  Card:")
        .appendField(new Blockly.FieldDropdown([["MR-MXP","MR-MXP_ID"], ["WSE","WSE_ID"], ["200G-CK-LC","200G-CK-LC_ID"]]), "provisioning_ppm_createPPM_card");
    this.appendDummyInput()
        .appendField("PPM:    ")
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
        .appendField("NodeId:")
        .appendField(new Blockly.FieldTextInput("1"), "NodeId")
        .appendField("  Shelf:")
        .appendField(new Blockly.FieldTextInput("1"), "Shelf")
        .appendField("  Slot:")
        .appendField(new Blockly.FieldTextInput("1"), "SlotName")
        .appendField("  Card:")
        .appendField(new Blockly.FieldDropdown([["MR-MXP","MR-MXP_ID"], ["WSE","WSE_ID"], ["200G-CK-LC","200G-CK-LC_ID"]]), "provisioning_ppm_createpayload_card");
    this.appendDummyInput()
        .appendField("Port:     ")
        .appendField(new Blockly.FieldTextInput("1"), "ppmNo")
        .appendField("  Port Type: ")
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




Blockly.defineBlocksWithJsonArray([  // BEGIN JSON EXTRACT
{
  "type": "opmode_create",
  "message0": "     %1 %2      Card :  %3",
  "args0": [
    {
      "type": "field_image",
      "src": "../media/images/Provisioning/Card/createOpmode.png",
      "width": 120,
      "height": 60,
      "alt": "*"
    },
    {
      "type": "input_dummy"
    },
    {
      "type": "field_dropdown",
      "name": "opmode_card",
      "options": [
        [
          "Choose Card",
          "none_id"
        ],
        [
          "WSE",
          "wse_id"
        ],
        [
          "Falco",
          "falco_id"
        ]
      ]
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 260,
  "tooltip": "",
  "helpUrl": "",
  "mutator": "opmode_create_mutator"
},

{
  "type": "math_number_property_multiple",
  "message0": "%1 %2 %3",
  "args0": [
    {
      "type": "input_value",
      "name": "NUMBER_TO_CHECK",
      "check": "Number"
    },
    {
      "type": "field_dropdown",
      "name": "PROPERTY1",
      "options": [
        [
          "even",
          "EVEN_ID"
        ],
        [
          "odd",
          "ODD_ID"
        ],
        [
          "divisible by",
          "DIVISIBLE_BY_ID"
        ]
      ]
    },
    {
      "type": "input_value",
      "name": "NAME"
    }
  ],
  "colour": 230,
  "tooltip": "",
  "helpUrl": "",
  "mutator": "math_is_divisibleby_mutator_multiple"
}
]);  // END JSON EXTRACT (Do not delete this comment.)




Blockly.Constants.Provisioning.IS_DIVISIBLEBY_MUTATOR_MULTIPLE_MIXIN = {
  /**
   * Create XML to represent whether the 'divisorInput' should be present.
   * @return {Element} XML storage element.
   * @this Blockly.Block
   */
  mutationToDom: function() {
    var container = document.createElement('mutation');
    var divisorInput = (this.getFieldValue('PROPERTY1') == 'DIVISIBLE_BY_ID');
    container.setAttribute('divisor_input', divisorInput);
    return container;
  },
  /**
   * Parse XML to restore the 'divisorInput'.
   * @param {!Element} xmlElement XML storage element.
   * @this Blockly.Block
   */
  domToMutation: function(xmlElement) {
    var divisorInput = (xmlElement.getAttribute('divisor_input') == 'true');
    this.updateShape_(divisorInput);
  },
  /**
   * Modify this block to have (or not have) an input for 'is divisible by'.
   * @param {boolean} divisorInput True if this block has a divisor input.
   * @private
   * @this Blockly.Block
   */
   updateShape_: function(divisorInput) {
    // Add or remove a Value Input.
    var inputExists = this.getInput('DIVISOR');
    if (divisorInput) {
      if (!inputExists) {
        this.appendValueInput('DIVISOR')
            .appendField(new Blockly.FieldImage("../media/images/Provisioning/Card/createOpmode.png", 120, 60, "*"))
            .appendField("Shelf ")
        this.appendValueInput('DIVISOR1')
            .appendField(new Blockly.FieldTextInput("1"), "card_create_shelf")
            .appendField("Shelf1 ")
            .appendField(new Blockly.FieldTextInput("2"), "card_create_shelf1");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
           
      }
    } else if (inputExists) {
      this.removeInput('DIVISOR');
      this.removeInput('DIVISOR1');
    }
  }
};

/**
 * 'math_is_divisibleby_mutator' extension to the 'math_property' block that
 * can update the block shape (add/remove divisor input) based on whether
 * property is "divisble by".
 * @this Blockly.Block
 * @package
 */
Blockly.Constants.Provisioning.IS_DIVISIBLE_MUTATOR_MULTIPLE_EXTENSION = function() {
  this.getField('PROPERTY1').setValidator(function(option) {
    var divisorInput = (option == 'DIVISIBLE_BY_ID');
    console.log(option)
    this.sourceBlock_.updateShape_(divisorInput);
  });
};



Blockly.Extensions.registerMutator('math_is_divisibleby_mutator_multiple',
  Blockly.Constants.Provisioning.IS_DIVISIBLEBY_MUTATOR_MULTIPLE_MIXIN,
  Blockly.Constants.Provisioning.IS_DIVISIBLE_MUTATOR_MULTIPLE_EXTENSION);



Blockly.Constants.Provisioning.OPMODE_CREATE_MUTATOR_MUMIXIN = {
  /**
   * Create XML to represent which card create opmode data should be present should be present.
   * @return {Element} XML storage element.
   * @this Blockly.Block
   */
  mutationToDom: function() {
    var container = document.createElement('mutation');
    var cardInput = ((this.getFieldValue('opmode_card') == 'falco_id') || (this.getFieldValue('opmode_card') == 'wse_id'))
    container.setAttribute('card_input', cardInput);
    return container;
  },
  /**
   * Parse XML to restore the 'divisorInput'.
   * @param {!Element} xmlElement XML storage element.
   * @this Blockly.Block
   */
  domToMutation: function(xmlElement) {
    var cardInput = (xmlElement.getAttribute('card_input') == 'true');
    this.updateShape_(cardInput);
  },
  /**
   * Modify this block according to the card type.
   * @private
   * @this Blockly.Block
   */
   updateShape_: function(cardInput) {
        // Add or remove a Value Input.
        var wse1    = this.getInput('WSE1');
        var wse2    = this.getInput('WSE2');
        var falco1  = this.getInput('FALCO1');
        var falco2  = this.getInput('FALCO2');
        var falco3  = this.getInput('FALCO3');

        //clear all
        if(wse1 || wse2){
            // getting console error , don't know why
           //     this.removeInput('WSE1');
            //    this.removeInput('WSE2');
        }
        if(falco1 || falco2 || falco3){
            //    this.removeInput('FALCO1');
            //    this.removeInput('FALCO2');
            //    this.removeInput('FALCO3');
        } 
     
        if(cardInput == "none_id"){
            console.log(cardInput)
            if(wse1 || wse2){
                this.removeInput('WSE1');
                this.removeInput('WSE2');
            }
            if(falco1 || falco2 || falco3){
                this.removeInput('FALCO1');
                this.removeInput('FALCO2');
                this.removeInput('FALCO3');
            }    
        
        }else if(cardInput == "wse_id"){   
                if(wse1 || wse2){
                    this.removeInput('WSE1');
                    this.removeInput('WSE2');
                } 
                if(falco1 || falco2 || falco3){
                this.removeInput('FALCO1');
                this.removeInput('FALCO2');
                this.removeInput('FALCO3');
                }     
                this.appendValueInput('WSE1')
                    .appendField("NodeId:")
                    .appendField(new Blockly.FieldTextInput("1"), "card_create_node_wse")
                    .appendField("  Shelf:")
                    .appendField(new Blockly.FieldTextInput("1"), "card_create_shelf_wse")
                    .appendField("  Slot:")
                    .appendField(new Blockly.FieldTextInput("1"), "card_create_slot_wse")
                    .appendField("      Card Configuration :")
                    .appendField(new Blockly.FieldDropdown([["TXP-10G","TXP_10G_opmode"], ["RGN-10G","RGN_10G_opmode"]]), "card_create_opmode_wse")
                    .appendField("  Peer Card :")
                    .appendField(new Blockly.FieldDropdown([["N/A","N/A_peerCard"]]), "card_create_peerCard_wse");
                this.appendValueInput('WSE2')
                    .appendField("Card Configuration Dialog:")
                    .appendField(" 1")
                    .appendField(new Blockly.FieldCheckbox("FALSE"), "port1")
                    .appendField("  2")
                    .appendField(new Blockly.FieldCheckbox("FALSE"), "port2")
                    .appendField("  3")
                    .appendField(new Blockly.FieldCheckbox("FALSE"), "port3")
                    .appendField("  4")
                    .appendField(new Blockly.FieldCheckbox("FLASE"), "port4")
                    .appendField("  5")
                    .appendField(new Blockly.FieldCheckbox("FLASE"), "port5")
                    .appendField("  6")
                    .appendField(new Blockly.FieldCheckbox("FALSE"), "port6")
                    .appendField("  7")
                    .appendField(new Blockly.FieldCheckbox("FALSE"), "port7")
                    .appendField("  8")
                    .appendField(new Blockly.FieldCheckbox("FALSE"), "port8")
                    .appendField("  9")
                    .appendField(new Blockly.FieldCheckbox("FLASE"), "port9")
                    .appendField("  10")
                    .appendField(new Blockly.FieldCheckbox("FLASE"), "port10");
        }else if(cardInput == "falco_id"){

                if(falco1 || falco2 || falco3){
                    this.removeInput('FALCO1');
                    this.removeInput('FALCO2');
                    this.removeInput('FALCO3');
                } 
                if(wse1 || wse2){
                    this.removeInput('WSE1');
                    this.removeInput('WSE2');
                }  
          
                this.appendValueInput('FALCO1')
                    .appendField("NodeId:")
                    .appendField(new Blockly.FieldTextInput("1"), "card_create_node")
                    .appendField("   Shelf:")
                    .appendField(new Blockly.FieldTextInput("1"), "card_create_shelf")
                    .appendField("   Slot:")
                    .appendField(new Blockly.FieldTextInput("1"), "card_create_slot")
                    .appendField("      Card Configurtion :")
                    .appendField(new Blockly.FieldDropdown([["TXP-100G","TXP_100G_opmode"], ["RGN-100G","RGN_100G_opmode"], ["MXP-200G","MXP_200G_opmode"]]), "card_create_opmode");
                this.appendValueInput('FALCO2')
                    .appendField("Peer Card :")
                    .appendField("Slot")
                    .appendField(new Blockly.FieldDropdown([["N/A","N/A_peerCard"], ["1","1_peerCard"], ["2","2_peerCard"], ["3","3_peerCard"], ["4","4_peerCard"], ["5","5_peerCard"], ["6","6_peerCard"], ["7","7_peerCard"], ["8","8_peerCard"], ["9","9_peerCard"], ["10","10_peerCard"], ["11","11_peerCard"], ["12","12_peerCard"], ["13","13_peerCard"], ["14","14_peerCard"], ["15","15_peerCard"]] ), "card_create_peerCard")
                    .appendField("            Skip Peer Card :")
                    .appendField("Slot")
                    .appendField(new Blockly.FieldDropdown([["N/A","N/A_skipPeerCard"], ["1","1_skipPeerCard"], ["2","2_skipPeerCard"], ["3","3_skipPeerCard"], ["4","4_skipPeerCard"], ["5","5_skipPeerCard"], ["6","6_skipPeerCard"], ["7","7_skipPeerCard"], ["8","8_skipPeerCard"], ["9","9_skipPeerCard"], ["10","10_skipPeerCard"], ["11","11_skipPeerCard"], ["12","12_skipPeerCard"], ["13","13_skipPeerCard"], ["14","14_skipPeerCard"], ["15","15_skipPeerCard"]]), "card_create_skipPeerCard");
                this.appendValueInput('FALCO3')
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
            }
    }   
};

/**
 * update the block shape based on card type.
 * property is "divisble by".
 * @this Blockly.Block
 * @package
 */
Blockly.Constants.Provisioning.OPMODE_CREATE_MUTATOR_EXTENSION= function() {
  this.getField('opmode_card').setValidator(function(option) {
    var cardInput = option ;
    console.log(option)
    this.sourceBlock_.updateShape_(cardInput);
  });
};




Blockly.Extensions.registerMutator('opmode_create_mutator',
  Blockly.Constants.Provisioning.OPMODE_CREATE_MUTATOR_MUMIXIN,
  Blockly.Constants.Provisioning.OPMODE_CREATE_MUTATOR_EXTENSION);









