class Node:
#{
    """
    Representing a node consisting of
    - datum: the datum stored at the node
    - next: reference to the next node
    """

    def __init__(self, datum, next):
    #{
        self.datum = datum
        self.next = next
    #}

#}

class MyLinkedList:
#{
    """
    Implementation of a linked list
    that connect firstNode -> node -> node -> ... -> NULL
    """
    def __init__(self):
    #{
        """
        Constructs an empty linked list
        """
        self.firstNode = None
    #}

    def insertFirst(self, datum):
    #{
        """
        Inserts a node holding the datum at the beginning of this list.
        """
        # create a new node
        newNode = Node(datum=datum, next=self.firstNode)

        # set the new node to be the first node of the list
        self.firstNode = newNode
    #}

    def getLastNode(self):
    #{
        """
        Returns the last node of this list.
        If the list is empty then returns None
        """

        # start at the first node
        node = self.firstNode

        # travel down the list
        while (node != None) and (node.next != None):
            node = node.next

        return node
    #}

    def getLength(self):
    #{
        """
        Returns the length of the list.
        If the list is empty then returns 0.
        """

        # counting number of nodes
        count = 0

        # start at the first node
        node = self.firstNode

        # travel down the list and increase count
        while node != None:
        #{
            node = node.next
            count = count + 1
        #}

        return count
    #}

    def getNode(self, index):
    #{
        """
        Returns the node at the specified index in this list.
        Returns None if there is no node at that position.
        Index 0 refers to the first node.
        """

        # start at the first node
        node = self.firstNode
        i = 0

        # travel down the list until the index
        while (i < index) and (node != None):
        #{
            node = node.next
            i = i + 1
        #}

        return node
    #}

    def removeFirst(self):
    #{
        """
        Removes the first node of this list and return its datum.
        Returns None if the list is empty.
        """

        # if the list is empty
        if (self.firstNode == None):
            return None

        # get the first datum
        firstDatum = self.firstNode.datum

        # reset the first node of this list
        self.firstNode = self.firstNode.next

        return firstDatum



    def __str__(self):
        element =[]
        current_node = self.firstNode
        while current_node:
            element.append(str(current_node.datum))
            current_node = current_node.next
        return  "MyLinkedList["+ '->'.join(element)+ "]"
    #}
#}




linkedListObj = MyLinkedList()
linkedListObj.insertFirst(10)
linkedListObj.insertFirst(20)
linkedListObj.insertFirst(30)
