from collections import Counter

_ = int(input())
sizes = Counter(input().split())
earnings = 0

for _ in range(int(input())):
    size, price = input().split()
    if sizes[size] > 0:
        earnings += int(price)
        sizes[size] -= 1

print(earnings)
