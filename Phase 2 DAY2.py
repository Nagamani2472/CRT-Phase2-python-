#Linked list
class Node:
    def _init_(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def add_element_at_start(self,head,value):
        new_node=Node(value)
        new_node.next=head
        head=new_node
        return head
    def add_element_at_last(self, head, value):
        new_node = Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next=new_node
    def add_element_at_particular(self,head,value,pos):
        new_node=Node(value)
        curr=head
        prev=None
        while pos!=0:
            prev=curr
            curr=curr.next
            pos=pos-1
        prev.next=new_node
        new_node.next=curr
        
    def remove_element_at_last(self,head,value):
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next=None
    def print_list(self,head):
        temp = head
        while temp != None:
            print(temp.data,"->",end='')
            temp = temp.next
    def search_element(self, value):
        pass
obj = LinkedList()
head = Node(10)
obj.add_element_at_last(head, 20)
obj.add_element_at_last(head, 30)
obj.add_element_at_last(head, 40)
head=obj.add_element_at_start(head,50)
obj.add_element_at_particular(head,100,2)
obj.print_list(head)
#linked list taking user input
class Node:
    def _init_(self, value):
        self.data = value
        self.next = None
while(1):
    print("MENU")
    print("1.headnode   2.Insertion at beginning   3.insertion at ending    4.insertion at particular   5.deletion  6.printlist 7.exit ")
    choice=int(input())
    if choice==1:
        value=int(input())
        head=Node(value)
    elif choice==2:
        value=int(input())
        new_node=Node(value)
        new_node.next=head
        head=new_node
    elif choice==3:
        value=int(input())
        new_node = Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next=new_node
    elif choice==4:
        value=int(input())
        pos=int(input())
        new_node=Node(value)
        curr=head
        prev=None
        while pos!=0:
            prev=curr
            curr=curr.next
            pos=pos-1
        prev.next=new_node
        new_node.next=curr
    elif choice==5:
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next=None
    elif choice==6:
        temp = head
        while temp != None:
            print(temp.data)
            temp = temp.next
    elif choice==7:
        print("exited")
    else:
        print("invalid input")
# Reversing linked list
class Node:
    def _init_(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def add_element_at_start(self,head,value):
        new_node=Node(value)
        new_node.next=head
        head=new_node
        return head
    def add_element_at_last(self, head, value):
        new_node = Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next=new_node
    def add_element_at_particular(self,head,value,pos):
        new_node=Node(value)
        curr=head
        prev=None
        while pos!=0:
            prev=curr
            curr=curr.next
            pos=pos-1
        prev.next=new_node
        new_node.next=curr
    def reverse(self,head):
        cur=head
        prev=None
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    def remove_element_at_last(self,head,value):
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next=None
    def print_list(self,head):
        temp = head
        while temp != None:
            print(temp.data,"->",end='')
            temp = temp.next
    def search_element(self, value):
        pass
obj = LinkedList()
head = Node(10)
obj.add_element_at_last(head, 20)
obj.add_element_at_last(head, 30)
obj.add_element_at_last(head, 40)
head=obj.reverse(head)
obj.print_list(head)
#Reversing first half of the linked list
class Node:
    def _init_(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def add_element_at_last(self, head, value):
        new_node = Node(value)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next=new_node
    def reverse(self,head):
        first=head
        cur=head
        prev=None
        n=int(input())
        while n!=0:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            n-=1
        first.next=cur
        return prev
            
    def print_list(self,head):
        temp = head
        while temp != None:
            print(temp.data,"->",end='')
            temp = temp.next
    def search_element(self, value):
        pass
obj = LinkedList()
head = Node(10)
obj.add_element_at_last(head, 20)
obj.add_element_at_last(head, 30)
obj.add_element_at_last(head, 40)
head=obj.reverse(head)
obj.print_list(head)


