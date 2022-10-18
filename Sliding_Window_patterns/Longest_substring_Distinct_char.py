
class Solution:
    def LongestSubstring(self, array):
        max_length = 0
        window_start = 0
        char_index_map = {}


        for window_end in range(len(array)):
            right_char = array[window_end]

            if right_char in char_index_map:

                window_start = max(window_start, char_index_map[right_char]+1)
                
            char_index_map[right_char] = window_end



            max_length = max(max_length, window_end - window_start + 1)











String="aabccbb"