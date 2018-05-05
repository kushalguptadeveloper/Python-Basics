import random
import sys
import os

print("hello")

# comment

name = "kushal"
print(name)

# dataTypes - Numbers,Strings,Tuples,Lists,Dictionaries


# creating a list

fruit_list = ['banana', ' apple', 'mango']

vegie_list = ['brocolli', 'spinach', 'potato']

print("item 1 =" + fruit_list[1])

# lsit within list
list_within_list = [fruit_list, vegie_list]
print(list_within_list)
print(list_within_list[0][2])

# appending a list
vegie_list.append("onion")
print(list_within_list)
print(vegie_list)

# inserting at perticular position in list

vegie_list.insert(1, "pickle")
print(vegie_list)

# removing a particular item in list
vegie_list.remove("pickle")
print(vegie_list)

# reversing a list
vegie_list.reverse()
print(vegie_list)

# sorting a list
vegie_list.sort()
print(vegie_list)

# deleting a particular element by no in list

del vegie_list[3]
print(vegie_list)

# creating a single list by adding items of two list

add_list = fruit_list + vegie_list
print(add_list)

# getting the length of a list

print(len(add_list))

# getting last element of list
print(max(add_list))

# getting first element of list
print(min(add_list))

# Tuples -  Unlike lists tuples cant be changed once they are created

# creating a tuple

pi_tuple = (1, 2, 3, 4, 5)

# making a list from tuple
list_tuple = list(pi_tuple)
print(pi_tuple)
print(list_tuple)

# accessing particular item of a tuple
print(pi_tuple[0])

# creating a tuple from list
tuple_list = tuple(list_tuple)
print(tuple_list)

# getting length of tuple

print(len(tuple_list))

# getting lest element of tuple

print(max(tuple_list))

# getting first element of tuple
print(min(tuple_list))

# dictionaries are stored with key , the main difference is that dictionaries cant be joined with + sign as done in list

dic = {'key1': 'kushal',
       'key2': 'anubhav',
       'key3': 'nainika'}

print(dic['key1'])

# deleting a dictionary
del dic['key2']
print(dic)

# another way of printing something
print(dic.get("key3"))

# getting length
print(len(dic))

# changing value of a particular key
dic['key3'] = 'nain'
print(dic['key3'])

# getting all keys

print(dic.keys())

# getting all values

print(dic.values())

# conditionaries

age = 21;
if age == 20:
    print("haww")
elif age == 21:
    print("ooyeah")
else:
    print("noo")

# using for loop

for x in range(0, 10):
    print(x, '', end="")

print("\n")

for y in vegie_list:
    print(y)

for n in [2,4,5]:
        print(n)

num_list = [[0,1,2],[10,20,30],[100,200,300]]

for k in range(0,3):
    for nk in range(0,3):
        print(num_list[k][nk])

random_num = random.randrange(0,100)


#defining a function

def addNumber(no1,no2):
    temp = no1 + no2
    return temp

print(addNumber(1,2))


#taking input from user

#name = sys.stdin.readline()
#print(name)

#performing functions on strings

long_string = "i'll play cricket today"

#printing first four characters
print(long_string[0:4])

#printing last five characters

print(long_string[-5:])

#printing till last except for last 5 charcters

print(long_string[:-5])

#concatenating

print(long_string[:4] + " dance")

#captitalizing

print(long_string.capitalize())
print(long_string.find("floor"))

#creating a file

test_file = open("text.txt", "wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("hola \n", "UTF-8"))

test_file.close()

#reading afile

test_file = open("text.txt", "r+")

text_in_file = test_file.read()

print(text_in_file)


class Animal:

    __name = ""

#making constructor

    def __init__(self, name):
        self.__name = name

    #setters and getters

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_type(self):
        return "animal"

    def to_string(self):
        return "{}is myname".format(self.__name)

#making object of class and calling its function


dog = Animal("anubhav")

print(dog.to_string())


class Dog(Animal):

    __owner = ""

    def __init__(self, namea, owner):

        Animal.__init__(self, namea)
        self.__owner = owner
       # super(Dog, self).__init__(name)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        return "dog"

    def to_string(self):
        #self.set_name("hola")
        return "{} is myname and wife is {}".format(self.get_name(), self.__owner)


    #passing a parameter or not using None

    def para(self, sound=None):

        if sound is None:
            print("no sound")

        else:
            print("sound is there")


bruno = Dog("anubhav", "rupali")

print(bruno.to_string())

bruno.para()


#polymorphism

class AnimalType:
    def animal_type(self, animal):
        print(animal.get_type())


type = AnimalType()
type.animal_type(bruno)
type.animal_type(dog)
