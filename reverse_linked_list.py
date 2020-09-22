class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def create_list(self, list):
        flag = 0
        for l in list:
            if flag ==0:
                l1 = ListNode(val=l,next = None)
                start = l1
                flag = 1
            else:
                node = ListNode(val=l,next=None) 
                l1.next = node
                l1 = l1.next
        return start
    
    def print_list(self, l:ListNode):
        while(1):
            if l is not None:
                print(l.val)
                l = l.next
            else:
                break
    def reverse_list(self, head: ListNode):
        if head == None or head.next==None:
            return head
        prev = head.next
        head.next = None
        temp = prev.next
        i =0 
        while(prev.next is not None):
            #print(head.val,temp.val,prev.val)
            prev.next = head
            head = prev
            #print(prev.next)
            prev = temp
            #print(head.val,temp.val,prev.val)
            temp = prev.next
            i+=1
        prev.next = head
        head = prev
        return head


if __name__ == "__main__":
    a = Solution()
    l = a.create_list([5,4,3,2,1])
    a.print_list(l)
    o = a.reverse_list(l)
    a.print_list(o)