'''
 Create a Tic Tac Toe game in python.
1. You should be able to play with two players.
2. You should be able to play against computer.
After you complete simple game implement it in a way that computer never loses. 
'''

import random

def cheak(val,matrix,pos):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == pos:
                matrix[i][j] = val
                break
    # else:
    #     print("not valid value you lost chanse")

    for out in matrix:
        for inner in out:
            print(f" {inner} ", end = "")
        print()
    win_cross_1 = 0
    win_cross_2 = 0
    # win_row = 0
    # win_col = 0
    # col = 0
    for i in matrix:
        if i.count(val) == 3:
            return True
            
    for i in range(3):
        col = 0
        win_col = 0
        
        for j in range(3):
            if(i==j and matrix[i][j] == val):
                win_cross_1+=1
                if win_cross_1 == 3:
                    return True
            elif(i+j==2 and matrix[i][j] == val):
                win_cross_2+=1
                if win_cross_2 == 3:
                    return True
            else:
                for k in range(3):
                    if(matrix[j][k] == val and col == k):
                        win_col+=1
                        if win_col == 3:
                             return True
                col+=1        
                
            # else:
            #     pass
            # if(matrix[j][i] == val):
            #     win_col+=1
            #     if win_col == 3:
            #         return True
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
li = [1,2,3,4,5,6,7,8,9]

for k in matrix:
    for p in k:
        print(f" {p} ", end = "")
    print()
select  = int(input("enter No with whome you want to play \n1. with ffrind \n2.with computer:"))
if select == 1:
    while True:
        if li == []:
            print("game is over")
            break
        a = int(input("player A, enter Number where you want x :"))
        li.remove(a)
        
        print("-------------------")
        ans = cheak("x",matrix,a)
        print("-------------------")
        if ans:
            print("congratulation player A(x) win....")
            print("--------------------------------------------------")
            
            break
        
        
                # else:
                #     print("please enter valid ")
        if li == []:
            print("game is over")
            break
        b = int(input("player B, enter Number where you want o :"))
        li.remove(b)
        
        print("--------------------------------------------------")
        ans = cheak("o",matrix,b)
        print("--------------------------------------------------")
        if ans:
            print("congratulation player B(o) win....")
            print("--------------------------------------------------")
            break

            
elif select == 2:
    while True:
        if li == []:
            print("game is over")
            break
        a = random.choice(li)
        print(f"player A(x):computer :{a}")
        li.remove(a)
        print("-------------------")
        ans = cheak("x",matrix,a)
        print("-------------------")
        if ans:
            print("congratulation player A(x) win....")
            print("--------------------------------------------------")
            break
                # else:
                #     print("please enter valid ")
        if li == []:
            print("game is over")
            break
        b = int(input("player B, enter Number where you want o :"))
        li.remove(b)
        print("--------------------------------------------------")
        ans = cheak("o",matrix,b)
        print("--------------------------------------------------")
        if ans:
            print("congratulation player B(o) win....")
            print("--------------------------------------------------")
            break            
else:
    print("please enter valid choice.")
    