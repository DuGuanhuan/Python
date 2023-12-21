class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key

        self.payload = val

        self.leftChild = left

        self.rightChild = right

        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None

            else:
                self.parent.rightChild = None

        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild

                else:
                    self.parent.rightChild = self.leftChild

                self.leftChild.parent = self.parent

            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild

                else:
                    self.parent.rightChild = self.rightChild

                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None

        if self.hasRightChild():
            succ = self.rightChild.findMin()

        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent

                else:
                    self.parent.rightChild = None

                    succ = self.parent.findSuccessor()

                    self.parent.rightChild = self

        return succ

    def findMin(self):
        current = self

        while current.hasLeftChild():
            current = current.leftChild

        return current

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key

        self.payload = value

        self.leftChild = lc

        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self

        if self.hasRightChild():
            self.rightChild.parent = self

    # This is the overload built-in function to print the object to a string

    # It outputs the tree node object to the string

    # For example, a node "b" has "c" as the left node, "d" as the right node and "a" as the parent node.

    # The output is "Node:[Key:1,value:B],Left Child:[key:1,value:C],Right Child:[key:1,value:C],Parent:[key:1,value:A]"

    # please beware the space between "Left" and "Child", also between  "Right" and "Child". It may lead to an incorrect answer due to the auto marking process. No mark will be awarded. If the answer does not match.

    # please also noted that the answer is case sensitive as well.

    # Please write your code here
    def __str__(self):
        left = (
            f"Left Child:[key:{self.leftChild.key},value:{self.leftChild.payload}]"
            if self.hasLeftChild()
            else "Left Child:None"
        )
        right = (
            f"Right Child:[key:{self.rightChild.key},value:{self.rightChild.payload}]"
            if self.hasRightChild()
            else "Right Child:None"
        )
        parent = (
            f"Parent:[key:{self.parent.key},value:{self.parent.payload}]"
            if self.parent
            else "Parent:None"
        )
        return f"Node:[Key:{self.key},value:{self.payload}],{left},{right},{parent}"
