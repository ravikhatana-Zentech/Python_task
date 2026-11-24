'''
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
'''

temp = 1
n = 5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    temp = 1
    print(f"{temp} ",end="" )
    for j in range(1,i):
        temp = temp * (i-j)
        temp = temp//j
        print(f"{temp} ",end="")
    print()