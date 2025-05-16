import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(maput())
    pivot = abs(a[0])
    less = 0
    more = 0
    lesscan = 0
    morecan = 0
    for i in a[1:]:
        if i < pivot:
            less += 1
            if abs(i) >= pivot:
                lesscan += 1
        elif i > pivot:
            more += 1
            morecan += 1
    if abs(more - less) <= 1:
        print('YES')
        continue
    else:
        if more > less:
            if more - morecan <= less + morecan + 1:
                print('YES')
                continue
        else:
            if less - lesscan <= more + lesscan:
                print("YES")
                continue

    pivot = -pivot
    less = 0
    more = 0
    lesscan = 0
    morecan = 0
    for i in a[1:]:
        if i < pivot:
            less += 1
            lesscan += 1
        elif i > pivot:
            more += 1
            if -abs(i) <= pivot:
                morecan += 1
    if abs(more - less) <= 1:
        print('YES')
    else:
        if more > less:
            if more - morecan <= less + morecan + 1:
                print('YES')
            else:
                print('NO')
        else:
            if less - lesscan <= more + lesscan:
                print("YES")
            else:
                print("NO")
