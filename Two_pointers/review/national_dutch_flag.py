

def Solution(array):
    left, right = 0, len(array)-1
    i = 0
    while i <= right:

        if array[i] == 0:
            array[i], array[left] = array[left], array[i]
            i += 1
            left += 1

        elif array[i] == 1:
            i += 1

        else:
            array[i], array[right] = array[right], array[i]

            right -= 1



def main():
  arr = [1, 0, 2, 1, 0]
  Solution(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  Solution(arr)
  print(arr)


main()