s = input()
t = input()

s = ['abcdefgh'.index(s[0]), int(s[1]) - 1]
t = ['abcdefgh'.index(t[0]), int(t[1]) - 1]

ans = []

while s[0] != t[0] or s[1] != t[1]:
    a = ''
    if s[0] > t[0]:
        a += 'L'
        s[0] -= 1
    elif s[0] < t[0]:
        a += 'R'
        s[0] += 1
    if s[1] > t[1]:
        a += 'D'
        s[1] -= 1
    elif s[1] < t[1]:
        a += 'U'
        s[1] += 1
    ans.append(a)

print(len(ans))
for i in ans:
    print(i)
