#TREE TRAVERSAL
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BSTree:
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
        
        
    def levelorder(self,root):
        q = []
        q.append(root)
        while len(q)!=0:
            ele=q.pop(0)
            print(ele.data,end=",")
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            ele=q.pop(0)
            print(ele.data)
ob=BSTree()
root=Node(10)
ob.add_element(root,7)
ob.add_element(root,40)
ob.add_element(root,5)
ob.add_element(root,9)
ob.add_element(root,15)
ob.add_element(root,60) 
ob.inorder(root)
print("inorder completed")
ob.preorder(root)
print("preorder completed")
ob.postorder(root)
print("postorder completed")
#DOUBLE LINKED LIST
