def largestAndSecondLargest(a,n):
         
        # Your code here'''
        # Function should return a list containing two elements'''
        # li = [maximum, second_maximum]
        max1,max2 = -1,-1
        
        for i in a:
            if(max1 < i):
                max2 = max1
                max1 = i
            elif(max2 < i and max1!=i):
                max2 = i
            
        # if max2==0:
        #     max2=-1
        return [max1,max2]


inp = int(input())
for _ in range(inp):
    n=int(input())
    a = list(map(int, input().rstrip().split()))
    print(largestAndSecondLargest(a,n))

