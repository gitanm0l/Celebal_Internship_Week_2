def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

s = input()
print(solve(s))
