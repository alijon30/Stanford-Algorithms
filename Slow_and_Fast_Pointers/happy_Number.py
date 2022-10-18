

def Solution(num):
    slow, fast = num, num

    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))

        if slow == fast:
            break

    return slow == 1

def find_square_sum(num):
    _sum = 0

    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum

