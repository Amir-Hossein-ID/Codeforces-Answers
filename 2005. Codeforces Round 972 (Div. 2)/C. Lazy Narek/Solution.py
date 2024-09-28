import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

ss = 'narek'
for i in range(t):
    n,m = maput()
    bestans = 0
    dic = {0 : 0}

    for i in range(n):
        s = input()
        ndic = dic.copy()
        for look in dic:
            score = dic[look]
            for i in s:
                if i == ss[look]:
                    score += 1
                    look += 1
                    look %= 5
                elif i in ss:
                    score -= 1
            bestans = max(bestans, score - 2 * look)
            if look not in ndic or score > ndic[look]:
                ndic[look] = score
        dic = ndic
    print(str(bestans) + '\n')
