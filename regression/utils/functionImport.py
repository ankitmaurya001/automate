from functools import partial
from jdsu import Jdsu
def testQuery(firstArg,secondArg):
    print firstArg,secondArg
    
class testClass:
    def __init__(self):
        pass
    def testQuery(self,firstArg,secondArg):
        print firstArg,secondArg
    
def loadFunctions(className,baseFunction= "testQuery",functionFile = "jdsu.json"):
     """ add functions to the Jdsu object on the fly"""
     import json
     funData =json.load(open(functionFile,'r'))
     #print funData
     print funData["commandList"].keys()
     for (fun,cmd) in funData["commandList"].items():
         myFun = partial(getattr(className,baseFunction),cmd.encode("ascii","ignore"))
         setattr(className,fun,myFun)
         
     
if __name__ == "__main__":
   # loadFunctions(testClass)
    #testClass.test("silly")
    testObj = Jdsu("10.64.109.230",2,1)
#    testObj = testClass()
    loadFunctions(testObj,"query")
    testObj.identifyMe()
#    jd = Jdsu("10.64.109.65",3,1)
#    loadFunctions(jd,"query")   
#    print jd.identifyMe()