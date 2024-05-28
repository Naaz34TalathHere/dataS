def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum
cal_sum(2,3)

def mul(a,b):
    mul=a*b
    return mul
   
sum=mul(2,5)
print(sum)

def print_hello():
    print("hello")
print_hello()

def naaz():
    print("nazu")

naaz()

def sum_avg(a,b,c):
    avg=a+b+c/3
    print(avg)

sum_avg(2,2,2)

def div (a=4,b=2):
    print(a/b)
    return
div()

'''cities =['delh','mum','bng','mum']
hero=['naaz','nazu','tala']
def city_count(list):
    print(len(list))
    print(cities)
    return
city_count(cities)
city_count(hero)
n=5'''
'''i=5
def cal_fac(n):
    fact=1
    for i in range(1,n+1):
        fact *=1
    print(fact)

cal_fac(6)

def con_INR(usd_val):
    inr=usd_val *83
    print(usd_val,"USD",inr,"INR")
con_INR(73)

num=int(input("Enter a numbr"))
def num_1 (num):
    if num%2==0:
        print("even")
    else:
        print("odd")
num_1(num)'''
 # RECURSION


def show(n):
    print(n)
show(5)
show(7)