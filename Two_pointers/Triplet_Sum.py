



def search_triplets(array):
    array.sort()
    triplets = []

    for i in range(len(array)):
        if i > 0 and array[i] == array[i-1]:
            continue
        search_pair(array, -array[i], i+1, triplets)

    return triplets

def search_pair(array, target_sum, left, triplets):
    right = len(array)-1
    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == target_sum:
            triplets.append([-target_sum, array[left], array[right]])
            left += 1
            right += 1

            while left < right and array[left] == array[left-1]:
                left += 1
            while left < right and array[right] == array[right+1]:
                right -= 1
        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1