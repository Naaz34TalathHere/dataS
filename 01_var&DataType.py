# python is a implicit languaue

print("Hello naaz")
print(2+5)
name="naaz"
age=20
print("my name is",name,"and my age is",age)
print(type(name))

a=None
print(a)
print(type(a))
a=5
b=5
print(a+b)

# multiply string and number together
A,B=2,4
Txt="@"
print(A*Txt*B)
# string & string operation
A,B="2",3
Txt="@"
print((A+Txt)*B)# Strig and atring with + opeartor will join 
#print((A*Txt)*B) # string with string with*  and - operator error

# Numeric values can opearte with all arithematic operator
A,B=2,3
c=4
print(A+B*c)

# Arithematic expression with interger and float will result in float
A, B=10, 5.0
c=A*B
print(c)

# Result of division opearot with 2 integer will be float
A,B=10,5
c=A/B
print(c) # float value
 # // will produce float value even if the result is int 
A, B=1.5,3
c=A//B
print(c)

a,b=12,52
c=a//B
print(c) # give closes value 

 # REMAINDER IS NEGATIVE WHEN DENOMINATOREE IS NEGATIVE
# + % + = +
# + % - = -
# - % - = +
# - % + = +
a, b= -5, 2
c=a%b               #-5/2 = +
print(c)

a,b=5,2
c=a%b              # + /+ = +
print(c)

a,b=5,-2
c=a%b               # +/- = -
print(c)

#COMMENT LINE
# Single line
"""
Multi line
"""

# INPUT STATEMENT ()

name= input("name:")
age=input("age:")
print("My name is ",name +"age is ",age)

#CONDITONAL STATMENT
# if , elif , else

Light=input("light:")
if (Light=="red"):
    print("stop")
elif(Light=="green"):
    print("Go")
elif(Light=="yellow"):
    print("Wait")
else:
    print("light broken")

marks=int(input("marks:"))
if(marks>=90):
    print("A+")
elif(marks>=80 and marks<90):
    print("B+")
elif(marks>=70 and marks <80):
     print("C+")
else:
    print("Fail")

# single line conditon
food=input("food:")
eat="yes" if food=="cake" else"no"
print(eat)

