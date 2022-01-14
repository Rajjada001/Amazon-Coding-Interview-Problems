def maxIndex(a):
    n = len(a)
    left,right = 0,n-1
    m = 0
    while(left<right):
        if a[left]<=a[right]:
            diff = right-left
            m = max(m,diff)
            left+=1
            right = n-1
        else:
            right = right-1

    return m if m>0 else -1


print(maxIndex([34, 8, 10, 3, 2, 80, 30, 33, 1]))