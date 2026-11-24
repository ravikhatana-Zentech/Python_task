'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *
'''

n = int(input("please enter positive number"))
for i in range(n):
    for k in range(n,i+1,-1):
        print("  ",end="")
    for j in range(i+1):
        print("* ",end="")
    for j in range(i):
        print("* ",end="")
    print()