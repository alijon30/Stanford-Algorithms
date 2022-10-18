

def find_longest(strin, k):

    max_length = 0
    char_freq = {}
    window_start = 0

    for window_end in range(len(strin)):

        current = strin[window_end]

        if current not in char_freq:
            char_freq[current] = 0

        char_freq[current] += 1

        while len(char_freq) > k:
            prev = strin[window_start]

            char_freq[prev] -= 1
            if char_freq[prev] == 0:
                del char_freq[prev]

            window_start += 1

        max_length = max(max_length, window_end-window_start + 1)

    return max_length

def main():

    print("The result is : " + str(find_longest('cbbebi', 3)))

main()