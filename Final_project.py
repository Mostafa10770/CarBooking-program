from Project import Location
from Project import Client
from Project import Car
from Project import Driver
from Project import Wallet
from Project import Ride
import datetime
timestamp = datetime.datetime.now()

client_locat1 = Location(10,15)
client_locat2 = Location(20,40)
client_locat3 = Location(5,30)

client1=Client("Ahmed","Smouha     ",1231232213, () , 0)
client2=Client("Mohamed","Sidibeshr",4534535   , () , 0)
client3=Client("samir","sporting   ",7897987   , () , 0)
client1.loc=Location(10,15)
client2.loc=Location(20,40)
client3.loc=Location(15,30)
client1.wallet=Wallet(1000)
client2.wallet=Wallet(500)
client3.wallet=Wallet(700)
oclient1=client1.wallet
oclient2=client2.wallet
oclient3=client3.wallet

driver2=Driver("Karim  ","Abu-Kir   ",88888888  , 0.15 ,0)
driver1=Driver("Samy   ","Clepatra  ",77777777  , 0.1  ,0)
driver3=Driver("Hay    ","Alex      ",99999999  , 0.05 ,0)
driver4=Driver("Fouad  ","Alex      ",11111111  , 0.2  ,0)
driver1.wallet=Wallet(2000)
driver2.wallet=Wallet(1300)
driver3.wallet=Wallet(250)
driver4.wallet=Wallet(1190)
odriver1=driver1.wallet
odriver2=driver2.wallet
odriver3=driver3.wallet
odriver4=driver4.wallet

clocat1 = Location(7,15)
clocat2 = Location(16,31)
clocat3 = Location(25,39)
clocat4 = Location(75,89)


car1 = Car("Red   ", driver1, clocat1)
car2 = Car("blue  ", driver2, clocat2)
car3 = Car("black ", driver3, clocat3)
car4 = Car("yellow", driver4, clocat4)

#car1.getDistance(10,12)#distance between the client and the car or driver
#car2.getDistance(2,5)
#car3.getDistance(2,5)
#car4.getDistance(2,5)

#for c in Client.clients_list:
#    print(c)
#locat1.getDistance(2,2)




