
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        reverse = []
        length = 0
        while head:
            reverse.append(head)
            head = head.getNext()
            length+=1
        for i in range(length):
            reverse[length-i-1].printValue()