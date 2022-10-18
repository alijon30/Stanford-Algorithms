

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




def Solution(head, k):

    current, previous = head, None

    while current is not None:
        last_node_of_first_part = previous
        last_node_sublist = current

        i = 0

        while current is not None and i < k:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
            i += 1

        if last_node_of_first_part is not None:
            last_node_of_first_part.next=  previous
        else:
            head = previous

        last_node_sublist.next = current

        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1
    return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = Solution(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()