'''
A 
B B 
C C C 
D D D D 
E E E E E
'''

val = 65
n = int(input("please enter positive number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{chr(val)} ",end="")
    val +=1
    print()