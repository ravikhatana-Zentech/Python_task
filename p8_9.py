'''Matrix Multiplication
1. Take two 3x3 matrix.
2. take user inputs to fill it up.
3. Multiply them both and store it in another 3x3 matrix.
4. Display the result.


Find diterminent of 3x3 matrix
'''

# matrix
# m1 = list([[1,2,3],[4,5,6],[7,8,9])
# m2 = list([[9,8,7],[6,5,4],[3,2,1]])
m1 = []
m2 = []
ans = list()
print("enter values of first matrix ")
for i in range(3):
    temp = list()
    for j in range(3):
        ele = int(input())
        temp.append(ele)
    m1.append(temp)
print(m1)

print("enter values of second matrix ")
for i in range(3):
    temp = list()
    for j in range(3):
        ele = int(input())
        temp.append(ele)
    m2.append(temp)
print(m2)

for i in range(3):
    temp = list()
    for j in range(3):
        sm = 0
        for k in range(3):
            sm += m1[i][k]*m2[k][j]
        temp.append(sm)
    ans.append(temp)


print(f"Multiplication : {ans}")


dit = (
    ans[0][0] * ((ans[1][1] * ans[2][2]) - (ans[1][2] * ans[2][1]))
    - ans[0][1] * ((ans[1][0] * ans[2][2]) - (ans[1][2] * ans[2][0]))
    + ans[0][2] * ((ans[1][0] * ans[2][1]) - (ans[1][1] * ans[2][0]))
)


print(f"Diterminent : {dit}")
