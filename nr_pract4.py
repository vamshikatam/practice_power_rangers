#1 count of list
list=[1,2,3,4,22,33,44,5]
v=0
for i in list:
    v=v+1
print(v)

#2 first and last no of list.

list=[66,2,3,4,22,33,44,1]
list[0],list[-1]=list[-1],list[0]
print(list)

#3
list=[66,2,3,4,22,33,44,1]
le=len(list)
tem=list[0]
list[0]=list[le-1]
list[le-1]=tem
print(list)

#4 unique
l1=[1,2,5,7,99,9,4]
l2=[2,5,99,44,3]
l3=[]
for i in l1:
 if i in l2 and i not in l3:
    l3.append(i)
print(l3)

#5 max of list:
def max():
    lst=[1,222,887878,33,45,6]
    tem=0
    for i in lst:
        if i>tem:
            tem=i
    print(tem)
max()

#6 vowels
new=input("enter a alphabet:")
cout=0
if new in ("a","e","i","o","u","A","E","I","O","U"):

    print(new,"vowel")
else:
    print("consonant")


#7 upper & lower
l=input("enter:")
list=[]
list1=[]
for i in l:
    if i.isupper():
        list1.append(i)
    else:
        list.append(i)
print(list1)
print(list)

# 8 p & n
l1=[1,2,3,5,0,-3,-4,-6]
l2=[]
l3=[]
for i in l1:
    if i<0:
        l2.append(i)
    else:
        l3.append(i)
print(l2)
print(l3)

#9 len vowels
new=input("enter a alphabet:")
cout=[]
l=["a","e","i","o","u","A","E","I","O","U"]
for i in l:
    if i in new:
        cout.append(i)
print(cout)
print(len(cout))


#10 reverse of str

new="sting"
cout=""
for i in new:
    cout=i+cout
print(cout)

#11 sort

new="helpme"
v=sorted(new)
print(v)
new="".join(v)
print(new)

#12reverse number = 1672

number=1234
rev =0
while (number > 0):
    rem = number % 10
    rev=(rev*10)+rem
    number=number//10
print((rev))

#13 reverse of tuple

x=(10,12,18,30,33)
reversetuple=()
for y in reversed(range(len(x))):
    reversetuple+=(x[y],)
print("reversing=",reversetuple)


#14 user pass word:
user_name = input("enter user name:")
password = input("enter password:")
if user_name == "vamshi":
    if password == "krishna123":
        print("welcome user:")
    else:
        print("enter password:")
else:
    print("wrong password:")

#2
while True:
    user=input(("enter a user :"))
    password=input("enter password:")
    if user=="naresh" and password=="1234it":
        break
    print("wrong password try again!")
print("welcome:")

#15 10 city names:
new=[]
for i in range(10):
    t=input("enter city name:")
    new.append(t)
print(new)

#16 odd no:

lst=[1,2,3,4,5,6,7,8,9]
new=[]
for i in lst:
    if i%2!=0:
        new.append(i)
print(new)
#2
lst=[]
for i in range(10):
    if i%2!=0:
        lst.append(i)
print(lst)


#17 largest_no from list:

def max():
    lst=[1,222,887878,33,45,6]
    tem=0
    for i in lst:
        if i>tem:
            tem=i
    print(tem)
max()
#2
def max():
    set_e=[1111,222,887878,33,45,6,2222222,77,1]
    tem=0
    min = set_e[0]
    for i in set_e:
        if i>tem:
            tem=i
        if i<min:
            min = i
    print(tem,min)
max()
#18 pos values to lst remove negative value:

lst=[]
for i in range(10):
    user=int(input("enter the value:"))
    if user<0:
        print("enter positive no:")
    else:
        lst.append(user)
print(lst)

#19 random values in dict
import random
d={}
for i in range(1,5):
    new=random.randint(1,20)
    v=i**2
    d2={new:v}
    d.update(d2)
print(d)

