def findDuplicates(a):
        s = {}
        res = []
        for i in range(len(a)):
            if a[i] in s:
                s[a[i]] +=1
            else:
                s[a[i]]=1
        
        for num in s:
            if s[num]>1:
                res.append(num)

        return sorted(res) if len(res)>0 else [-1]


print(findDuplicates([2,3,1,2,3]))