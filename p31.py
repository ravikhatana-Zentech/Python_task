'''
*****
****
***
**
*
'''


num = int(input("enter Number :"))
for i in range (num):
    for j in range(num,i,-1):
        print("*",end="")

    print()