from collections import deque

def Solution(array, target):
    product = 1
    result = []
    left = 0

    for right in range(len(array)):
        product *= array[right]

        while product >= target and left < len(array):
            product /= array[left]

            left += 1

        temp_list = deque()

        for i in range(right, left-1, -1):
            temp_list.appendleft(array[i])
        result.append(list(temp_list))
    return result
def main():
  print(Solution([2, 5, 3, 10], 30))
  print(Solution([8, 2, 6, 5], 50))


main()