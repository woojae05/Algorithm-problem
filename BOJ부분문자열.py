while True:
    try:
        result = 'No'
        idx=0
        s,t = input().split()
        for i in t:
            if i==s[idx]:
                idx+=1
                if idx==len(s):
                    result='Yes'
                    break
        print(result)        
    except EOFError:
        break