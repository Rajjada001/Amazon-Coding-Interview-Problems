def thirdLargest(a, n):
        # code here
        
        if(n<3):
            return -1
        max1,max2,max3 = 0,0,0

        for nums in a:
            if(max1< nums):
                max3,max2,max1 = max2,max1,nums
            
            elif(max2 < nums):
                max3,max2 = max2,nums
            
            elif(max3 < nums):
                max3 = nums
                
        return max3


inp = int(input())
for _ in range(inp):
    n=int(input())
    a = list(map(int, input().rstrip().split()))
    print(thirdLargest(a,n))