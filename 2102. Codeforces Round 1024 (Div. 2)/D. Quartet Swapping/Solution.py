import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = sys.stdout.write

t = int(input())

def merge_and_count(arr, l, m, r):
    left_half = arr[l : m + 1]
    right_half = arr[m + 1 : r + 1]
    i = 0 
    j = 0
    k = l
    inversions = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            inversions += (len(left_half) - i)
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return inversions

def merge_sort_and_count(arr, l, r):
    inversions = 0
    if l < r:
        m = (l + r) // 2
        inversions += merge_sort_and_count(arr, l, m)
        inversions += merge_sort_and_count(arr, m + 1, r)
        inversions += merge_and_count(arr, l, m, r)
    return inversions

for _ in range(t):
    n = int(input())
    a = list(maput())
    b = a[::2]
    c = a[1::2]
    bbb = merge_sort_and_count(b, 0, len(b)-1)
    ccc = merge_sort_and_count(c, 0, len(c)-1)
    # print(bbb, ccc)
    if (bbb+ccc) % 2 == 0:
        for i in range(0, len(c)):
            printf(str(b[i]) + ' ')
            printf(str(c[i]) + ' ')
        if n % 2 == 1:
            printf(str(b[-1]) + ' ')
    else:
        if n % 2 == 1:
            for i in range(0, len(c)-1):
                printf(str(b[i]) + ' ')
                printf(str(c[i]) + ' ')
            printf(str(b[-1]) + ' ')
            printf(str(c[-1]) + ' ')
            printf(str(b[-2]) + ' ')
        else:
            for i in range(0, len(c)-2):
                printf(str(b[i]) + ' ')
                printf(str(c[i]) + ' ')
            printf(str(b[-2]) + ' ')
            printf(str(c[-1]) + ' ')
            printf(str(b[-1]) + ' ')
            printf(str(c[-2]) + ' ')
            
    printf('\n')
