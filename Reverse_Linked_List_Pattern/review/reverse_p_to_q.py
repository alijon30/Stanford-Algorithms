

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def Solution(head, p, q):

    current, previous = head, None

    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    lastNode_of_first_part = previous

    lastNode_of_sublist = current

    i = 0
    while current is not None and i < q-p+1:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
        i +=1

    if lastNode_of_first_part is not None:
        lastNode_of_first_part.next = previous
    else:
        head = previous

    lastNode_of_sublist.next = current

    return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = Solution(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
