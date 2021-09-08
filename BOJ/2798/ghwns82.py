# 2798

from itertools import combinations

N, M= map(int, input().split())
card = list(map(int, input().split()))
comb_ = [sum(i) for i in list(combinations(card, 3)) if sum(i) <= M]
print(
    sorted(list(set(comb_)))[-1]
)

# print(
#     sorted(list(set([sum(i) for i in list(combinations(card, 3)) if sum(i) <= M])))[-1]
# )
