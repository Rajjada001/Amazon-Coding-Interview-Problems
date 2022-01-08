def twoSum(a,k):
    s = {}
    for i in range(len(a)):
         temp = k-a[i]
         print(temp)
         if temp in s:
             print(s)
             return [s[temp],i]
         else:
             s[a[i]]=i
             print(s)
        



inp = int(input())
for _ in range(inp):
    n=int(input())
    a = list(map(int, input().rstrip().split()))
    print(twoSum(a,n))

