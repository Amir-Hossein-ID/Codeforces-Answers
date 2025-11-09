n = int(input())

for i in range(n):
    st = input()
    n1 = 0
    n2 = 0
    st1 = ''
    i = 0
    while st[i] >= 'A' and st[i] <= 'Z':
        st1 += st[i]
        i += 1
    while i < len(st) and st[i] >= '0' and st[i] <= '9':
        n1 = n1 * 10 + int(st[i])
        i += 1
    if i != len(st):
        i += 1
        while i < len(st):
            n2 = n2 * 10 + int(st[i])
            i += 1
        ans = ''
        while n2:
            n2 -= 1
            ans += chr(n2 % 26 + ord('A'))
            n2 //= 26
        print(ans[::-1]+str(n1))
    else:
        for i in range(len(st1)):
            n2 += 26 ** (len(st1) - i - 1) * (ord(st[i]) - ord('A') + 1)
        print(f'R{n1}C{n2}')
