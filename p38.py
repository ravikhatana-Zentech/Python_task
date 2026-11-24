"""
*       *       *
 *     * *     * *
  *   *   *   *   *
   * *     * *     *
    *       *       *
"""

num = int(input("enter number :"))
temp = 0
for i in range(1,num+1):
    for j in range(1,(num*5)+1):
        if(i==j or j == (num*2)-i or j == (num*2)+i-2 or j == (num*4)-i-2 or j == (num*4)+i-4):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    temp+=1