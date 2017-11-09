#! /usr/bin/env python


class Falco:
    def __init__(self, console):
        self.console = console

    def getDigiOpMode(self):
        digi= self.console.cmd('adpt_get_devid()')
        self.digiMode = self.cmdParse(digi)
    

    def getAtlanteMode(self):
        self.atlante = self.console.cmd('TpDrv "cg list"')
        self.cmdParse(self.atlante)

    def cmdParse(self,cmdOutput):
        import re
        result = re.search("value = (-?\d+)",cmdOutput)
        return result.group(1)

if __name__ == "__main__":
    import vxPython
    import myCfg
    c = myCfg.myCfg()
    nodeip = c.get("node","ip")
    slot = c.get("node","slot")
    port = '200' +slot   
    t = vxPython.vxConsole(nodeip,port)
    fal = Falco(t)
    fal.getDigiOpMode()
    fal.getAtlanteMode()
    
