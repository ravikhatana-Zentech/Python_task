'''
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      *

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