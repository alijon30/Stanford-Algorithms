class Solution:
    def Longest_substring(self, String, k):

        max_length, max_letter_count, window_start = 0, 0, 0

        char_frequency = {}


        for window_end in range(len(String)):
            right_char = String[window_end]

            max_letter_count = max(max_letter_count, char_frequency[right_char])


            if window_end - window_start + 1 - max_letter_count > k:
                left_char = String[window_start]
                window_start += 1
                char_frequency[left_char] -=1

            max_length = max(max_length, window_end - window_start + 1)










String="aabccbb"