'''   Implement Circular Queue
You script should contain four functions
1. Front: Get the front item from queue.
2. Rear: Get the last item from queue.
3. enqueue(value)
4. dequeue()
User will be given choice to perform action from above four.
Script should be kept running until user chooses to exit. '''

class CirculatrQueue:
    
    def __init__(self,size):
        self.q = list()
        self.size=size
        self.cnt = 0
        
    def enqueue(self,value):
        if self.cnt == self.size:
            print("circular Queue is overfull")
            return
        else:
            self.cnt+=1
            self.q.append(value)
            return
       
             
    def deqeue(self):
        if self.cnt == 0:
            print("queue is empty")
            return
        else:
            temp = self.q[0]
            self.cnt -=1
            self.q.pop(0)
            return temp
        
    def front(self):
        return self.q[0]

    def rear(self):
        return self.q[-1]
        


sz = int(input("enter size of circular Queue :"))
sq = CirculatrQueue(sz)
# q = Queue(3)

while(True):
    inp = int(input("enter Number according bellow options : \n1.enqueue \n2.deqeue \n3.front \n4. rear \n5.exit"))
    if inp == 1:
        val = input("enter vale to push")
        sq.enqueue(val)
    elif inp == 2:
        print(f" deqeue :{sq.deqeue()}")
    elif inp == 3:
        print(f"front : {sq.front()}")
    elif inp == 4:
        print(f"rear : {sq.rear()}")
    elif inp == 5:
        print("thank you")
        break
    else:
        print("please enter valid value.")