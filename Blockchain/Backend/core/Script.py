class Script:
    def __init__(self, cmds = None):
        if cmds is None:
            self.cmds = []
        else:
            self.cmds = cmds
            
    @classmethod
    def p2pkh_script(cls, h160):
        #Take a hash160 and return the p2pkh ScriptPubKey
        return Script([0x76, 0xa9, h160, 0x88, 0xac])