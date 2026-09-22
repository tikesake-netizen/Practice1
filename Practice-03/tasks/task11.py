from itertools import permutations


def string_permutations(text):
    result = permutations(text)

    for permutation in result:
        print("".join(permutation))


text = input("Enter a string: ")
string_permutations(text)