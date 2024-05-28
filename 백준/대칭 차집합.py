n,m = map(int, input().split(" "))
A_list = list(map(int, input().split(" ")))
A_dict = dict(zip(A_list,range(len(A_list))))
B_list = list(map(int, input().split(" ")))
B_dict = dict(zip(B_list,range(len(B_list))))

cnt = len(A_list)
for i in B_list:
    if(A_dict.get(i)!=None):
        cnt-=1
  

cnt+= len(B_list)

for i in A_list:
    if(B_dict.get(i)!=None):
        cnt-=1
   
print(cnt)