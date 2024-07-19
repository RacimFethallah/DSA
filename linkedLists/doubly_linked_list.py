class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insert_at_end(self, data):
        node = Node(data, None, None) #end node
        if self.head is None:
            self.head = node
            return
    
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        node.prev = itr

    def insert_values(self, data_list):  
        self.head = None

        for data in data_list:
            self.insert_at_end(data)


    def print_forward(self):
        if self.head is None:
            print("empty linked list")
            return
        
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + "---"
            itr = itr.next
        dllstr += '|'
        print(dllstr)

    def print_backward(self):

        itr = self.head

        while itr.next:
            itr = itr.next
        
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + "----"
            itr = itr.prev
        print(dllstr)
    




if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()