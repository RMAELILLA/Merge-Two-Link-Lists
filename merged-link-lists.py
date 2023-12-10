class ListNode:
    def __init__(self, value=0, next=None):
        if -100 <= value <= 100:
            self.value = value
        else:
            raise ValueError("Node value must be within the range [-100, 100]")
        self.next = next

def merge_sorted_lists(list1, list2):
    temp = ListNode()
    current = temp

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return temp.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()

list1_values = list(map(int, input("Input num for list1 (comma-separated): ").split(',')))
list2_values = list(map(int, input("Input num for list2 (comma-separated): ").split(',')))

list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)

merged_list = merge_sorted_lists(list1, list2)
print("Merged lists:", end=" ")
print_linked_list(merged_list)