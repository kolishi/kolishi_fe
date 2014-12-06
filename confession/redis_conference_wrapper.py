from .  import Redis_connection_pool as RS

def AddNumberToRedis(FromNumber,ToNumber):
    RS.set("FirstNumber",(FromNumber,ToNumber))
class ConferenceStatus:
    def __init__(self):
        self.ready = False
        self.FromNumber1 = 0
        self.FromNumber2 = 1
        self.ToNumber1 = 0
        self.ToNumber2 = 1
    def addNumbes(self,FromNum1,ToNum1,FromNum2,ToNum2):
        self.FromNumber1 = FromNum1
        self.ToNumber1 = ToNum1
        self.FromNumber2 = FromNum2
        self.ToNumber2 = ToNum2
        self.ready =True

def AddNumberAndGetPair(NewNumberFrom,NewNumberTo):
    OldNumTuple = RS.get("FirstNumber")

    if OldNumTuple is None : # If this is the first number
        AddNumberToRedis((NewNumberFrom,NewNumberTo))
        return ConferenceStatus()
    else:
        C = ConferenceStatus()
        C.addNumbes(*(NewNumberFrom,NewNumberTo),*OldNumTuple)
        RS.delete("FirstNumber")
        return C

