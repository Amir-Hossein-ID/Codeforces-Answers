d, sum_ = map(int, input().split())
mis = []
mas = []
mi_sum = 0
ma_sum = 0
    
for day in range(d):
    mi, ma = map(int, input().split())
    mi_sum += mi
    ma_sum += ma
    mis.append(mi)
    mas.append(ma)
    
if sum_ > ma_sum or sum_ < mi_sum:
    print('NO')
else:
    print('YES')
    can_lie = ma_sum - sum_
    ans = []
    for i in range(d):
        to = min(can_lie, mas[i]-mis[i])
        ans.append(mas[i] - to)
        can_lie -= to
    print(*ans)
