class TreeNode:

    def __init__(self,key,val,left=None,right=None,parent=None):

        self.key = key

        self.payload = val

        self.leftChild = left

        self.rightChild = right

        self.parent = parent

    def hasLeftChild(self):

    def hasRightChild(self):

    def isLeftChild(self):

    def isRightChild(self):

    def isRoot(self):

    def isLeaf(self):

    def hasAnyChildren(self):

    def hasBothChildren(self):

    def spliceOut(self):

    def findSuccessor(self):

    def findMin(self):

    def replaceNodeData(self,key,value,lc,rc):

    def __str__(self):
 
 # Assumed that all the above methods in Treenode had been implemented.



    # This is the overload built-in iteration function that iterates each node in the left child node and the right child node. 

    def __iter__(self):                 

    # add you code here  

class BinarySearchTree:

    def __init__(self):

        self.root = None

        self.size = 0

    def length(self):

        return self.size

    def __len__(self):  # print (len(mytree))

        return self.size

    def put(self,key,val):

        if self.root:

            self._put(key,val,self.root)

        else:

            self.root = TreeNode(key,val)

        self.size = self.size + 1

    def _put(self,key,val,currentNode):

        if key < currentNode.key:

            if currentNode.hasLeftChild():

                   self._put(key,val,currentNode.leftChild)

            else:

                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)

        else:

            if currentNode.hasRightChild():

                   self._put(key,val,currentNode.rightChild)

            else:

                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):  #  mytree[3]="red" : k=3 v="red" 

       self.put(k,v)

    def get(self,key):

       if self.root:

           res = self._get(key,self.root)

           if res:

                  return res.payload

           else:

                  return None

       else:

           return None

    def _get(self,key,currentNode):

       if not currentNode:

           return None

       elif currentNode.key == key:

           return currentNode

       elif key < currentNode.key:

           return self._get(key,currentNode.leftChild)

       else:

           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):  # print(mytree[6]): key = 6

       return self.get(key)

    def __contains__(self,key): # print(3 in mytree): key = 3

       if self._get(key,self.root):

           return True

       else:

           return False

    def delete(self,key):

      if self.size > 1:

         nodeToRemove = self._get(key,self.root)

         if nodeToRemove:

             self.remove(nodeToRemove)

             self.size = self.size-1

         else:

             raise KeyError('Error, key not in tree')

      elif self.size == 1 and self.root.key == key:

         self.root = None

         self.size = self.size - 1

      else:

         raise KeyError('Error, key not in tree')

    def __delitem__(self,key): # del mytree[3] : key = 3

       self.delete(key)

    def remove(self,currentNode):

         if currentNode.isLeaf(): #leaf

           if currentNode == currentNode.parent.leftChild:

               currentNode.parent.leftChild = None

           else:

               currentNode.parent.rightChild = None

         elif currentNode.hasBothChildren(): #interior

           succ = currentNode.findSuccessor()

           succ.spliceOut()

           currentNode.key = succ.key

           currentNode.payload = succ.payload

         else: # this node has one child

           if currentNode.hasLeftChild():

             if currentNode.isLeftChild():

                 currentNode.leftChild.parent = currentNode.parent

                 currentNode.parent.leftChild = currentNode.leftChild

             elif currentNode.isRightChild():

                 currentNode.leftChild.parent = currentNode.parent

                 currentNode.parent.rightChild = currentNode.leftChild

             else:

                 currentNode.replaceNodeData(

                    currentNode.leftChild.key,currentNode.leftChild.payload,

                    currentNode.leftChild.leftChild,currentNode.leftChild.rightChild)

           else:

             if currentNode.isLeftChild():

                 currentNode.rightChild.parent = currentNode.parent

                 currentNode.parent.leftChild = currentNode.rightChild

             elif currentNode.isRightChild():

                 currentNode.rightChild.parent = currentNode.parent

                 currentNode.parent.rightChild = currentNode.rightChild

             else:

                 currentNode.replaceNodeData(

                   currentNode.rightChild.key,currentNode.rightChild.payload,

                   currentNode.rightChild.leftChild,currentNode.rightChild.rightChild)

    def __str__(self):

        return str(self.root)

   # This is the overload built-in iteration function that iterates the key of the nodes in the BinarySearchTree object. 

    def __iter__(self): 

        if self.root:

            for elem in self.root:

                yield elem

