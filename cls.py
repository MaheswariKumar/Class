#Chapter-9
#Object Oriented Programming 
#Class
#Creating and Using a Class
class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.upper() + " is stiiting now")

	def roll_over(self):
		print(self.name.title() + " is rolling over")

#making an instance from class
my_dog = Dog("willie", 6)

#Accessing an attribute name => EX: my_dog.name
print("my Dog name is " + my_dog.name)
print("my Dog age is " + str(my_dog.age))

#Calling methods
my_dog.sit()
my_dog.roll_over()

#Creating a multiple instances
your_dog = Dog("shalu", 5)
print("my Dog name is " + your_dog.name)
print("my Dog age is " + str(your_dog.age))
your_dog.sit()
your_dog.roll_over()

#Ass-1
class Restarunt():
	def __init__(self, restarunt_name, cusine_type):
		self.restarunt_name = restarunt_name
		self.cusine_type = cusine_type

	def describe_restarunt(self):
		print("restarunt_name is " + self.restarunt_name.title() + " cusine_type is " + self.cusine_type.upper())
	def open_restarunt(self):
		print("The Restarunt is open now")

my_restarunt = Restarunt("mahi", "chettinadu")
my_restarunt.describe_restarunt()
my_restarunt.open_restarunt()

#Ass-2
details = Restarunt("laxmi", "all types")
details.describe_restarunt()
details1 = Restarunt("selvi", "chinese")
details1.describe_restarunt()

#Ass-3
class User():
	def __init__(self, first_name, last_name, age, dob):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.dob = dob

	def describe_user(self):
		print("first_name: " + self.first_name.title() + 
					" last_name: " + self.last_name.title() + " age is " + str(self.age) + " dob is " + self.dob)

	def greet_user(self):
		print("Hi " + self.first_name.upper() + " " + self.last_name.upper() +   " welcome to the login page")

my_user = User("maheswari", "kumar", 23, "08/04/1998")
my_user.describe_user()
my_user.greet_user()
my_user1 = User("tamil", "kumar", 27, "02/06/1994")
my_user1.describe_user()
my_user1.greet_user()	


#Working with class and instance
class Car():
	def __init__(self, year, model):
		self.year = year
		self.model = model	

	def describe(self):
		msg = str(self.year) + " " + self.model.upper()
		print(msg)

my_car = Car(1999, "Audi")
my_car.describe()

#Setting default value for attribute
class Car():
	def __init__(self, year, model):
		self.year = year
		self.model = model
		self.milage = 0 # if you want to set a default value for an attribute and that no need add as parameter

	def describe(self):
		msg = str(self.year) + " " + self.model
		print(msg)

	def car_milage(self):
		print(self.model + " milage is " + str(self.milage)) 

my_car = Car(1888, "BMW")
my_car.describe()
my_car.car_milage()

#Modify the attribute values
#set the value through instaces directly
my_car.milage = 20
my_car.car_milage()

#set the value through the method
class Car():
	def __init__(self, year, model):
		self.year = year
		self.model = model
		self.milage = 0 # if you want to set a default value for an attribute and that no need add as parameter

	def describe(self):
		msg = str(self.year) + " " + self.model
		print(msg)

	def car_milage(self):
		print(self.model + " milage is " + str(self.milage)) 

	def update_value(self, milage):
		#Additional work
		if milage >= milage:
			self.milage = milage
		else:
			print("you can't change")
#Incrementing attributes values through method
	def increment(self, miles):
		self.milage += miles

my_car = Car(1888, "BMW")
my_car.describe()
my_car.update_value(20)
my_car.increment(100)
my_car.car_milage()

#Ass-1
class Restarunt():
	def __init__(self, restarunt_name, cusine_type):
		self.restarunt_name = restarunt_name
		self.cusine_type = cusine_type
		self.number_served = 0

	def describe_restarunt(self):
		print("restarunt_name is " + self.restarunt_name.title() + " cusine_type is " + self.cusine_type.upper())
	def open_restarunt(self):
		print("The Restarunt is open now")
	def set_number_served(self):
		print(self.number_served)
	def increment_server(self, servers):
		self.number_served += servers

