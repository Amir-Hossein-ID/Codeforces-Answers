import sys
    
input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n,m,k = maput()
    a = input()
    if m > n:
        print('YES\n')
        continue
    best_place = -1
    while best_place <= n - 1:
        if best_place == -1 or a[best_place] == 'L': # if we are in a log jump to farthest log if possible, else jump to farthest water
            if best_place + m >= n:
                print("YES\n")
                break
            where = a.rfind('L', best_place+1, best_place + m + 1)
            if where != -1:
                best_place = where
            else:
                where = a.rfind('W', best_place+1, best_place + m + 1)
                if where != -1:
                    best_place = where
                else:
                    print('NO\n')
                    break
        else:
            i = best_place
            while i != n and a[i] != 'L':
                if a[i] == 'C' or not k:
                    print('NO\n')
                    break
                i += 1
                k -= 1
            else:
                if i == n:
                    print('YES\n')
                    break
                best_place = i
                continue
            break
    else:
        print('YES\n')
