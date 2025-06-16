def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        seen = ""
        for c in string[i:i+k]:
            if c not in seen:
                seen += c
        print(seen)

string = input()
k = int(input())
merge_the_tools(string, k)
