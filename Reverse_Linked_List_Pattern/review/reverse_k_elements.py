

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next



def Solution(head, k):
    previous, current = None, head
    while True:
        last_node_of_first_part = previous
        last_node_of_sublist = current

        i = 0
        while current is not None and i < k:
            nxt = current.next
            current.next = previous
            previous =current
            current = nxt
            i += 1

        if last_node_of_first_part is not None:
            last_node_of_first_part.next = previous
        else:
            head = previous

        last_node_of_sublist.next = current

        if current is None:
            break
        previous = last_node_of_sublist