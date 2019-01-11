# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:40:01 2018

@author: Swetha Srikanthan
"""


# Node class 
class Node: 

	# Function to initialize the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 

# Linked List class 
class LinkedList: 
	
    # Function to initialize the Linked List object 
    def __init__(self): 
        self.head = None

    #insert at beginning
    def push(self, new_data):
        #code
        nnode = Node(new_data)
        nnode.next = self.head
        self.head = nnode
    
    # This function is in LinkedList class. 
    # Inserts a new node after the given prev_node. This method is  
    # defined inside LinkedList class shown above */ 
    def insertAfter(self, prev_data, new_data): 
        #code
        nnode = Node(new_data)
        if self.head == None:
            self.head = nnode
            return
        temp = self.head
        while(temp.next != None):
            if (temp.data == prev_data):
                break
            temp = temp.next
        nnode.next = temp.next
        temp.next = nnode
            
    
    #add at last
    def append(self, new_data): 
        #code
        nnode = Node(new_data)
        if self.head == None:
            self.head = nnode
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        nnode.next = temp.next
        temp.next = nnode
        
    def delete_node(self, val):
        #code
        if self.head == None:
            return
        
        if self.head.data == val:
            self.head = self.head.next
            return
            
        temp = self.head
        while(temp.next != None):
            if temp.next.data == val:
                temp.next = temp.next.next
                break
            temp = temp.next
        
    def delete_node_pos(self, pos):
        #code        
        if self.head == None:
            return
        
        if pos == 1:
            self.head = self.head.next
            return
            
        temp = self.head
        temp_pos = 1  
        
        while(temp.next != None):
            if temp_pos + 1 == pos:
                temp.next = temp.next.next
                break
            temp = temp.next
 
    # Utility function to print the linked list 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data) 
            temp = temp.next
    
    def hasCycle(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        head = self.head
        if head == None or head.next == None or head.next.next == None:
            return False
        
        temp = head
        temp2 = head.next.next
        
        while(temp2.next and temp2.next.next):
            if temp == temp2:
                return True
            temp2 = temp2.next.next
            temp = temp.next
        
        return False
    

if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    # Insert 6.  So linked list becomes 6->None 
    llist.append(6) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.push(7); 
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.push(1); 
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.append(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    llist.insertAfter(7, 8) 
    
    
  
    print('Created linked list is:') 
    llist.printList()
    
    llist.delete_node(4)
    llist.delete_node(1)
    
    print('Final linked list is:')
    llist.printList()