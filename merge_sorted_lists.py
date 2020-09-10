class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    Merge two sorted linked lists and return it as a new sorted list. 
    The new list should be made by splicing together the nodes of the first two lists.
    Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    """
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
        out = []
        while(1):
            if l is not None:
                out.append(l.val)
                l = l.next
            else:
                break
        print(out)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        flag = 0
        start = None
        while(1):
            if (l1 is None) and (l2 is not None):
                if flag == 0:
                    l3 = l2
                    start = l3
                    flag = 1
                else:
                    l3.next = l2
                return start
            elif (l1 is not None) and (l2 is None):
                if flag ==0:
                    l3 = l1
                    start = l3
                    flag = 1
                else:
                    l3.next = l1
                return start
            elif (l1 is None) and (l2 is None):
                if flag == 0:
                    return None
                return start
            else:
                if(l1.val==l2.val):
                    if flag == 0:
                        flag = 1
                        l3 = l1
                        l1 = l1.next
                        l3.next = l2
                        start = l3
                        l3 = l3.next
                        l2 = l2.next
                    else:
                        l3.next = l1
                        l1 = l1.next
                        l3 = l3.next
                        l3.next = l2
                        l2 = l2.next
                        l3 = l3.next
                elif(l1.val <l2.val):
                    if flag == 0:
                        l3 = l1
                        flag = 1
                        l1 = l1.next
                        start = l3
                    else:
                        l3.next = l1
                        l1 = l1.next
                        l3 = l3.next
                elif (l2.val<l1.val):
                    if flag == 0:
                        l3 = l2
                        start = l3
                        flag = 1
                        l2 = l2.next
                    else:
                        l3.next = l2     
                        l2 = l2.next 
                        l3 = l3.next
        
if __name__ == "__main__":
    a = Solution()
    ln1 = a.create_list([1,2,4])
    ln2 = a.create_list([1,3,4])
    out = a.mergeTwoLists(ln1,ln2)
    a.print_list(out)