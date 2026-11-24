'''
 *                 * 
 *  *           *  * 
 *  *  *     *  *  * 
 *  *  *  *  *  *  *

'''

num = int(input("enter number "))
# num = num-2
temp = 1
space = num-2
for i in range(1,num):
    for j in range(i):
        print(" * ",end="")
    for p in range(space):
        print("   ",end="")
    if space <= 0:
        i -= 1
    for k in range(i):
        print(" * ",end="")
    print()
    if(space <= 0):
        break
    space-=2
    # temp+=1

    