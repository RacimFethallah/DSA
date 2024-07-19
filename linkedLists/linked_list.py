class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  
        self.head = node

    def print(self):
        if self.head is None:
            print("empty linked list")
            return 
          
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '----->'
            itr = itr.next
        llstr += '|'
        print(llstr)

    def insert_at_end(self, data):
        node = Node(data, None) #end node
        if self.head is None:
            self.head = node
            return
    
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    
    def insert_values(self, data_list):  
        self.head = None

        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        #validate the index
        if index<0 or index>= self.get_length():
            print("Invalid index bounds")
            raise Exception("Invalid index")
        
        if index == 0: #at beginning
            self.head = self.head.next
            return
        elif index == self.get_length()-1: #At end
            itr = self.head
            prevItr = itr
            while itr.next:
                prevItr = itr
                itr = itr.next
            prevItr.next = None
            return
        else: #in the middle
            prev = self.head
            itr = self.head.next
            for i in range(1, self.get_length() - 2):
                if index == i:
                    prev.next = itr.next
                else:
                    itr= itr.next
                    prev = prev.next

                




if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([1,2,3,4,5])
    ll.remove_at(2)
    ll.print()

