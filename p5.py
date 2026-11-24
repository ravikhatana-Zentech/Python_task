'''Bubble sort
Use a static list 
Use bubble sort to sort this list'''

# Bubble sort
li = [5,3,2,8]
print(li)
for i in range(len(li)):
    for j in range(len(li)-1):
        if li[j]>li[j+1]:   
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
print(li)
