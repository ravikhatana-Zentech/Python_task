'''Binary search
Use a static list 
Use Binary search to find element asked by user
Use one of the sorting algorithm that you have developed to sort list here'''

# Binary search

li = [1,2,3,4,5,6,7,8,9,10]
num = 9

left = 0
right = len(li) - 1

while left <= right:
    mid = (right + left) // 2
    # print(mid)

    if li[mid] == num:
        print("Found at index:", mid)
        break

    elif li[mid] > num:
        right = mid - 1

    else:
        left = mid + 1

else:
    print("Element not found")