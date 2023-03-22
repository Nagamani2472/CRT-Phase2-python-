#HEIGHT OF A TREE
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BSTree:
    arr1=[]
    def add_element(self,root,value):
        new_node=Node(value)
        if new_node.data<root.data:
             if root.left!=None:
                self.add_element(root.left,value)
                return
             else:
                root.left=new_node
                return
        else:
            if root.right!=None:
                self.add_element(root.right,value)
                return
            else:
                root.right=new_node
      
        
    def inorder(self,root):#7
        if root.left!=None:
            self.inorder(root.left)
        print(root.data)
        if root.right!=None:
            self.inorder(root.right)
        
    def preorder(self,root):
        print(root.data)
        if root.left!=None:
            self.preorder(root.left)
        if root.right!=None:
            self.preorder(root.right)
        
        
    def postorder(self,root):
        if root.left!=None:
            self.preorder(root.left)
        if root.right!=None:
            self.preorder(root.right)
        print(root.data)
    def sum(self,root):
        sum=root.data
        if root.left!=None:
            sum+=self.sum(root.left)
        if root.right!=None:
            sum+=self.sum(root.right)
        return sum
    def height(self,root):
        if root==None:
            return -1
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        return 1+ max(left_height,right_height)
        
    
ob=BSTree()
root=Node(10)
ob.add_element(root,7)
ob.add_element(root,40)
ob.add_element(root,5)
ob.add_element(root,9)
ob.add_element(root,8)
ob.add_element(root,15)
ob.add_element(root,60)
ob.inorder(root)
print(ob.sum(root.left))
print(ob.sum(root.right))
ob.height(root)
#SELECTION SORT
def selection(arr):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1,len(arr)):
            if arr[min_ind]>arr[j]:
                min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
    return arr
arr=list(map(int,input().split(',')))
print(*arr)
arr2=[]
arr2.append(selection(arr))
print(','.join(map(str,arr2)))
#INSERTION SORT
def insertion(arr):
    for i in range(len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr
arr=[5,2,4,3,1,7]
print(insertion(arr))
#BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
          if arr[j] > arr[j+1]:
           arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)

     


