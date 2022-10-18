

def find_longest(String):

    max_length = 0
    window_start = 0
    char_freq = {}

    for window_end in range(len(String)):
        current = String[window_end]

        if current not in char_freq:
            char_freq[current] = window_end

        else:
            window_start = max(window_start, char_freq[current] + 1)

            char_freq[current] = window_start

        max_length = max(max_length, window_end - window_start + 1)


    return max_length

def main():

    print("The answer is " + str(find_longest("abccde")))

main()