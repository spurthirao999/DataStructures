import LList_length


class Node:
	
	def __init__(self,data):
		self.data=data
		self.next=None
		
class LinkedList:
	
	def __init__(self):
		self.head=None
		

	def insert_node_at_beg(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node
		
	
			
	def length_list(self,node):
               
               if (not node):
                   return 0
               else:
                   return 1 + self.length_list(node.next)
                   
        
	def del_a_node(self,key):
	    temp=self.head
	    
	    if (temp is not None):
	       if(temp.data == key):
	           self.head=temp.next
	           temp=None
	           return
	           
	    while (temp is not None):
	        if(temp.data==key):
	            break
	            
	        prev=temp
	        temp=temp.next 
	        
	    if (temp==None):
	        return
	        
	    prev.next=temp.next
	    temp=None
	    
	def del_list(self):
	    current=self.head
	    
	    while(current):
	        next=current.next
	        del current.data
	        current=next
	      
	        
		
		
	def insert_node_at_end(self,new_data):
	    
	       new_node=Node(new_data)
	       
	       if self.head is None:
	           self.head=new_node
	           return
	       
	       current=self.head
	       
	       while (current.next):
	           current=current.next
	           
	       current.next=new_node
	       
        	       

		
	def printList(self):
		temp=self.head
		
		
		if temp is not None:
          	    while (temp):
         	      print(temp.data)
         	      temp=temp.next
         	      

		

		
if __name__=='__main__': 
	
	llist=LinkedList()
	llist.insert_node_at_beg(1)
	llist.insert_node_at_beg(2)
	llist.insert_node_at_end(3)
	#llist.insert_node_after(2,10)
	llist.insert_node_at_end(4)
	#llist.del_a_node(2)
	llist.printList()
	#llist.del_list()
	
	##Find the length of the list 
	count=llist.length_list(llist.head)
	print("COunt"+str(count))
		
	