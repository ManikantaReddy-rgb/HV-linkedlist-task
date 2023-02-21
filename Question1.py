class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def merged_sorted_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        merged_list = list1
        merged_list.next = merged_sorted_lists(list1.next, list2)
    else:
        merged_list = list2
        merged_list.next = merged_sorted_lists(list1, list2.next)

    return merged_list

def print_list(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next

if __name__ == '__main__':
    list1 = Node(2)
    list1.next = Node(1)
    list1.next.next = Node(3)

    list2 = Node(4)
    list2.next = Node(6)
    list2.next.next = Node(5)

    sorted_list = merged_sorted_lists(list1, list2)
    print_list(sorted_list)
