
def convertFiveRec(n):
    
    if n == 0:
        return 0
    
    digit = n % 10
    
    if(digit == 0):
        digit = 5
    return convertFiveRec(n//10)*10+digit

def convertFive(n):
    # Code here
    if n == 0:
        return 5
    else:
        return convertFiveRec(n)
        

t = int(input())
for _ in range(t):
    print(convertFive(int(input().strip())))
    