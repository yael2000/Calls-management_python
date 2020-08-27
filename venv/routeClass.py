class route:
    def __init__(self,roureId,routeName,rountPrice,minutesIsrael,minutesAbroad):
        self.__roureId=roureId
        self.__routeName=routeName
        self.__rountPrice=rountPrice
        self.__minutesIsrael=minutesIsrael
        self.__minutesAbroad=minutesAbroad

    @property
    def roureId(self):
        return  self.__roureId
    @property
    def routeName(self):
        return  self.__routeName
    @property
    def rountPrice(self):
        return  self.__rountPrice
    @property
    def minutesIsrael(self):
        return  self.__minutesIsrael
    @property
    def minutesAbroad(self):
        return  self.__minutesAbroad

    def __str__(self):
        print("roureId: " + self.__roureId + "routeName: " + self.__routeName + "rountPrice: " + self.__rountPrice," minutesIsrael: "+self.__minutesIsrael+" minutesAbroad: "+self.__minutesAbroad)
