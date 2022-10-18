

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def Solution(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next


    second_half = reverse(slow)
    head_first_half = head

    while head_first_half is not None and second_half is not None:
        temp = head_first_half.next
        head_first_half.next = second_half
        head_first_half = temp

        temp = second_half.next
        second_half.next = head_first_half
        second_half = temp

    if head_first_half is not None:
        head_first_half.next = None


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  Solution(head)
  head.print_list()


main()