my_restarunt = Restarunt("mahi", "chettinadu")
print(my_restarunt.number_served)
my_restarunt.describe_restarunt()
my_restarunt.open_restarunt()
my_restarunt.number_served = 20
my_restarunt.increment_server(10)
my_restarunt.set_number_served()

#Ass-2
class User():
	def __init__(self, first_name, last_name, age, dob, login_attmpt):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.dob = dob
		self.login_attmpt = login_attmpt

	def describe_user(self):
		print("first_name: " + self.first_name.title() + 
					" last_name: " + self.last_name.title() + " age is " + str(self.age) + " dob is " + self.dob)

	def greet_user(self):
		print("Hi " + self.first_name.upper() + " " + self.last_name.upper() +   " welcome to the login page")

	def increment_login_attempt(self):
		self.login_attmpt += 1
		print("login attempts are " + str(self.login_attmpt))

	def reset_login_attempt(self):
		self.login_attmpt = 0
		print("reset " + str(self.login_attmpt))

my_user = User("maheswari", "kumar", 23, "08/04/1998", 1)
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempt()
my_user.increment_login_attempt()
my_user.increment_login_attempt()
my_user.increment_login_attempt()
my_user.increment_login_attempt()
my_user.reset_login_attempt()

#Inhertance
class Car():
	def __init__(self, year, model):
		self.year = year
		self.model = model
		self.milage = 0 # if you want to set a default value for an attribute and that no need add as parameter

	def describe(self):
		msg = str(self.year) + " " + self.model
		print(msg)

class Electric_car(Car):
	def __init__(self, year, model):
		super().__init__(year, model)
		#creating new attribute for child car
		self.battery = 70

	#creating new method for child car
	def battery_info(self):
		print("The Electric car has " + str(self.battery) + " kWh battery" )

my_audi = Electric_car(2000, "audi")
my_audi.describe()
my_audi.battery_info()

#Overriding methods from the parent class
class Car():
	def __init__(self, year, model):
		self.year = year
		self.model = model
		self.milage = 0 # if you want to set a default value for an attribute and that no need add as parameter

	def describe(self):
		msg = str(self.year) + " " + self.model
		print(msg)

	def gas_tank(self):
		print("car does have gas tank ")

class Electric_car(Car):
	def __init__(self, year, model):
		super().__init__(year, model)
		#creating new attribute for child car
		self.battery = 70

	#creating new method for child car
	def battery_info(self):
		print("The Electric car has " + str(self.battery) + " kWh battery" )

	def gas_tank(self):
		print("Electric_car does not have gas tank ")

my_audi = Electric_car(2000, "audi")
my_audi1 = Car(2000, "audi")
my_audi.describe()
my_audi.battery_info()
my_audi.gas_tank()
my_audi1.gas_tank()

#Instance as Attributes
class Car():
	def __init__(self, year, model):
		self.year = year
		self.model = model
		self.milage = 0 # if you want to set a default value for an attribute and that no need add as parameter

	def describe(self):
		msg = str(self.year) + " " + self.model
		print(msg)

class battery():
	def __init__(self, battery=80):
		self.battery = battery

	def battery_info(self):
		print("The Electric car has " + str(self.battery) + " kWh battery" )

	def range(self):
		if self.battery == 70:
			range = 240
		elif self.battery == 80:
			range = 280
		msg = "this car has " + str(range) + " range"
		print(msg)

class Electric_car(Car):
	def __init__(self, year, model):
		super().__init__(year, model)
		self.battery = battery()
		self.range = range
	

my_audi = Electric_car(2000, "audi")
my_audi.describe()
my_audi.battery.battery_info()
my_audi.battery.range()

#Ass-1
class Restarunt():
	def __init__(self, restarunt_name, cusine_type):
		self.restarunt_name = restarunt_name
		self.cusine_type = cusine_type

	def describe_restarunt(self):
		print("restarunt_name is " + self.restarunt_name.title() + " cusine_type is " + self.cusine_type.upper())
	def open_restarunt(self):
		print("The Restarunt is open now")

class IceCreamStand(Restarunt):
	def __init__(self, restarunt_name, cusine_type):
		super().__init__(restarunt_name, cusine_type)
		self.flavours = ["vennila", "choco", "mango"]

	def displays(self):
		lst = self.flavours
		for lsts in lst:
			print(lsts)

