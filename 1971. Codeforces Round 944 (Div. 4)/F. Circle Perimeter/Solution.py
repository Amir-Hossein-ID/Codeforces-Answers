import sys
    
input = sys.stdin.readline
print = sys.stdout.write
    
t = int(input())
    
for _ in range(t):
    r = int(input())
    maxi = (r+1) * (r+1)
    mini = r * r
    ans = 0
    newr = r
    for i in range(0, newr+1):
        for j in range(r, 0, -1):
            ss = i * i + j * j
            if ss < maxi:
                if ss >= mini:
                    ans += 1
                else:
                    break
            else:
                r -= 1 # if it is already >= maxi we wont have another answer with this r
    ans *= 4    
    print(str(ans) + '\n')
