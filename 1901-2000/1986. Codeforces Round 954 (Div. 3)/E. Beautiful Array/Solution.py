import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n,k = maput()
    a = sorted(maput())
    b = {}
    for i in a:
        rem = i % k
        if rem not in b:
            b[rem] = []
        b[rem].append(i)

    can_ignore = n % 2
    imp = False

    ans = 0
    for j in b:
        a = b[j]
        lena = len(a)
        if lena % 2:
            if can_ignore:
                can_ignore -= 1
            else:
                imp = True
                break
            distances = [(a[i+1]-a[i])//k for i in range(lena-1)]
            left_ans = 0
            right_ans = sum(distances[i] for i in range(1, lena, 2))
            this_part_best_ans = left_ans + right_ans
            for leave in range(2, lena, 2):
                left_ans += distances[leave-2]
                right_ans -= distances[leave-1]
                this_part_best_ans = min(left_ans+right_ans, this_part_best_ans)
            ans += this_part_best_ans
        else:
            for i in range(0, lena, 2):
                ans += (a[i+1] - a[i]) // k

    if imp:
        print('-1\n')
    else:
        print(str(ans) + '\n')
