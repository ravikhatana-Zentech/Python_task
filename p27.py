'''
1    2    3    4
12   13   14   5
11   16   15   6
10   9    8    7
'''

row = 6
col = 5
matrix = list()
for i in range(row):
    temp = list()
    for j in range(col):
        temp.append(0)
    matrix.append(temp)
# print(matrix)

top = 0
left = 0
bottum = row-1
right = col-1
cnt = 1
# top == bottum or right == left
while (top<=bottum and right>=left):
    for i in range(left,right+1):
        matrix[top][i]=cnt
        cnt+=1
    top+=1
    for k in range(top,bottum+1):
        matrix[k][right] = cnt
        cnt+=1
    right-=1

    for j in range(right,left-1,-1):
        matrix[bottum][j]=cnt
        cnt+=1
    bottum-=1

    for l in range(bottum,top-1,-1):
        matrix[l][left]=cnt
        cnt+=1

    left+=1
    # break
    
for i in matrix:
    print(i)