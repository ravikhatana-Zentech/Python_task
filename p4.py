'''Selection sort
Use a static list 
Use selection sort to sort this list'''

# selection
li = [5,3,2,8]
print(li)
for i in range(len(li)):
    small = i
    for j in range(i,len(li)):
        if li[small]>li[j]:
            small = j
    if small<li[0]:
        temp = li[i]
        li[i] = li[small]
        li[small] = temp
print(li)