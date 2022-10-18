

def find_longest(String, k):

    max_repeat_letter_count = 0

    max_length, window_start = 0, 0

    char_freq = {}

    for window_end in range(len(String)):
        current = String[window_end]

        if current not in char_freq:
            char_freq[current] = 0

        char_freq[current] += 1

        max_repeat_letter_count = max(max_repeat_letter_count, char_freq[current])

        if window_end - window_start + 1 - max_repeat_letter_count > k:
            left = String[window_start]
            char_freq[left] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length