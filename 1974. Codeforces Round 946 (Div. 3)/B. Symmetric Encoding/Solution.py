t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    p = sorted(list(set(s)))
    map = {}
    for i in range(len(p)):
        map[p[i]] = p[-i-1]
    print("".join([map[i] for i in s]))
