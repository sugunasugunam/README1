class queue:
    def __init__(self):
        self.q=[]
        self.front=-1
        self.rear=-1
        
    def enqueue(self, val):
        self.q.append(val)
        if self.front==-1:
            self.front +=1
            self.rear +1
            print(val,"is successfully inserted")
        else:
            self.rear +=1
            print(val,"is successfully inserted")

    def dequeue(self):
        if len(self.q)==0:
            print("queue is empty")
            return
        else:
            temp=self.q.pop(self.front)
            print("deleted item=",temp)
            self.rear-=1
            if len(self.q)==0:
                self.front=-1
                self.rear=-1
                return

    def display(self):
        if len(self.q)==0:
            print("queue is empty")
            return
        print("the contents of queue are")
        if self.front==self.rear:
            print(self.q[self.front],"<== REAR")
            return
        print(self.q[self.front],"<== FRONT")
        i=self.front+1
        while i<self.rear:
            print(self.q[i])
            i=i+1
            print(self.q[self.front],"<== REAR")
a=queue()
a.enqueue(1)
a.enqueue(2)
a.display()
a.dequeue()
a.display()
a.dequeue()

