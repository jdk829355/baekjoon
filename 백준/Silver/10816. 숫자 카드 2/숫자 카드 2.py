import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

count_cards = Counter(cards)

print(" ".join(map(lambda x: str(count_cards.get(x, 0)), nums)))
