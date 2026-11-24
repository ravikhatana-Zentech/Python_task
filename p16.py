'''
Rearrange array such that A[A[i]] is set i for every element A[i]
Input:{1, 3, 4, 2, 0}
Output:{4, 0, 3, 1, 2}
Explanation:
A[0] = 1, A[1] becomes 0
A[1] = 3, A[3] becomes 1
A[2] = 4, A[4] becomes 2
A[3] = 2, A[2] becomes 3
A[4] = 0, A[0] becomes 4
'''

inp = "13420"
output = list("01234")
cnt = 0
for i in inp:
    output[int(i)]=cnt
    cnt+=1
print(f"{output}")