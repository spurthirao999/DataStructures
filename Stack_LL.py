class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:

    def __init__(self):
        self.head = None
        
        
    def push(self,new_data):
        
        if(self.head is None):
            self.head=Node(new_data)
        else:
            new_node=Node(new_data)
            new_node.next=self.head
            self.head=new_node
            
            
    def pop(self):
        if(self.head is None):
            return None
        else:
            pop_elem=self.head.data
            self.head=self.head.next
            return pop_elem
            
            
stack=Stack()
stack.push(1)
count=4
while(count >= 0):
    pop=stack.pop()
    stack.push(count)
    print("Pop:"+str(pop))
    count -=1

        
        