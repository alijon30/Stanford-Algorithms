

class Solution:
    def LongestSubString(self, string, size):
        max_length = 0
        window_start = 0
        char_frequency = {}


        for window_end in range(len(string)):
            right_char = string[window_end]

            if right_char not in char_frequency:
                char_frequency[right_char] = 0

            char_frequency[right_char] += 1


            while len(char_frequency) > size:
                left_char = string[window_start]
                char_frequency[left_char] -= 1
                window_start += 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]

            max_length = max(max_length, window_end - window_start + 1)















String="araaci"
K=2