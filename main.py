import sys

naturals = {1: 1, 2: 1}
unique_sum = [1,2]

def find_element(n):
    for i in range(2, sys.maxsize):
        if len(unique_sum) == n:
            print(f"The {n}th element in the unique sum sequence is: {unique_sum[-1]}")
            print(f"The final squence generated is: {unique_sum}")
            break
        if len(unique_sum) % 1000 == 0:
            print(f"The {len(unique_sum)}th element in the unique sum sequence is: {unique_sum[-1]}")
        for j in range(1, i):
            candidate = j + i
            naturals[candidate] = naturals.get(candidate, 0) + 1
            # print(f"Candidate [{candidate}] using {j} + {i} has {naturals.get(candidate)} matches.")
            if j == i -1 and naturals.get(candidate) == 1:
                unique_sum.append(candidate)

input = input("Type the nth unique sum element you are looking for: ")

find_element(int(input))