#2
import random
d={}
for i in range(1,5):
    new=random.randint(1,20)
    v=new*new
    d2={new:v}
    d.update(d2)
print(d)

#20
d1={"hyd":44,"wgl":77}
d2={}
for i,j in d1.items():
    print("temperature {} is {}".format(i,j))

#21 sum of values:
d1={1:1,2:1,3:1,4:1,5:1}
v=d1.values()
t=sum(v)
print(t)

#22 removing the key:
d1={1:23,2:43,3:45}
user=int(input("enter a value:"))
d1.pop(user)
print(d1)

#2
d1={1:23,2:43,3:45}
user=int(input("enter a value:"))
if user in d1:
 d1.pop(user)
else:
    print("key not found")
print(d1)

#22
d={1:["a","b"],2:["c","d"]}
for a in d[1]:
    for b in d[2]:
        print(a,b)
'''
a c
a d
b c
b d
'''

#22
import random
i=[]
for x in range(5):
    randomnum=random.randint(1,30)
    i.append(randomnum)
re= (x**3 for x in i) #list
print(re)

#23 odd even
lst=[2,3,4,5,6,7,8,9]
l1=[]
l2=[]
m=[l1.append(i) if i %2==0 else l2.append(i) for i in lst]
print(l1)
print(l2)

#24
ph=[]
for i in range(2):
 lst=int(input("enter mobile no:"))
 ph.append(lst)
print("original",ph)
con=[i if len(str(i))==10 else ph.remove(i) for i in ph]
print("after removing",ph)


#26 com in set, uniq
s1={1,2,3,4,5}
s2={3,4,5,6,7,}
s3={3,4,5,6,8,}
s4=[]
for a in s1:
    for b in s2:
        for c in s3:
            if a==b==c:
                s4.append(a)
print(set(s4))

#27 set max and min
def max():
    set={1,222,887878,33,45,6}
    tem=0
    for i in set:
        if i>tem:
            tem=i
    print(tem)
max()

#28
x={1,2,4,76}
x.add(8)
print(x)

f = ["css", "html", "sql"]

b = frozenset(f)
#frozenset' object does not support item assignment

b[1] = "python"


#29 pass word
def password_check(user_password):
    numerics="0123456789"
    capital_alphabets="ABCD"
    special="#@%"
    sum=0
    x=0
    y=0
    z=0
    while sum!=3:
        while len(user_password)!=6:
            user_password=input(" please enter correct possword:")

        for i in range(len(user_password)):
            if user_password[i] in numerics:
                x=1
            elif user_password[i] in capital_alphabets:
                y=1
            elif user_password[i] in special:
                z=1
        sum=x+y+z
        if sum!=3:
            user_password=input("enter a correct password")
        else:
            print("password accepted")
password_check(" ")

#30 function will work like range function:
def demo(n):
    if (n==0):
        return 0
    print(n)
    demo(n-1)
demo(5)
#2
def value(start,stop,step):
    while stop >start:
        yield start
        start+=step
for i in value(23,40,5):
    print(i)

#31 count of upper and lower:
def a(str):
    upper,lower=0,0
    for i in range(len(str)):
        if str[i].isupper():
            upper+=1
        elif str[i].islower():
            lower+=1
    print("upper case:",upper)
    print("lower case:",lower)
str=input("enter a value:")
a(str)

#32 polindrome using func:
def polindrome(name):
    name1=""
    for i in name:
        name1=i+name1
    if name==name1:
        print("polindrome")
    else:
        print("not polindrome")
name=input("enter:")
polindrome(name)

#33
def showemployee(name,salary=5000):
    print("employee:",name,"salary:",salary)
showemployee("vams",10000)
showemployee("krish")

#34
class car:
    def __init__(self,name,colour,style):
        self.name=name
        self.colour=colour
        self.style=style
    def display(self):
        print(self.name)
        print(self.colour)
        print(self.style )
c=car("tesla","black","Z23")
c.display()

