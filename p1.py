''' Your script should contain three functions
1. push
2. pop
3. peep
User will be given choice to perform action from above three.
Script should be kept running until user chooses to exit.'''

class stack:
    def __init__(self,n):
        self.st = list()
        self.size = n
        self.i = -1
        
    def pop(self):
        if self.i == -1:
            print("stack is underflow")
            return 
        else:
            temp = self.st[-1]
            self.st.pop()
            self.i -=1
            return temp

    def push(self,data):
        if(self.i == self.size-1):
            print("stack overflow")
        else:
            self.st.append(data)
            self.i +=1
            print("Pused")

    def peep(self):
        return self.st[-1]






size = int(input("enter size of Stack :"))
stack_1 = stack(size)

while(True):
    inp = int(input("enter Number according bellow options : \n1.push \n2.pop \n3.peep \n4.exit"))
    if inp == 1:
        val = input("enter vale to push")
        stack_1.push(val)
    elif inp == 2:
        print(f" pop :{stack_1.pop()}")
    elif inp == 3:
        print(f"peep : {stack_1.peep()}")
    elif inp == 4:
        print("thank you")
        break
    else:
        print("please enter valid value.")
        
        