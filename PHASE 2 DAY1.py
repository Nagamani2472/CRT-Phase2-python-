#IMPLEMENTATION OF STACK
class Stack:
    arr=[]
    size=5
    def stack_push(self,element):
        self.arr.append(element)
    def stack_pop(self):
        self.arr.pop()
    def stack_peek(self):
        return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
s=Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
print(s.arr)
s.stack_pop()
s.stack_pop()
print(s.arr)
s.stack_peek()

#STACK OVERFLOW AND UNDERFLOW
class Stack:
    arr=[]
    size=5
    def stack_push(self,element):
        if len(self.arr)==self.size:
            print("Stack is full")
        else:
            self.arr.append(element)
    def stack_pop(self):
        if len(self.arr)==0:
            print("Stack is empty")
        else:
            self.arr.pop()
s=Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
s.stack_push(50)
s.stack_push(60)
print(s.arr)
s.stack_pop()
s.stack_pop()
s.stack_pop()
s.stack_pop()
s.stack_pop()
s.stack_pop()
print(s.arr)
#IMPLEMENTATION OF QUEUE
class Queue:
    arr=[]
    size=5
    def enQueue(self,element):
        self.arr.append(element)
    def deQueue(self):
        self.arr.pop(0)
    def Queue_peek(self):
        return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
q=Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
print(q.arr)
q.deQueue()
q.deQueue()
print(q.arr)
q.Queue_peek()
#LINEAR SEARCH
arr=[]
flag=0
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
print(arr)
k=int(input())
for i in range(len(arr)):
    if k==arr[i]:
        print("element found at",i)
        flag=1

if flag==0:
    print("element not found")
        
        
#STACK OPERATIONS
    class Stack:
    arr=[]
    arr1=[]
    def stack_push(self,element):
        self.arr.append(element)
    def stack_pop(self):
        self.arr.pop()
s=Stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
s.stack_push(40)
print(s.arr)

