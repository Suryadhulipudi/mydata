class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None
        

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_after_node(self,data,x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        
        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def add_before_node(self,data,x):
        if self.head is None:
            print("LinkedList is empty")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref
        
        if n is None:
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
   
    def delete_by_value(self,x):
        if self.head is None:
            print("Can't delete LL is empty")
            return
        if x==self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref
        
    

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_begin(20)
LL1.delete_by_value(100)
LL1.print_LL()
