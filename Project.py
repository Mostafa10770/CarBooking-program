import math
import datetime

class Location():
    def __init__(self, lat, lon):
        self.__lat = lat
        self.__lon = lon
    def get_lat(self):
        return self.__lat
    def set_lat(self, new_lat):
        self.__lat = new_lat
    def get_lon(self):
        return self.__lon
    def set_lon(self,new_lon):
        self.__lon = new_lon

    def getDistance( self, x, y):

        distance = math.sqrt((Location.__lat - x)**2 + (Location.__lon - y)**2) 
        
        #return distance
        print(f"the distance is {distance}")

    def __str__(self):
        return "LOCATION COORDINATES ARE {} & {}".format(self.get_lat(),self.get_lon())

#////////////////////////////////////////////////////////////////////////////////////////////////////////

class Transaction():
    def __init__(self, amount, type, timestamp):
        self.__amount=amount
        self.__type = type
        self.__timestamp = timestamp
        timestamp = datetime.datetime.now()
        
    def __str__(self):
        return "TRANSACTION {} , {} , {}".format(self.__amount, self.__type, self.__timestamp)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Wallet():
    ctrans_list = []
    dtrans_list = []
    def __init__(self,balance):
        self.balance = balance
        #balance = 0
    def __str__(self):
        return "  WALLET {} ".format(self.balance)

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("balance has been updated : EGP", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("CAN NOT HAPPEN your balance is : EGP", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("balance has been updated : EGP", self.balance)
    
    def transfer(self,amount,outbalance,inbalance):
        #self.withdraw(amount,outbalance)
        #self.deposit(amount,inbalance)
        self.amount = amount
        self.inbalance = inbalance
        self.outbalance = outbalance
        if self.amount > self.outbalance :
            print(f"CAN NOT HAPPEN {self.outbalance} balance is : EGP {self.balance}")
        else:
            self.outbalance -= self.amount
            self.inbalance += self.amount
            print(f"the client balance is : EGP {self.outbalance} and driver balance is : EGP {self.inbalance}")
    
    def addTrans(self,trans_list,transaction):
        Wallet.__trans_list = trans_list
        self.__trans_list.append(transaction)

    def printTrans(self, trans_list):
        for transction in trans_list:
              print(transction)
#////////////////////////////////////////////////////////////////////////////
class Person:
    def __init__(self, name, addr, ssn, wallet : Wallet):
        self.name = name
        self.addr = addr
        self.ssn = ssn
        self.wallet = wallet
#////////////////////////////////////////////////////////////////////////////
class Client(Person):
    clients_list=[]
    cwallet = []
    def __init__(self,name,addr,ssn, loc, wallet : Wallet):
         super().__init__(name,addr,ssn,wallet)
         self.loc = loc
         Client.clients_list.append(self)

    def __str__(self):
        return f"CLIENT -> {self.name} {self.addr} {self.ssn} {self.loc} {self.wallet}"
#/////////////////////////////////////////////////////////////////////////////
class Driver(Person):
    drivers_list=[]
    dwallet = []
    def __init__(self, name, addr, ssn, rate, wallet : Wallet):
        super().__init__(name, addr, ssn, wallet)
        self.rate = rate
        Driver.drivers_list.append(self)

    def __str__(self):
        return f" DRIVER -> {self.name} {self.addr} {self.ssn} {self.rate}★ {self.wallet}"
#/////////////////////////////////////////////////////////////////////////////

class Car:
    cars_list = []
    def __init__(self, color, driver : Driver, location : Location):
        self.location=location
        self.__color=color
        self.driver=driver
        Car.cars_list.append(self)
    def get_color(self):
        return self.__color
    def set_color(self,new_color):
        self.__color=new_color
    def getDistance(self, Client_lat, Client_lon):
        self.Client_lon = Client_lon
        self.Client_lat = Client_lat
        distance = math.sqrt((self.location.get_lat() - self.Client_lat) ** 2 + ((self.location.get_lon() - self.Client_lon) ** 2))
        #print(distance)
        return distance  

    def __str__(self):
        return f"CARS -> {self.__color} {self.location}  [{self.driver.name} - {self.driver.rate}★]"

#//////////////////////////////////////////////////////////////////////////////

class Ride:
    ride_list = []
    def __init__(self, client, car, dest : Location , src : Location):
        self.__client=client
        self.__car=car
        self.dest=dest
        self.src=src

    def get_client(self):
        return self.__client
    def get_car(self):
        return self.__car
#    def get_dest(self):
#        return self.__dest
#    def get_src(self):
#       return self.__src

    def set_client(self, new_client):
        self.__client = new_client
    def set_car(self, new_car):
        self.__car = new_car
#    def set_dest(self, new_dest):
#        self.__dest = new_dest
#    def set_src(self, new_src):
#        self.__src= new_src

    def calcDistance(self):
        distance = math.sqrt((self.src.get_lat() - self.dest.get_lat()) ** 2 + ((self.src.get_lon() - self.dest.get_lon()) ** 2))
        print(distance)
        return distance

    def Get_fare(self, dis, rate):
        self.rate = rate
        self.dis = dis
        fare = (self.dis * 10) * ( 1 + self.rate)
        #print(fare)
        return fare

    def __str__(self):
        return f'{self.__client} = {self.__car} {0.1} -> {self.src} [  ]'
#////////////////////////////////////////////////////////////////////////////////////