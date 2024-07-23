# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(res) -> ListNode:
        print(res)
        nl = ListNode(res[0], None)

        for n in res[1:]:
             itr = nl
             while itr.next:
                  itr = itr.next
             itr.next = ListNode(n, None)

        return nl
        


if __name__ == '__main__':
     res=[7,0,8]
     l = ListNode()
     addTwoNumbers(res)




        