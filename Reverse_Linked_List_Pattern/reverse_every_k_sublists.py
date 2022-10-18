



def Solution(head, k):

    if k <= 1 or head is None:
        return head

    current, previous = head, None
    while True:

        last_node_of_first_part = previous
        last_node_of_sub_part = current

        i = 0
        next = None
        while i < k and current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        if last_node_of_first_part is not None:
            last_node_of_first_part.next = previous
        else:
            head = previous

        last_node_of_sub_part.next = current

        if current is None:
            break
        previous = last_node_of_sub_part