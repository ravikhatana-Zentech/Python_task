'''

        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5 
'''

n = int(input("please enter positive number"))
val = 1
for i in range(n):
    temp = val
    for k in range(n,i+1,-1):
        print("  ",end="")
        
    for j in range(i+1):
        print(f"{temp} ",end="")
        temp+=1
        
    for j in range(i):
        print(f"{temp-2} ",end="")
        temp-=1
    val = val+1 
    print()

    