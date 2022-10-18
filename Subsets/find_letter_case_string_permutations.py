

def find_letter_case_string_permutations(strin):
    permutations = []
    permutations.append(strin)

    for i in range(len(strin)):

        if strin[i].isalpha():
            n = len(permutations)

            for j in range(n):

                old = list(permutations[j])

                old[i] = old[i].swapcase()
                permutations.append("".join(old))