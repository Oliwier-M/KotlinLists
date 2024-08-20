# Task 1 List 3
def shingles(t, k):
    """
    :param t: input string
    :param k: natural number k to make k-shingles
    :param text: a list of words extracted from the input string t, split at " "
    :return: shingles
    """
    if k <= 0 or k > len(t):
        raise ValueError("Invalid k number")

    text = t.split(" ")
    shingle = []

    for i in range(len(text)-1):
        if i+k <= len(text):
            shingle.append(text[i:i+k])
    # print(shingle)
    return shingle

# t = "im checking this thing here"
# for s in shingles(t, 2):
#     print(s)
#