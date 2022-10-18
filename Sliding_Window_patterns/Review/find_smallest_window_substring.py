

def find_smallest(String, Pattern):

    char_freq = {}

    for char in Pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    substr_start = 0
    matches, window_start = 0, 0
    min_length = len(String) + 1
    for window_end in range(len(String)):
        current = String[window_end]

        if current in char_freq:
            char_freq[current] -= 1

            if char_freq[current] >= 0:
                matches += 1

        while matches == len(char_freq):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left = String[window_start]
            if left in char_freq:
                if char_freq[left] == 0:
                    matches -= 1
                char_freq[left] += 1

            window_start += 1
    if min_length > len(String):
        return ""
    return String[substr_start: substr_start + min_length]
def main():
    print(find_smallest("adcad", "abc"))

main()