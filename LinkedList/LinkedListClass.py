class Node():
    def __init__(self, val):
        self.val=val
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None

    def add(self, val):
        node=Node(val)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def __str__(self):
        curr=self.head
        ll=[]
        while curr!=None:
            ll.append(str(curr.val))
            curr=curr.next
        return "->".join(ll)
ls=[5,10,19,20]
l=LinkedList()
for i in ls:
    l.add(i)
print(l)