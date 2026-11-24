''' Find the factors of a number opimize it as much as you can'''

num = int(input("enter number"))
factors = list()
for i in range(1,num+1):
    if num%i == 0:
        factors.append(i)
print(factors)
