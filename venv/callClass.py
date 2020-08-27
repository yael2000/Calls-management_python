class call:
    countCalls=0
    def __init__(self,callId,startDate,finishDate,outgoingCall,incomingCall):
        call.countCalls+=1
        self.__callId=callId
        self.__startDate=startDate
        self.__finishDate=finishDate
        self.__outgoingCall=outgoingCall
        self.__incomingCall=incomingCall

    @property
    def callId(self):
        return self.__callId

    @property
    def startDate(self):
        return self.__startDate

    @property
    def finishDate(self):
        return self.__finishDate

    @property
    def outgoingCall(self):
        return self.__outgoingCall

    @property
    def incomingCall(self):
        return self.__incomingCall

    def __str__(self):
       return (  "callId: " + self.callId + " startDate: " + str(self.startDate) + " finishDate: " + str(self.finishDate) + " outgoingCall: " + self.outgoingCall+" incomingCall: "+self.incomingCall)

    def __eq__(self,other):
         if isinstance(other,call):
             print(self.finishDate-self.startDate)
             if (self.finishDate-self.startDate)==(other.finishDate-other.startDate):
                 return True
             else:
                 return False

    def __ne__(self, other):
         if isinstance(other,call):
             if (self.finishDate-self.startDate)!=(other.finishDate-other.startDate):
                 return True
             else:
                 return False




