N,B = input().split(" ")
N = int(N)
B = int(B)

numbers ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""
cnt =0 
while(True):
    cnt+=1
    na =  N % B
    number = numbers[na]
    result += number
    N = N // B
    if(N==0):
        break
result = result[::-1]
print(result)
