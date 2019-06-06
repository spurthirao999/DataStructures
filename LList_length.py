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

    def detectloop(self):
        slow=self.head
        fast=self.head
        
        while (slow and fast and fast.next):
                slow=slow.next
                fast=fast.next.next
                
                if(slow == fast):
                    print("Loop detected")
                    return
              
            
            

if __name__=='__main__': 
	
	llist=LinkedList()
	llist.insert_node_at_beg(1)
	llist.insert_node_at_beg(2)
	llist.insert_node_at_beg(3)
	llist.insert_node_at_beg(4)
	llist.insert_node_at_beg(5)
	llist.head.next.next.next.next.next = llist.head
	#llist.printList()
	llist.detectloop()



			