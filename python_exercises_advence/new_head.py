"""
File: new_head.py
Name: Annby
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def new_head(head: ListNode, x: int) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    less_head = ListNode(0)  # 連接小於x的點
    greater_head = ListNode(0)  # 連接大於或等於x的點

    less = less_head  # 小於x的串
    greater = greater_head  # 大於或等於x的串

    while head:
        if head.val < x:
            less.next = head  # 把點連接到小於x的串上
            less = less.next
        else:
            greater.next = head  # 把點連接到大於或等於x的串上
            greater = greater.next
        head = head.next  # 移動到下一個點

    greater.next = None  # 結束大於或等於x的串
    less.next = greater_head.next  # 連接兩個串列

    return less_head.next

####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 new_head.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(9, None)
            l1.next = ListNode(6, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(8, None)
            ans = new_head(l1,8)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(1, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(2, None)
            l1.next.next.next.next = ListNode(5, None)
            l1.next.next.next.next.next = ListNode(1, None)
            ans = new_head(l1, 3)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 new_head.py test1"')


if __name__ == '__main__':
    main()