while True:
 print("enter 1 to List all Client")
 print("enter 2 to List all Drivers")
 print("enter 3 to  List all Cars")
 print("enter 4 to  List Customer Transactions")
 print("enter 5 to List Driver Transactions")
 print("enter 6 to Book a Ride")
 print("enter 7 to Display all Rides")
 print("enter  to Exit")
 print(">> ")
 driver1.wallet=Wallet(2000)
 driver2.wallet=Wallet(1300)
 driver3.wallet=Wallet(250)
 driver4.wallet=Wallet(1190)
 client1.wallet=Wallet(1000)
 client2.wallet=Wallet(500)
 client3.wallet=Wallet(700)
 x=int(input())
 if x==1:
     for client in Client.clients_list:
         print(client)
 elif x==2:
     for driver in Driver.drivers_list:
         print(driver)
 elif x==3:
     for car in Car.cars_list:
         print(car)
 elif x==4:
     if oclient1 != client1.wallet:
         print("name client : " + client1.name)
         print("Balance : ")
         print(client1.wallet)
         print("withdraw")
         print(timestamp)
     elif oclient2 != client2.wallet:
         print("name client : " + client2.name)
         print("Balance : ")
         print(client2.wallet)
         print("withdraw")
         print(timestamp)
     elif oclient3 != client3.wallet:
         print("name client : " + client3.name)
         print("Balance : ")
         print(client3.wallet)
         print("withdraw")
         print(timestamp)
     else: pass
 elif x==5:
    if odriver1 != driver1.wallet:
         print("name client : " + driver1.name)
         print("Balance : ")
         print(driver1.wallet)
         print("deposit")
         print(timestamp)
    elif odriver2 != driver2.wallet:
         print("name client : " + driver2.name)
         print("Balance : ")
         print(driver2.wallet)
         print("deposit")
         print(timestamp)
    elif odriver3 != driver3.wallet:
         print("name client : " + driver3.name)
         print("Balance : ")
         print(driver3.wallet)
         print("deposite")
         print(timestamp)
    elif odriver4 != driver4.wallet:
         print("name client : " + driver4.name)
         print("Balance : ")
         print(driver4.wallet)
         print("deposite")
         print(timestamp)
    else: pass
 elif x==6:
     w=str(input("client name : "))
     if w==client1.name:
         if car1.getDistance(10,15) < car2.getDistance(10,15):
             print("Nearst Car :")
             print(car1)
             www=car1.driver
             xxx=car1
             c=client1
             v=client1.wallet
             bb=www.wallet
         elif car2.getDistance(10,15) < car3.getDistance(10,15):
             print("Nearst Car :")
             print(car2)
             www=car2.driver
             xxx=car2
             c=client1
             v=client1.wallet
             bb=www.wallet
         elif car3.getDistance(10,15) < car4.getDistance(10,15):
             print("Nearst Car :")
             print(car3)
             www=car3.driver
             xxx=car3
             c=client1
             v=client1.wallet
             bb=www.wallet
         else: 
             print("Nearst Car :") 
             print(car4)
             www=car4.driver
             xxx=car4
             c=client1
             v=client1.wallet
             bb=www.wallet
     elif w==client2.name:
         if car1.getDistance(20,40) < car2.getDistance(20,40):
             print("Nearst Car :")
             print(car1)
             www=car1.driver
             xxx=car1
             c=client2
             v=client2.wallet
             bb=www.wallet
         elif car2.getDistance(20,40) < car3.getDistance(20,40):
             print("Nearst Car :")
             print(car2)
             www=car2.driver
             xxx=car2
             c=client2
             v=client2.wallet
             bb=www.wallet
         elif car3.getDistance(20,40) < car4.getDistance(20,40):
             print("Nearst Car :")
             print(car3)
             www=car3.driver
             xxx=car3
             c=client2
             v=client2.wallet
             bb=www.wallet
         else: 
             print("Nearst Car :") 
             print(car4)
             www=car4.driver
             xxx=car4
             c=client2
             v=client2.wallet
             bb=www.wallet
     elif w==client3.name:
         if car1.getDistance(15,30) < car2.getDistance(15,30):
             print("Nearst Car :")
             print(car1)
             www=car1.driver
             xxx=car1
             c=client3
             v=client3.wallet
             bb=www.wallet
         elif car2.getDistance(15,30) < car3.getDistance(15,30):
             print("Nearst Car :")
             print(car2)
             www=car2.driver
             xxx=car2
             c=client3
             v=client3.wallet
             bb=www.wallet
         elif car3.getDistance(15,30) < car4.getDistance(15,30):
             print("Nearst Car :")
             print(car3)
             www=car3.driver
             xxx=car3
             c=client3
             v=client3.wallet
             bb=www.wallet
         else: 
             print("Nearst Car :") 
             print(car4)
             www=car4.driver
             xxx=car4
             c=client3
             v=client3.wallet
             bb=www.wallet
     zz=str(input("comfirm( Y / N)   "))
     if zz == "Y":            
             t=int(input("ENTER DESTINATION Latitude  :"))
             u=int(input("ENTER DESTINATION Longitude :"))
             ride=Ride(w,www,c.loc,(t,u))
             print("distance estimated is:")
             disss=xxx.getDistance(t,u)
             print(disss)
             print("estimated fare is: ")
             feee =ride.Get_fare(disss,www.rate) 
             print(feee)
             z=str(input("comfirm( Y / N)   "))
             if z== "Y":
                print("Ride Completed")
                Ride.ride_list.append(ride)
                #c.wallet.balance = 1000
                #www.wallet.balance = 500
                print("client's ")
                v.withdraw(feee)
                print("driver's ")
                bb.deposit(feee)
                #c.wallet.withdraw(feee)
                #www.wallet.deposit(feee)

             elif z=="N":   print("Cancel")
             else:  print("Invalid Input")
     else:  print("Not Found")
 elif x==7:
       for ride in Ride.ride_list:
           print(ride)
 else:  exit()