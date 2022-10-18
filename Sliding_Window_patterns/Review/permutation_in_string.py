

def find_permutation(String, pattern):

    char_freq = {}

    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    matches =  0
    window_start = 0

    for window_end in range(len(String)):
        current = String[window_end]

        if current in char_freq:
            char_freq[current] -= 1

            if char_freq[current] == 0:
                matches += 1

        if matches == len(char_freq):
            return True

        if window_end >= len(pattern)-1:
            left = String[window_start]

            if left in char_freq:

                if char_freq[left] == 0:
                    matches -= 1
                char_freq[left] += 1
            window_start += 1

    return False

def main():

    print("The answer is "  + str(find_permutation("odicf", 'dc')))

main()
