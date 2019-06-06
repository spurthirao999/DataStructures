# This program is to add two numbers represented by a linked list
#Given two numbers represented by two lists, write a function that
#returns sum list. The sum list is list representation of 
#addition of two input numbers.

#Input:
 # First List: 5->6->3  // represents number 365
 # Second List: 8->4->2 //  represents number 248
#Output
 # Resultant list: 3->1->6  // represents number 613
 
 
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

    def addTwoNumbers(self, l1, l2):
        
        if(l1 is None or l2 is None):
            return
        
        head1=l1
        head2=l2
        carry=0
        prev=None
        
        while(head1 or head2):
            firstval=0 if head1 is None else head1.data
            secondval=0 if head2 is None else head2.data
            
            sum=carry + firstval + secondval
            carry=1 if sum>=10 else 0
            sum=sum if sum<10 else sum%10
            
            temp=Node(sum)
            print("Sum" + str(sum))
            
            
            if self.head is None:
                self.head=temp
            else:
                prev.next=temp
            
            prev=temp
            if head1 is not None:
                head1=head1.next
            if head2 is not None:
                head2=head2.next
                
            
        if carry > 0:
            print("Carry",carry)
            temp.next=Node(carry)
            
                
        
                
llist=LinkedList()
llist.insert_node_at_beg(9)
llist.insert_node_at_beg(9)
llist.insert_node_at_beg(9)
llist1=LinkedList()
llist1.insert_node_at_beg(9)
llist1.insert_node_at_beg(8)

#llist1.insert_node_at_beg(2)
llist.printList()
print("List2")
llist1.printList()  
print("*****")
llist3=LinkedList()
llist3.addTwoNumbers(llist.head,llist1.head) 
#llist1.printList() 
print("Resultant List") 
llist3.printList()     