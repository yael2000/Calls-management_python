import pyodbc
import datetime
from callClass import call
from customerClass import customer
from lineClass import line
from routeClass import route

database="RouterDB_Python"
server="DESKTOP-2S5DPSD"
connection=pyodbc.connect('DRIVER={SQL Server};SERVER='+server+'; DATABASE='+database)
cursor=connection.cursor()

# 1 יצירת שיחה חדשה:
#(צריך לעשות בדיקה שאם המפר לא קיים להוסיף אותו לרוטר??? ואם קיים לא?? )
def createNewCall():
    custNum = input("enter customer num: (1-4)")
    startDate = input("enter start date in format: hh:mm:ss")
    finishDate = input("enter finsh date in format: hh:mm:ss")
    outgoingCall = input("enter out going call")
    incomingCall = input("enter in coming call")
    router = input("choose router 100/101/102")

    count1 = cursor.execute("insert Line_tbl(CustNum,routeId,lineNum)values(?,?,?)", custNum, router,
                           outgoingCall).rowcount
    count = cursor.execute(" INSERT into Call_tbl( startDate, finishDate, outgoingCall, incomingCall) "
                           "VALUES ( ?,?,?,?)", startDate, finishDate, outgoingCall, incomingCall).rowcount
    print(count)
    print("row add")


##########################
# יצירת לקוח חדש-קליטה מהמשתמש
# custID=input("enter Cust ID")
# custName=input("enter CustName")
# custLastName=input("enter CustLastName")
# custAddress=input("enter CustAddress")
# custCountry=input("enter CustCountry")
# print('custName')
# count=cursor.execute(" INSERT into Customer_tbl(  CustID, CustName, CustLastName, CustAddress, CustCountry) "
#                      "VALUES (?,?,?,?,?)",custID,custName, custLastName, custAddress, custCountry).rowcount
# print(count)
# print("row add")
################################
# //הוספת לקוח
# count=cursor.execute(" INSERT into Customer_tbl(  CustID, CustName, CustLastName, CustAddress, CustCountry) "
#                      "VALUES (  '987654','gila', 'frid', 'ramat gan', 'israel')").rowcount
# print(count)
# print("row add")
#########################
#2 הצגת כל השיחות של לקוח לפי מס' טלפון
def displayCallsByPhone():
    phone = input("enter phone number to searh all the calls:")
    cursor.execute("select * from [dbo].[Call_tbl] where [outgoingCall]=? or [incomingCall]=? ", phone, phone)
    all = cursor.fetchall()
    print(all)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

#############################
#3 הצגת הסכום לתשלום של לקוח לכל הקווים שלו לפי ת.ז
def displayPay():
    custIdToSumPrice = input("enter cust id to calculate the price:")
    cursor.execute(
        "select  sum(DATEDIFF(MINUTE,[startDate] ,[finishDate])/60*r.rountPrice) from [dbo].[Call_tbl]c join [dbo].[Line_tbl]l on c.outgoingCall=l.lineNum join  [dbo].[Route_tbl]r on r.routeId=l.routeId where l.CustNum=?",
        custIdToSumPrice)
    p = cursor.fetchone()
    print("customer" + str(custIdToSumPrice) + "has to pay: " + str(p) + " $")


#4 בדיקת מס' הקווים לכל מסלול:
def showLinesOfRouter():
    cursor.execute("select [routeId] ,count([lineId]) from [dbo].[Line_tbl] group by [routeId]")
    all = cursor.fetchall()
    print("get the number of lines per route: ")
    print(all)

#5 בדיקה אם לקוח חרג ממספר הדקות המותר
def ExceptionCheck():
    custnum=input("enter customer num to check if it has exceeded the allowed number of minutes")
    cursor.execute(
        "select l.[CustNum], sum(DATEDIFF(MINUTE,[startDate] ,[finishDate])) as summinutes from [Call_tbl]c "
        "join [Line_tbl]l on c.outgoingCall=l.lineNum join  [Route_tbl]r on r.routeId=l.routeId "
        "where (DATEDIFF(MINUTE,[startDate] ,[finishDate])) >[minutesAbroad] and [CustNum]=? group by l.[CustNum]",custnum)
    all = cursor.fetchall();

    if all == []:
        print("The customer did not exceed the allowed number of minutes")
    else:
        print("The customer exceed the allowed number of minutes")
# סעיף ג: השוואת שני שיחות###################
# c1=call("120",datetime.datetime(2020,5,7,10,10,0),datetime.datetime(2020,5,7,12,50,0),'0524666625','0546294086')
# c2=call("121",datetime.datetime(2020,5,7,22,5,0),datetime.datetime(2020,5,7,22,5,0),'0546256256','0505465556')
# print("Is the duration of the calls equal? ")
# print(c1==c2)
# print("Is the duration of the calls not equal? ")
# print(c1!=c2)

# סעיף ו עדכון מחיר מסלול שקטן מ30################
# count=cursor.execute("UPDATE Route_tbl  SET rountPrice=rountPrice*1.05 WHERE rountPrice<30").rowcount
# print(str(count) +"rows updated- router is less then 30")

# סעיף ו מחיקת שיחות לפי מספר טלפון30################
# lineDelete=input("enter phone line to delete:")
# count=cursor.execute("DELETE FROM Call_tbl WHERE outgoingCall=?",lineDelete).rowcount
# print(str(count)+"rows deleted")
