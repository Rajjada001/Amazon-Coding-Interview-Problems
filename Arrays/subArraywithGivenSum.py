from re import L


def subArraywithGivenSum(a,s):
    n = len(a)-1
    left=right=0
    currSum = a[0]
    while(left<n and right<n):
        if(currSum==s):
            if(left==right):
                return [left+1,left+1]
            else:
                return [left+1,right+1]
        elif(currSum>s):
            currSum = currSum-a[left]
            left+=1
        else:
            right+=1
            currSum = currSum+a[right]
    
    return [-1]

print(subArraywithGivenSum([1,2,3,4,5,6,7,8,9,10],18))
