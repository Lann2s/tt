

import sys


print("hello") 

#name =input("what is your name ?")
#print(f"hay {input("what is your name ?")} wellcome to this course")





'''
numbers = []


for i in range (10):
   num = int(input(f"enter number {i+1} :"))
   numbers.append(num)

print(numbers)


max = numbers[0]

for i in numbers :
    if max <  i:
       max = i
   
  
 
print (f"maxmim number is {max} ")
'''


'''
s = set()

for i in range(4):
      s.add(int(  input("enter a number ")  )  )
      

print (s)


print( len(s)) 

'''

'''
dic = {}



for i in range(5) :
    name= input("enter name :")
    idnum =input("enter id number :")
    dic[name] =idnum



print (dic)


'''
'''

n =int ( input("enter a number"))

for i in range(n) :
    
    print (f"square {i} is {sq.square(i)}")
    

'''



'''
    
class Flight():

   def __init__(self):
        self.pasengers = []
        self.capacity = 50 
  

    
   def add_pasngers(self , name):
       if self.free_seat() <= self.capacity and self.free_seat() > 0:
           self.pasengers.append(name)
           return True
       else :
           print("no have available seat")
           return False

           
   def free_seat(self)   :
       return int (self.capacity - len(self.pasengers) )
     
     
     
     
flight = Flight()

x= int (input("how many pepole ypu want book for ? "))
names = []
for i in range(x) :
    name = input(f"enter the name for pasnger {i} :")
    names.append(name)
    
    

for i in names:
    if  flight.add_pasngers(i) :
        print(f"pasnger name {name} has benn added")
    else : 
     print(f"pasnger name {name} has NOT benn added")



print(f" the pasnger in this plan is {flight.pasengers}")


'''

'''
def ans (f):
    def warp() :
        print ("star")
        f()
        print("end")
    return warp


@ans
def tryy():
    print("hello")


tryy()

'''

'''
people =[{"name" : "lana" , "age" : "20"} ,{"name" : "tala" , "age" : "23"}, {"name" : "azzam" , "age" : "15"}]


people.sort( key=lambda  x :x["name"]  )


print(people)
'''
try :
    x= int (input ("enter a number : "))
    y= int (input ("enter a number : "))

    div = x / y 
    
except ZeroDivisionError:
    print("error dividion")
    sys.exit(1)
except ValueError :
    print("Value Error:")
    sys.exit(1)


print(div)

