class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #address of next node

class SingleLinkedList:
    def __init__(self):
        self.head=None


    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_at_end(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

    def insert_at_pos(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        


    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head 
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
L=SingleLinkedList()
n=Node(10)
L.head=n
n1=Node(20)
L.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
L.insert_at_beginning(5)
L.insert_at_end(60)
L.insert_at_pos(3,35)
L.insert_at_pos(5,90)
L.display()  #Linked List is empty