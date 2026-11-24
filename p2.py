''' Implement Queue
You script should contain three functions
1. enqueue
2. dequeue
3. peek 
User will be given choice to perform action from above three.
Script should be kept running until user chooses to exit.'''

class Queue:
    
    def __init__(self,size):
        self.q = list()
        self.size=size
        self.i_r = -1
        self.i_f = -1
        
    def enqueue(self,value):
         if self.i_f == -1:
             self.i_f = 0
             self.i_r = 0
             self.q.append(value)
             return
         if(self.i_r == self.size-1):
            print("Queue overflow")
            return
         else:
             self.q.append(value)
             self.i_r +=1
             return
             
    def deqeue(self):
        if self.i_f == -1:
            print("queue is empty")
            return
        else:
            temp = self.q[0]
            self.i_f +=1
            if self.i_f == self.size:
                self.i_f = -1
                self.i_r = -1
            self.q.pop(0)
            return temp
        
    def peek(self):
        return self.q[-1]
        



s = int(input("enter size of Queue :"))

q = Queue(s)

while(True):
    inp = int(input("enter Number according bellow options : \n1.enqueue \n2.deqeue \n3.peek \n4.exit"))
    if inp == 1:
        val = input("enter vale to push")
        q.push(val)
    elif inp == 2:
        print(f" pop :{q.pop()}")
    elif inp == 3:
        print(f"peep : {q.peek()}")
    elif inp == 4:
        print("thank you")
        break
    else:
        print("please enter valid value.")