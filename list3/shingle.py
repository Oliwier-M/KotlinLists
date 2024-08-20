# Task 2 List 3
# czytanie plików csv txt etc
# plot making
# pandas list 4 task 2 important
# numpy ndarray !!! .sum .mean etc 3d array
# 4 2 task, 5 2 task
# przekroje 2d w tabeli 3d


import main
import argparse


def read(n, k):
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers")

    parser = argparse.ArgumentParser(description="counts n common k-shingles")

    parser.add_argument('-n', type=int, help='number of most common shingles we want to get')
    parser.add_argument('-k', type=int, help='number k to make k-shingles')

    args = parser.parse_args()

    user_input = ""
    print("Enter your text: ")
    try:
        while True:
            line = input()
            user_input += line
    except EOFError:
        pass

    if k <= 0 or k > len(user_input):
        raise ValueError

    shingles = main.shingles(user_input, k)
    shingles_check = shingles.copy()

    repeats = []

    for s in shingles:
        if s in shingles_check:
            shingles_check.remove(s)

        counter = 1
        for check in shingles_check:
            if s == check:
                counter += 1

        if not repeats.__contains__(s) and counter > 1:
            repeats.append([s, counter])

        while s in shingles_check:
            shingles_check.remove(s)

    # sort them by the highest repeat count

    sorted_repeats = sorted(repeats, key=lambda x: x[1], reverse=True)

    result = sorted_repeats[:n]


print(read(2, 2))

# shingles, repeats, sorted_repeats, result = read(2, 2)
#
# # Print only shingles
# print("Shingles:")
# print(shingles)
#
# # Print only repeats
# print("Repeats:")
# print(repeats)
#
# print("Sorted:")
# print(sorted_repeats)
#
# print("Result:")
# print(result)
