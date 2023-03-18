"""
Generate all possible permutations from string
"""


def permutation_generator(word):
    if len(word) == 0:
        yield ""
    else:
        for m in range(len(word)):
            for n in permutation_generator(word[:m] + word[m + 1:]):
                yield word[m] + n


for x in permutation_generator("home"):
    print(x)