#35
class fruits:
    def __init__(self,colour="red",fruit="mango",taste="sweet"):
        self.colour=colour
        self.fruit=fruit
        self.taste=taste
    def detail(self):
        print(self.colour)
        print(self.fruit)
        print(self.taste)
f=fruits("blue")
f.detail()



#36 class person:
class person:
    def getname(self,name):
        self.name=name
    def getage(self,age):
        self.age=age
class employee(person):
    def empid(self,emp_id):
        self.empid_id=emp_id
    def salary(self,salary):
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("emp_id",self.empid_id)
        print("salary:",self.salary)
emp=employee()
emp.getname("vamshi")
emp.getage(23)
emp.empid(12334)
emp.salary(30000)
emp.display()

#37
class vehicle:
    def colour(self, colour):
        self.colour = colour
    def type(self, type):
        self.type = type
class car(vehicle):
    def no_passengers(self, no_passengers):
        self.no_passengers = no_passengers
    def show(self):
        print("colour:", self.colour)
        print("type:", self.type)
        print("passengers:", self.no_passengers)
class bike(vehicle):
    def no_passengers(self, no_passengers):
        self.no_passengers = no_passengers
    def show(self):
        print("colour:", self.colour)
        print("type:", self.type)
        print("passengers:", self.no_passengers)
emp = car()
emp.colour("red")
emp.type("4 tyer")
emp.no_passengers(4)
emp1=bike()
emp1.colour("black")
emp1.type("2 tyer")
emp1.no_passengers(4)
emp.show()
emp1.show()

