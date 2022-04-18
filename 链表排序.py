from re import S
from regex import L

from requests import head

#归并排序
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

#使用归并排序
def sortList(head):
    def sort(head,tail):
#         if not head:
#             return head
#         if head.next==tail:
#             head.next = None
#             return head
# #使用快慢指针找到链表中心节点
#         slow=fast=head
#         while fast!=None:
#             slow=slow.next
#             fast=fast.next
#             if fast!=tail:
#                 fast=fast.next
#         mid=slow
#         left=sort(head,mid)
#         right=sort(mid,tail)
#         return merge(left,right)
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return merge(sort(head, mid), sort(mid, tail))

    def merge(left,right):
        dummy=ListNode(0)
        temp=dummy
        temp1=left
        temp2=right
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                temp.next=temp1
                temp1=temp1.next
            else:
                temp.next=temp2
                temp2=temp2.next
            temp=temp.next
        if temp1:
            temp.next=temp1
        if temp2:
            temp.next=temp2
        return dummy.next
    return sort(head,None)

def printlist(head):
    while head:
        print(head.val)
        head=head.next

if __name__ == "__main__":
    head=ListNode(4)
    head.next=ListNode(2)
    head.next.next=ListNode(1)
    head.next.next.next=ListNode(3)
    printlist(sortList(head))

