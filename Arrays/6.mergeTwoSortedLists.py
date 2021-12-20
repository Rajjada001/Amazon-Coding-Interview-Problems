def mergeTwoSortedLists(a,b,n1,n2):
    i=j=k=0
    res = [None]*(n1+n2)
    while(i<n1 and j<n2):
        if(a[i]<b[j]):
            res[k]=a[i]
            i+=1
        else:
            res[k]=b[j]
            j+=1
        k+=1
    while(i<n1):
        res[k]=a[i]
        i+=1
        k+=1
    while(j<n2):
        res[k]=b[j]
        j+=1
        k+=1
    return res




t = int(input("Enter no. of test cases: "))
for _ in range(t):
    n1,n2= map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(mergeTwoSortedLists(a,b,n1,n2))