my_restarunt = IceCreamStand("mahi", "chettinadu")
my_restarunt.displays()

#Ass-2
class User():
	def __init__(self, first_name, last_name, age, dob):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.dob = dob

	def describe_user(self):
		print("first_name: " + self.first_name.title() + 
					" last_name: " + self.last_name.title() + " age is " + str(self.age) + " dob is " + self.dob)

	def greet_user(self):
		print("Hi " + self.first_name.upper() + " " + self.last_name.upper() +   " welcome to the login page")

class Admin(User):
	def __init__(self, first_name, last_name, age, dob):
		super().__init__(first_name, last_name, age, dob)
		self.privilages = ["can add post", "can delete post", "can ban user"]

	def show_privilages(self):
		lst = self.privilages
		for lsts in lst:
			print(lsts)

my_user = Admin("maheswari", "kumar", 23, "08/04/1998")
my_user.show_privilages()

#Ass-3
class User():
	def __init__(self, first_name, last_name, age, dob):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.dob = dob

	def describe_user(self):
		print("first_name: " + self.first_name.title() + 
					" last_name: " + self.last_name.title() + " age is " + str(self.age) + " dob is " + self.dob)

	def greet_user(self):
		print("Hi " + self.first_name.upper() + " " + self.last_name.upper() +   " welcome to the login page")

class privilages():
	def __init__(self, privilages=["can add post", "can delete post", "can ban user"]):
		self.privilages = privilages

	def show_privilages(self):
		lst = self.privilages
		for lsts in lst:
			print(lsts)


class Admin(User):
	def __init__(self, first_name, last_name, age, dob):
		super().__init__(first_name, last_name, age, dob)
		self.privilages = privilages()

my_user = Admin("maheswari", "kumar", 23, "08/04/1998")
my_user.privilages.show_privilages()

#Ass-4
class Car():
	def __init__(self, year, model):
		self.year = year
		self.model = model
		self.milage = 0 # if you want to set a default value for an attribute and that no need add as parameter

	def describe(self):
		msg = str(self.year) + " " + self.model
		print(msg)

class battery():
	def __init__(self, battery=70):
		self.battery = battery

	def battery_info(self):
		print("The Electric car has " + str(self.battery) + " kWh battery" )

	def ranges(self):
		if self.battery == 70:
			ranges = 240
		elif self.battery == 85:
			ranges = 280
		
		msg = "this car has " + str(ranges) + " range"
		print(msg)

	def upgrade_battery(self):
		if self.battery == 70:
			self.battery = 85
			print("upgrade the battery to 85")
		else:
			print("already upgraded")
		
class Electric_car(Car):
	def __init__(self, year, model):
		super().__init__(year, model)
		self.battery = battery()
	
my_audi = Electric_car(2000, "audi")
my_audi.describe()
my_audi.battery.battery_info()
my_audi.battery.upgrade_battery()
my_audi.battery.ranges()
my_audi.battery.upgrade_battery()
my_audi.battery.ranges()

#Python Standard Library
#OrderedDict() from collections module
from collections import OrderedDict
fav_lanuages = OrderedDict()
fav_lanuages["Mahi"] = "Python"
fav_lanuages["Nandi"] = "C"
fav_lanuages["Tamil"] = "C++"

for a, b in fav_lanuages.items():
	print(str(a) + " fav lanuages is " + str(b))

#Ass-1
from collections import OrderedDict

fav_ice = OrderedDict()

fav_ice["prithi"] = "choco"
fav_ice["subi"] = "cone"
fav_ice["aswath"] = "vennila"

for x, y in fav_ice.items():
	print(str(x) + " fav IceCream is " + str(y))

#Ass-2
#We have random module that contains one fucntion called as randint()
from random import randint
x = randint(1, 6)
print(x)

from random import randint
class Die():
	def __init__(self, slides=6):
		self.slides = slides

	def roll_die(self):
		return randint(1, self.slides)
		
my_die = Die()
results = []
for roll in range(10):
	result = my_die.roll_die()
	results.append(result)
print(results)