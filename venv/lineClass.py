class line:
    def __init(self,lineId,custId,routId,lineNum):
        self.__lineId=lineId
        self.__custId=custId
        self.__routId=routId
        self.__lineNum=lineNum

    @property
    def lineId(self):
        return self.__lineId

    def custId(self):
        return self.__custId

    def routId(self):
        return self.__routId

    def lineNum(self):
        return self.__lineNum

    def __str__(self):
        print("lineId: "+self.__lineId+" custId: "+self.__custId+" routId: "+self.__routId+" lineNum: "+self.__lineNum)