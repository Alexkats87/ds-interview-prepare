"""
A list of pairs given:

pairs = [["a", 0.1], ["b", 0.2], ["c", 0.7]]


Write a function that generates:
 - element "a" with probability 0.1
 - element "b" with probability 0.2
 - element "c" with probability 0.7


(Ozon-2023)
"""

from itertools import accumulate
from collections import Counter
import random


def bin_search(lst, e):
    # print(lst)

    l = 0
    r = len(lst) - 1
    m = int((r - l) / 2)

    while r - l > 1:
        # print(l,m,r)
        if e > lst[m]:
            l = m
            m = int((r - m) / 2.0) + m

        else:
            r = m
            m = int((m - l) / 2.0)

    return l


class Sampler:

    def __init__(self, pairs):
        self.elem_list = [e[0] for e in pairs]
        self.probs_lst = [e[1] for e in pairs]
        self.cum_probs_lst = [0.0] + list(accumulate(self.probs_lst))

        print(self.probs_lst)
        print(self.cum_probs_lst)

    def sample(self) -> str:
        r = random.random()
        # r = 0.99
        # print(r)

        left_index = bin_search(self.cum_probs_lst, r)
        # print(left_index)
        # print(self.cum_probs_lst[left_index])
        # print(self.elem_list[left_index])

        return self.elem_list[left_index]


if __name__ == '__main__':

    p1 = [["a", 0.1], ["b", 0.2], ["c", 0.7]]
    # p2 = [["a", 0.1], ["b", 0.2], ["c", 0.3], ["d", 0.4]]
    # p3 = [["a", 0.1], ["b", 0.2], ["c", 0.3], ["d", 0.35], ["e", 0.05]]

    sampler = Sampler(p1)
    sampled_list = []

    for i in range(10000):
        s = sampler.sample()
        sampled_list.append(s)

    print(sampled_list)


