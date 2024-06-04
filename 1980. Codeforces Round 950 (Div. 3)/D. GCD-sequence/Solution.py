t = int(input())
    
def gcd(a,b):
    if b > a:
        a,b = b,a
    while b:
        a,b = b, a%b
    return a
    
def calc(arr, last = 0, did=True):
    for i in range(len(arr)-1):
        cur = gcd(arr[i], arr[i+1])
        if cur >= last:
            last = cur
        else:
            if did:
                return False
            return max(calc(arr[max(i-3, 0):i-1] + arr[i:]),
                       calc(arr[max(i-2, 0):i] + arr[i+1:]),
                       calc(arr[i:i+1] + arr[i+2:], last))
    return True
    
for i in range(t):
    n = int(input())
    m = [int(i) for i in input().split()]
    
    a = calc(m, 0, False)
    print('YES' if a else 'NO')
