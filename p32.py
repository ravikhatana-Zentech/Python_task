
'''
 1 
 2  3 
 4  5  6 
 7  8  9  10 
'''

num = int(input("enter Number :"))
cnt = 1
for i in range (num-1):
    for j in range(i+1):
        print(f" {cnt} ",end="")
        cnt+=1

    print()