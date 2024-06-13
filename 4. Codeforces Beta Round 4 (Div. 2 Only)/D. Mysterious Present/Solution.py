import heapq

n, w, h = map(int, input().split())

env = []
for i in range(n):
    newenv = list(map(int, input().split()))
    env.append(newenv)
sort = sorted(range(n), key=lambda x: env[x])

where_to = {}
dp = []
best_ans = -1
balen = 0
for i in range(n-1, -1, -1):
    i = sort[i]
    cur = env[i]
    if cur[0] <= w or cur[1] <= h:
        continue

    new_dp = dp.copy()
    ans = i
    ans_len = 1
    while new_dp:
        last_ans_len, last_env = heapq.heappop(new_dp)
        last_ans_len = -last_ans_len
        if cur[0] < env[last_env][0] and cur[1] < env[last_env][1]:
            where_to[i] = last_env
            ans_len = last_ans_len + 1
            break
    
    heapq.heappush(dp, (-ans_len, i))
    if ans_len > balen:
        balen = ans_len
        best_ans = i

if balen:
    print(balen)
    print(best_ans + 1, end=' ')
    balen -= 1
    while balen:
        best_ans = where_to[best_ans]
        print(best_ans + 1, end=' ')
        balen -= 1
    print()
else:
    print(0)
