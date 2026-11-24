'''
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
'''

n = int(input("please enter positive number"))
for i in range(n,0,-1):
    for k in range(n,i-1,-1):
        print(" ",end=" ")
    for j in range(i,1,-1):
        print("* ",end="")
    for p in range(i):
        print("* ",end= "")
    print()


    