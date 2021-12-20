def twoSum(a,k):
    start,end = 0, len(a)-1
    #start from left index to the right
    while(start<end):
        tsum = a[start] + a[end]
        if(tsum==k):
            return [start,end]
            break
        elif(tsum<k):
            start+=1
        else:
            end-=1
        



inp = int(input())
for _ in range(inp):
    n=int(input())
    a = list(map(int, input().rstrip().split()))
    print(twoSum(a,n))

