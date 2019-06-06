########################################################
# This contains the following:
# 1. Detect Loop and loop length
# 2. Middle element of the List
# 3. Print List from the end
# 4. Find odd/even list
###############################################################
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
        
    def find_middle_of_the_list(self,head):
         slow_temp=head
         fast_temp=head
         
         while(fast_temp and fast_temp.next):
               slow_temp=slow_temp.next
               fast_temp=fast_temp.next.next
             
         return slow_temp.data
             
         
        

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
                    
                    temp=slow
                    count=1
                    while(temp.next !=slow):
                        count +=1
                        temp=temp.next
                    
                    return count
                    
                    
    def print_list_from_end(self,head):
        
        if(not head):
            return
            
        temp=head
        self.print_list_from_end(temp.next)
        print(temp.data)
        
        
    def check_if_list_even_or_odd(self):
        curr=self.head
        
        while(curr and curr.next):
            curr=curr.next.next
            
        if(curr):
            print("Odd length")
        else:
            print("Even length list")
        
              
            
            

if __name__=='__main__': 
	
	llist=LinkedList()
	llist.insert_node_at_beg(1)
	llist.insert_node_at_beg(2)
	llist.insert_node_at_beg(3)
	llist.insert_node_at_beg(4)
	llist.insert_node_at_beg(5)
	llist.insert_node_at_beg(6)
	#llist.head.next.next.next.next.next = llist.head
	llist.printList()
	#count=llist.detectloop()
	#print("Loop length :"+str(count))
	middle_elem=llist.find_middle_of_the_list(llist.head)
	print("Middle_Elem"+str(middle_elem))
	print("Printing elements from end")
	llist.print_list_from_end(llist.head)
	llist.check_if_list_even_or_odd()



			