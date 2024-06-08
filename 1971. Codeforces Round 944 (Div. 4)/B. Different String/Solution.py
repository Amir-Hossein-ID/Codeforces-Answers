n = int(input())

for i in range(n):
    s = input()
    if len(set(s)) == 1:
        print('NO')
    else:
        print('YES')
        print(s[-1] + s[:-1])
