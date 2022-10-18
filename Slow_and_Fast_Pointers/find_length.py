

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next



def Solution(head):
    slow, fast = head, head
    cycle_length = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return find_cycle(slow)


    return cycle_length

def find_cycle(slow):
    current = slow
    length = 0

    while True:
        length += 1
        current = current.next
        if current == slow:
            break
    return length

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next= Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("LinkedList has a cycle " + str(Solution(head)))

    head.next.next.next.next.next = head.next

    print("LinkedList has a cycle " + str(Solution(head)))
main()