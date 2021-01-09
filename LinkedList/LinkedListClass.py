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

    def remove(self, val):
        curr=self.head
        prev=None
        while curr!=None:
            if curr.val==val:
                break
            prev=curr
            curr=curr.next
        if curr!=None:
            if curr==self.head:
                self.head=self.head.next
            else:
                prev.next=curr.next
            if curr==self.tail:
                self.tail=prev
   
            del curr

    def __str__(self):
        curr=self.head
        ll=[]
        while curr!=None:
            ll.append(str(curr.val))
            curr=curr.next
        return "->".join(ll)

ls=[5, 10, 19, 20, 6, 90, 1, 8]
l=LinkedList()
for i in ls:
    l.add(i)
l.remove(5)
l.remove(8)
l.remove(20)
print(l)
l.add(7)
print(l)