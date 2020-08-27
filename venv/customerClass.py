class customer:
   #this class represents a person model
  def __init__(self,custNum,custId,custName,custLastName,custAdress,custCountry,lineArr):
      self.custNum=custNum
      self.__custId = custId
      self.__custName=custName
      self.__custLastName=custLastName
      self.__custAdress=custAdress
      self.__custCountry=custCountry
      self.__lineArr=lineArr


  @property
  def custNum(self):
      return self.__custNum
  @property
  def custId(self):
      return self.__custId

  @property
  def custName(self):
      return self.__custName
  @property
  def custLastName(self):
      return self.__custLastName

  @property
  def custAdress(self):
      return self.__custAdress

  @property
  def custCountry(self):
      return self.__custCountry

  @property
  def lineArr(self):
      return self.__lineArr

  def __str__(self):
      print("custNum: "+self.custNum+" custId: "+self.custId+" custName: "+self.custName+
           " custLastName: "+self.custLastName+ " custAdress:"+self.custAdress+" custCountry: "+self.custCountry+" lineArr: "+lineArr)






