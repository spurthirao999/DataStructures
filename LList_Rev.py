class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node_at_beg(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr=curr.next

    def rev(self):
        prev=None
        curr=self.head
        
        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        
    def recursive_rev(self,curr):
        if(self.head is None):
            return
            
        first=curr
        rest=first.next
        
        if(rest is None):
            return
        
        print ("recur:"+str(rest.data))
        self.recursive_rev(rest)
        first.next.next=first
        first.next=None
        self.head=rest
        
        
if __name__=='__main__': 
	
	llist=LinkedList()
	llist.insert_node_at_beg(1)
	llist.insert_node_at_beg(2)
	llist.insert_node_at_beg(3)
	llist.insert_node_at_beg(4)
	llist.printList()
	print("After Reversing")
	llist.rev()
	llist.printList()
	print("After Reversing with recursion")
	llist.recursive_rev(llist.head)
	llist.printList()