def count_vowels(text):
    """Counts the amount of vowels in an input string.

    Args:
        text: string that will be checked for vowels
        vowels: list of characters (vowels)
        counter: int increased by 1 when a vowel is found
    Returns:
        Int: integer number of counted vowels in a string
    """
    if not isinstance(text, str):
        raise TypeError("input must be a string")

    vowels = ['a', 'e', 'i', 'o', 'u']
    text = text.lower()
    counter = 0

    for letter in text:
        if letter in vowels:
            counter += 1

    return counter


string = "I am trying this"
print(count_vowels(string))
