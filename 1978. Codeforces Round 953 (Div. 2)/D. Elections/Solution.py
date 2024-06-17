import sys
    
input = lambda: sys.stdin.readline().strip()
printf = print
print = sys.stdout.write
    
t = int(input())
    
for _ in range(t):
    n,c = map(int, input().split())
    votes = list(map(int, input().split()))
    votes[0] += c
    ans = list(range(n))
    maxi = max(range(n), key=lambda x:votes[x])
    max_vote = votes[maxi]
    ans[maxi] = 0

    sum = 0
    for i in range(n):
        if i == maxi:
            break
        sum += votes[i]
        if sum < max_vote:
            ans[i] += 1
        else:
            break
    for i in ans:
        print(str(i) + ' ')
    print('\n')
