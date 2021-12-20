'''
4. Minimum distance between two numbers 

You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

Your Task:
Complete the function minDist() which takes the array, n, x and y as input parameters and returns the minimum distance between x and y in the array.
 If no such distance is possible then return -1.

Example 1:

Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are
two distances between x and y, which are
1 and 3 out of which the least is 1.

'''
import sys

def minDis(a,n,x,y):
        minDis1,minDis2=-1,-1   
        res = sys.maxsize
        
        for i in range(n):
            if a[i] == x:
                minDis1 = i
            
            if a[i] == y:
                minDis2 = i
            
            if(minDis1 != -1 and minDis2 != -1):
                res = min(res, abs(minDis1-minDis2))
        
        return -1 if(minDis1==-1 or minDis2==-1) else res




inp = int(input("Number of test cases:"))
for _ in range(inp):
    n,x,y = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    print(minDis(a,n,x,y))

