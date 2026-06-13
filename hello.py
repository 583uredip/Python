print("Hi, welcome to Python programming!")
a=20
b=30
c=a+b
print("The sum of a and b is:",c)
if 10<100:
    print ("10 is less than 100")
    ##Statements 
    print("America is a great country"); print("I love programming"); print("Python is a great language")
    #Python Output / Print
    print('Brazil is a great country',end=' in South America,')
    print('I love Neymar',end=' and I love watching football\n')
    print(2026)
    print(20+65)
    print(100-900)
    print(20*96)
    print(100/4)
    print("I am" ,25 ,"years old")
    # Comments in Python
    '''This is a single line comment'''
    """This is a multi-line comment
    It can span multiple lines
    and is often used for documentation purposes"""
    #Variables
    x=10
    y="My name is Neymar"
    x="I am Love messi"
    print(x)
    print(y)
    print(type(x))
    print(type(y))
    b=20
    print(type(b))
    myvarialname=10
    print(myvarialname)
    my_name_is_neymar=20
    print(my_name_is_neymar)
    MYVARIALNAME=30
    print(MYVARIALNAME)
    # Assign Multiple Values
    X,Y,Z="brazil","argentina","france"
    print(X)
    print(Y)
    print(Z)
    x=y=z="Hello World"
    print(x)
    print(y)
    print(z)
    University=["Aiub","Aust","Aup"]
    print(University)
    #output with variables
    name="Neymar"
    age=30
    print("My name is",name,"and I am",age,"years old")
    x="Aiub"
    y="is a great university"
    print(x+" "+y)
    
    a=500
    
    def myfunc():
        a=300
        print("The number is", a)
    myfunc()
    print("The number is", a)
    
    #global variables
    b="I love Arentina"
    def myfunc():
        global b
        b="I love Brazil"
    myfunc()
    print(b)
    #pyton numbers
    x=10.52
    print(int(x))
    print(complex(x))
    print(float(x))
    
    import random
    print(random.randrange(1,10))
    
    #Python Strings
    
    a="Brazil,Argentina,France"
    print(a[0])
    print(len(a))
    b="I love Banglaseh"
    print("love" in b)
    print(b[2:6])
    print(b[:6])
    #Negative Indexing
    print(b[-5])
    print(b[-5:-2])
    #Python - Modify Strings
    a="Brazil Hexagon"
    print(a.upper())
    b="I LOVE MY MOTHER!      "
    print(b.lower())
    print(b.split(","))
    #The Walrus Operator
    num=[1,2,3,4,5]
    if(n:=len(num))>3:
        print(f"The list has {n} elements")
        age=[30,40,89,55,20]
    if (n:=len(age))>4:
        print(f"The list has {n} elements")
        #The Ternary Operator
        cgpa=2.50
        result="Probation" if cgpa<2.50 else "Not in Probation"
        print(result)
        age=20
        vote="Eligible to vote" if age>=18 else "Not eligible to vote"
        print(vote)
        # If statements
        a=20
        b=30
        if(a>b):
            print("a is greater than b")
num= 1
if num>0:
    print("The number is positive")
age=20
if(age>18):
    print("You Are an adulet")
    print("You can vote this elaction")
    
    #  a = int(input("Enter Your age:"))

if a < 60:
    print("Your Time Is Not Now To Retirement")
else:
    print("You Can Retire Now")
    
    login=True
    if login:
        print("Welcome back")
    else:
        print("Login falid")
        
        #Python Elif Statement
        a=20
        b=20
        if(a>b):
            print("a getaer than b")
        elif a==b:
            print("a Equal to b")
        mark=100
        if(mark>=90):
            print("Your grade is A+")
        elif(mark>=85):
            print("Your grade is A")
        elif(mark<=85):
            print("your grade is B+")
        
        #Python Shorthand If
        A=20
        b=30
        print("A") if a>b else print("B")
        
        x=20
        y=30
        print("X") if x>y else print("=") if a==b else print("Y")
        
        #Python Lists
country = ["Brazil", "Canada", "Bangladesh"]
print(country)
country= ["Brazil", "Canada", "Bangladesh","England"]
print(country)
print(len(country))
list1=["MA","Baba",20,False,39.09]
print(type(list1))

thisList=(list("Monitor","Dhaka",39,""))