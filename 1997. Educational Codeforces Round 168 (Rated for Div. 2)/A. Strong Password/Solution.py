import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t):
    s = list(input())
    last = ''
    for i in range(len(s)):
        if s[i] == last:
            s.insert(i, chr(((ord(s[i]) - ord('a') + 1) % 26) + ord('a'))) # adding next lowercase character
            break
        last = s[i]
    else:
        s.append(chr(((ord(last) - ord('a') + 1) % 26) + ord('a')))
    print("".join(s) + '\n')
