def average(array):
    return sum(set(array)) / len(set(array))

n = int(input())
arr = list(map(int, input().split()))
print(average(arr))
