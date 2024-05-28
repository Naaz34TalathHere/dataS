#

'''n=int (input("enter n number"))
i=1
while i<=10:
    print(i)
    i+=1'''

'''nums =[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx <len(nums):
    print(nums[idx])
    idx+=1'''

hero=['iron','man','mos']
idx=0
while idx<len(hero):
    print(hero[idx])
    idx+=1


'''num=(1,34,9,16,25,36,49,64,81,100)
x=int(input("Enter the num to search"))
i=0
while i<len(num):
    if(num[i]==x):
        print("found at ",i)
    i+=1 '''

# BREAK AND CONTINUE 
'''i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1'''


'''i=0
while i<=5:
   
    if(i==3):
        i+=1
        continue # skip the current iteraton
    print(i)
    i+=1

i=0
while i <=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
 
val=[1,2,3]
for i in val:
    print(i)

veggie=["poyayo","onione","tomato"]
for i in veggie :
    print(i)

tup=(1,2,3,4,5)
for num in tup:
    print(num)

name="naaz"
for i in name:
    print(i)'''

'''num=[1,4,9,16,25,36,49,64,81,100]
x=16
i=0
while i<len(num):
    if(num[i]==16):
        i+=1
        print("found")
        break
    print(num[i])
    i+=1

for i in range(5):
    print(i)

for i in range(1,13,2): # strat , stop , step 
    print(i)'''

n=5
for i in range(1,n+1):
    print(i)

sum =0
for i in range(1,n+1):
    sum+=1