
def string_anagrams(String, Pattern):

    char_freq = {}

    for char in Pattern:
        if char not in char_freq:
            char_freq[char] = 0

        char_freq[char] += 1

    matches, window_start = 0,0

    for window_end in range(len(String)):
        current = String[window_end]

        if current in char_freq:
            char_freq[current] -= 1
            