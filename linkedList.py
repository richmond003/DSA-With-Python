class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkConnection:
    def __init__(self):
        self._head = None
    
    # Add list to rear
    def addFront(self, item):
        newNode = Node(item)
        newNode.next = self._head
    
    def addToEnd(self, item):
        pass

    def removeFromFront(self):
        pass

    def removeFromRear(self):
        pass

    def getIndex(self, item):
        pass

    def _getPredeccessor(self, item):
        """ 
         Helper function to the previous data
           """
        pass
    def __len__(self):
        pass

    def contains(self):
        pass

    def delete(self, item):
        pass

    def insertAt(self, index, item):
        pass

    def insertBefore(self, target, item):
        pass

    def insertAfter(self, target, item):
        pass

    def insertListAt(self, target):
        pass

    def convertToList(self):
        pass

    def replace(self, oldItem, newItem):
        pass

    def replaceAll(self, oldList, newList):
        pass

    def reverse(self):
        pass

    def is_sorted(self):
        pass

    def sort(self):
        pass

    def  containSublist(self, otherList):
        pass







if __name__ == "__main__":
   pass 