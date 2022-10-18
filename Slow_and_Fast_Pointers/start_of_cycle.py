

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next= next


def Solution(head):
    slow, fast = head, head
    cycle_length = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_length = find_length(slow)
            break

    return find_start(head, cycle_length)


def find_length(slow):
    current = slow
    length = 0
    while True:
        length += 1
        current = current.next

        if current == slow:
            break
    return length

def find_start(head, length):
    pointer1 = head
    pointer2 = head

    while length > 0:
        pointer2 = pointer2.next
        length -= 1

    while pointer1 != pointer2:
        pointer2 = pointer2.next
        pointer1 = pointer1.next

    return pointer1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(33)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(Solution(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(Solution(head).value))


main()