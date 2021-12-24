def leftRotate(a,d,n):
    r = [0]*n
    for old_index in range(n):
        new_index = (old_index+(n-d))%n
        r[new_index] = a[old_index]
    return r


def rightRotate(a,d,length):
    copy = [0]*length
    for old_index in range(length):
        new_index = (old_index+d)%length
        copy[new_index] = a[old_index]
    
    for i in range(length):
        a[i] =copy[i]
    return a

# Better space complexity
def rightRotateOptimized(a,k,n):
    k = k%n
    reverse(a,0,n-1)
    reverse(a,0,k-1)
    reverse(a,k,n-1)
    return a

def reverse(a,l,r):
    while(l<r):
        temp = a[l]
        a[l]=a[r]
        a[r]=temp
        l+=1
        r-=1
    




t = int(input())
for _ in range(t):
    d,n = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    # print(leftRotate(a,d,n))
    # print(a)
    # print(rightRotate(a,d,n))
    # print(a)
    print(rightRotateOptimized(a,d,n))

