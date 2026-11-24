'''
 5  4  3  2  1 
 4  3  2  1 
 3  2  1 
 2  1 
 1 

'''
num = int(input("enter number :"))
temp = num
for i in range(1,num+1):
    for j in range(temp,0,-1):
        print(f" {j} ",end="")
    print()
    temp-=1