#38
class animal:
    def eating(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("bark")
d=dog()
d.eating()
d.bark()

#2
class family:
    def family(self):
        print("this is our family:")
class parent(family):
    def parent_n(self):
        print("parent")
class son(parent):
    def son(self,name):
        self.name=name
    def display(self):
        print("son name:",self.name)
c=son()
c.son("raju")
c.family()
c.parent_n()
c.display()

#39 How to Shuffle a Deck of Card in Python
import  random
class card:
    def addcard(self):
        self.A=list(range(1,53))
        print(self.A)
    def shufflei(self):
        random.shuffle(self.A)
        print("cards after shuffle:",self.A)
ob=card()
ob.addcard()
ob.shufflei()
#40
def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:

        return (a * power(a, b - 1))
a = 2
b = 4
print(power(a, b))

#2
def recursion(val,n):
    if n==0:
        return 1
    return (val*recursion(val,n-1))
print(recursion(10,3))


#41 roman:
class vam:
    def roman(self,num):
        val=[1,2,3,4,5]
        syb=["I","II","III","IV","V"]
        roman=""
        i=0
        while num>0:
            for i in range(num//val[i]):
                roman+=syb[i]
                num-=val[i]
            i+=1
        return roman
print(vam().roman(4))

#42
add=lambda  x,y:x+y
mul=lambda x,y:x*y
a=int(input("enter "))
b=int(input("enter 2"))
print("add",add(a,b))
print("mul",mul(a,b))



#43
def vam(n):
    if n == 0:
        return
    print(n)
    vam(n - 1)
vam(10)

#44  random 10 prime no:
import random
lst=[]
def rang():
    for i in range(10):
        x=random.randint(1,100)
        lst.append(x)
    print(lst)

def prime():
    for i in lst:
        for j in range(2,i):
            if i%j==0:
                print(i,"not prime no")
                break
        else:
            print(i,"prime no")
rang()
prime()


#45 class inside it create 3 function like no.of words, no. character,no of vowels
class new:
    def no_of_words(self):
        print("vams")
    def no_character(self):
        print(4)
    def no_vowels(self):
        print("aeiou")
s1=new()
s1.no_of_words()
s1.no_vowels()
s1.no_character()

#46 exception
a = 10
b = 0
try:
    print(a / b)
except Exception:
    print("you cannot divided a no. by zero:")

finally:
    print("hi vamshi")


#47
l1=[4,8,9]
l2=[6,8,0]
l3=list(map(lambda x,y:x+y,l1,l2))
print(l3)



#48
lst1 = [("x",88),("a",43,"k",54)]
lst1.sort(key=lambda y:y[1])
print(lst1)

#49 even and odd
y=[2,3,4,5,6]
even=list(filter(lambda x:x%2==0,y))
print(even,"even:")
odd=list(filter(lambda x:x%2==1,y))
print(odd,"odd:")


#50 day,month,year using lambda
import datetime
now= datetime.datetime.now()
print(now)
year=lambda x:x.year
month= lambda x:x.month
day=lambda x:x.day
time=lambda x:x.time
print(year(now))
print(month(now))
print(day(now))
print(time(now))

#51
import os
current_dir=os.getcwd()
print(current_dir)
os.chdir("/Users\PRASHANTH\PycharmProjects\Practice\import\pract_new/exceptions")
print(os.getcwd())

#52
import numpy as np
lst=[10,20,30,40,50]
new=np.array(lst)
print(new)
print(type(new))

#53
#np program to create 4*4 matrix with range og 40-80.
import numpy as np
arr=np.arange(40,80,2.5).reshape((4,4))
print(arr)

#54 4*4 matrix and fill
import numpy as mp
a=mp.arange(4,20).reshape(4,4)
print(a)

#55
import datetime
now=datetime.datetime.now()
print(now)


#56 file handling
f = open('file.py','r')
print(f.read())
#2
f = open('file.py','r')
f1=open('file.py','w')
print(f1.write("bannu"))
#3write a python program to append text to a file and display the text.
from itertools import islice
with open('file.py','w') as file:
    file.write("hi  vams")
    file.write("hyd")
txt=open('file.py')
print(txt.read())
#4 write a python program to read a file line by line store it into an array.
lst=[]
with open('file.py') as f:
    for l in f:
        lst.append(l)
    print(lst)
#5combine each line from first file with the corresponding line in second:
with open('file.py') as f1, open('file.py') as f2:
    for line1, line2 in zip(f1, f2):
        print(line1 + line2)

#57 fibbonacci
n=int(input("en"))
a=0
b=1
for i in range(n):
    print(a)
    c=a
    a=b
    b=c+b
print(b)

#58generator expression for cal cube roots
def root():
    i=0
    while i<=5:
        yield i**3
        i+=1
print(list(root()))

#59 arithametic progression
def num():
    a=1
    while True:
        yield  a*a
        a+=1
for n in num():
    if n>100:
        break
    print("square:",n)

#
def top():

    yield 5
    yield 3
    yield 2
    yield 9
val=top()
print(val.__next__())
print(val.__next__())
for i in val:
    print(i)
#
def top():
    n=1
    while n<=10:
        s=n*n
        yield s
        n+=1

val=top()
for i in val:
    print(i)
#
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for f in fib():
    if f>50:
        break
    print(f)


#60prime no using generator
def prime(a):
    for i in range(2,a):
        c=0
        for j in  range(2,i):
            if i%j==0:
                c=1
                break
        if c==0:
            yield i
print(list(prime(20)))


#61
import threading
def cube(val):
    print("cube:",val**3)
def square(val):
    print("square:",val**2)
obj1=threading.Thread(target=cube(5))
obj2=threading.Thread(target=square(3))
obj1.start()
obj1.join()
obj2.start()
obj2.join()

#62
from  time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)
t1=hello()
t2=hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("vamshi")

#63
d="python"
it=iter(d)
lenth=len(d)
while lenth>0:
    t=next(it)
    if t in ["a","e","i","o","u"]:
        print(t)
    lenth-=1

#64
import time
def square(num):
    print("calculate square:")
    for n in num:
        time.sleep(1)
        print("square:",n*n)
def cube(num):
    print("calculate cube:")
    for n in num:
        time.sleep(1)
        print("cube:",n*n*n)
arr=[1,2,3,4]
t=time.time()
square(arr)
cube(arr)
print("done",time.time()-t)
print("iam done")