



def solution(head, p, q):

    current, previous = head, None
    next = None
    i = 0
    while current is not None and i < p - 1:
        next = current.next
        previous = current
        current = current.next
        i += 1

    last_node_of_first_part = previous
    last_node_of_sub_part = current

    next = None

    j = 0
    while current is not None and j <  q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        j += 1

    if last_node_of_first_part is not None:
        last_node_of_first_part.next = previous
    else:
        head = previous

    last_node_of_sub_part.next = current