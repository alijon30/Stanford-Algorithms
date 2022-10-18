


class Solution:
    def Longest_SubString(self, array, limit):
        max_length, window_start, max_ones_count = 0, 0, 0

        for window_end in range(len(array)):
            if array[window_end] == 1:
                max_ones_count += 1


            if window_end - window_start + 1 - max_ones_count > limit:
                if array[window_start] == 1:
                    max_ones_count -=1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)








Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k=2