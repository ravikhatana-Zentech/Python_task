'''Insertion sort
Use a static list 
Use insertion sort to sort this list'''

# insertion
li = [5,3,2,8]
print(li)
temp = 0
for i in range(len(li)):
    # if li[0] > li[i]:
    for k in range(i,0,-1):
        if li[k]<li[k-1]:
            temp = li[k]
            li[k]=li[k-1]
            li[k-1] = temp
print(li)

