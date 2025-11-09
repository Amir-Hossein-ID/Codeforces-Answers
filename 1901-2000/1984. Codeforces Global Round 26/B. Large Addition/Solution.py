t = int(input())

for i in range(t):
    x = input()
    if x[0] > '1': # first digit can't be larger than 1
        print('NO')
        continue
    for i in x[1:-1]:
        if int(i) - 1 < 0: # middle digits cant be 0
            print('NO')
            break
    else:
        if x[-1] <= '8': #last digit should be less than 9 because no two "large" digits can make 9
            print('YES')
        else:
            print('NO')
