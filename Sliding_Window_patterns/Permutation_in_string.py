


class Solution:
    def PermutationInString(self, String, pattern):
        char_frequency = {}
        matched = 0
        window_start = 0

        for char in pattern:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1


        for window_end in range(len(String)):
            right_char = String[window_start]

            if right_char in char_frequency:
                char_frequency[right_char] -=1
                if char_frequency[right_char] == 0:
                    matched += 1

            if matched == len(char_frequency):
                return True

            if window_end >= len(pattern) - 1:
                left_char = String[window_start]
                window_start += 1

                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

Dict = {1: 2, 2:3, 3:4}
print(sorted(Dict))