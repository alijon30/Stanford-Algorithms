


class Solution:
    def Fruits_into_busket(self, array, limit):
        max_length = 0
        window_start = 0
        char_frequency = {}

        for window_end in range(len(array)):
            right_char = array[window_end]

            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1

            while len(char_frequency) > limit:
                left_char = array[window_start]
                char_frequency[left_char] -= 1

                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)