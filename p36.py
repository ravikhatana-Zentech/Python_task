'''
 *  *  *  *  *  *  * 
 *  *  *     *  *  * 
 *  *           *  * 
 *                 *

'''

num = int(input("enter number :"))
space = -1
for i in range(1,num-2):
    
    for j in range(i,(num//2)+2):
        print(f" * ", end="")
     
    for k in range(space):
        print("   ",end="")
    if i == 1:
        i += 1
    for p in range(i,(num//2)+2):
        print(f" * ", end="")
    print()
    if space == num-2:
        break
    space+=2