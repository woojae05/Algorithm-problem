s = input()
answer = {}

cnt = 0
for i in range(0,len(s)):
    for j in range(0,len(s)):
        if(i+j>len(s)): continue
        slice_str = s[j:j+i+1]
        if(answer.get(slice_str)==None):
            answer[slice_str] = True
            cnt+=1
print(cnt)