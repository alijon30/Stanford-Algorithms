

def search_next_letter(array, key):
    start, end = 0, len(array)-1

    while start <= end:
        middle = start + (end-start)//2

        if key < array[middle]:
            end = middle - 1
        else:
            start = middle + 1


    return array[start % len(array)]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()