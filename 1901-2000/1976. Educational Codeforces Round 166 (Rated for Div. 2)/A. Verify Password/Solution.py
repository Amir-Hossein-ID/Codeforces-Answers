t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    if s.isalnum() and list(s) == sorted(s):
        print('YES')
    else:
        print('NO')
