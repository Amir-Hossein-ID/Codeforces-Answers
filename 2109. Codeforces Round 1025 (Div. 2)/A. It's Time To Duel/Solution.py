import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())


for i in range(t):
    n = int(input())
    a = list(maput())

    lat = a[0]
    has_z = lat == 0
    for i in a[1:]:
        if i == 0:
            has_z = True
            if lat == 0:
                print("YES")
                break
        lat = i
    else:
        if has_z:
            print("NO")
        else:
            print("YES")
