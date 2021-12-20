def twoSum(a,k):
    s = {}
    for i in range(len(a)):
         temp = k-a[i]

         if temp in s:
             return [s[temp],i]
         else:
             s[a[i]]=i
        



inp = int(input())
for _ in range(inp):
    n=int(input())
    a = list(map(int, input().rstrip().split()))
    print(twoSum(a,n))

