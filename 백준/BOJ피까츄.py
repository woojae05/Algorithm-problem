s = input()

tmp = ""
answer = s
for i in range(0,len(s)):
    tmp += s[i]
    if(tmp== "pi"):
        answer = answer[len(tmp):len(answer)]
        tmp = ""
    elif(tmp=="ka"):
        answer = answer[len(tmp):len(answer)]
        tmp= ""
    elif(tmp=="chu"):
        answer = answer[len(tmp):len(answer)]
        tmp=""
        
if(len(answer)==0):
    print("YES")
else:
    print("NO")