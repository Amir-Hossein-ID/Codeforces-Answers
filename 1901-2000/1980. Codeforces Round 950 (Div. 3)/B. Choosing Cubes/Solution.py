t = int(input())
    
for i in range(t):
    n,f,k = map(int, input().split())
    s = [int(i) for i in input().split()]
    fav = s[f-1]
    s = sorted(s, reverse=True)
    if s[k-1]>fav:
        print('no')
    elif s[k-1]==fav and k != n and s[k]==fav:
        print('maybe')
    else:
        print('yes')
