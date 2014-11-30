from .  import Redis_connection_pool as RS

def AddNumberToRedis(Number):
    RS.set("FirstNumber",Number)
class ConferenceStatus:
    def __init__(self):
        self.ready = False
        self.Number1 = 0
        self.Number2 = 1
    def addNumbes(self,Num1,Num2):
        self.Number1 = Num1
        self.Number2 = Num2
        self.ready =True

def AddNumberAndGetPair(NewNumber):
    Num = RS.get("FirstNumber")

    if Num is None : # If this is the first number
        AddNumberToRedis(NewNumber)
        return ConferenceStatus()
    else:
        C = ConferenceStatus()
        C.addNumbes(Num,NewNumber)
        RS.delete("FirstNumber")
        return C

