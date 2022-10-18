
class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next


def Solution(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast= fast.next.next

    half_second_part = reverse(slow)
    copy_second_half = half_second_part

    while head is not None and half_second_part is not None:
        if head.value != half_second_part.value:
            break
        head = head.next
        half_second_part = half_second_part.next

    reverse(copy_second_half)
    if head is None or half_second_part is None:
        return True
    return False

def reverse(head):
    previous = None
    while head is not None:
        next= head.next
        head.next = previous
        previous = head
        head = next
    return previous
