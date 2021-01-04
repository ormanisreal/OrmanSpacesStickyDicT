from orman import OrmanNameSpace
import threading,os, sys

def disablePrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

class OrmanStickyDicT(object):
    def __init__(self, sticky_name):
        self.stickies = []
        self.sticky_name = sticky_name
        self.ONS = OrmanNameSpace()
        NS = self.ONS.ns()
        self.ns = NS
        if "stickies" not in NS:
            NS["stickies"] = dict()
        if sticky_name not in NS["stickies"]:
            NS["stickies"][sticky_name] = dict()
        self._Dict = NS["stickies"][sticky_name]
        
    @property
    def Dict(self):
        return self._Dict

    @Dict.setter
    def Dict(self, value):
        self._Dict = value
        for callback in self.stickies:
            callback( self._Dict )
        xT = threading.Thread( 
            target=self.update_space, 
            args=(
                self.sticky_name, 
                self.Dict
            ) 
        )
        xT.start()

    def stick_it(self, callback):
        self.stickies.append(callback)

    def update_space(self, sticky_name, sticky_dict):
        disablePrint()
        print( "Sticky dict %s just changed, saving..." % (sticky_name) )
        self.ns["stickies"][sticky_name] = sticky_dict
        
        self.ONS.save( self.ONS.sync( self.ns ) )
        enablePrint()
        
class Dict(object):
    def __init__(self, space):
        self.space = space
        self.stickiness = self.space.Dict
        space.stick_it( self.update_sticky )
        
    def update_sticky(self, Dict):
        self.ns = Dict

def Sticky(sticky_name):
    SD = OrmanStickyDicT(sticky_name)
    D = Dict(SD)
    return SD


