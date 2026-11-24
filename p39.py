# Linear Search

li = [12,11,10,7,8,9,20]
element = 20
for i in range(len(li)):
    if li[i] == element:
        print(f"index : {i}")
        break
else:
    print("not in list")