import sys

n = int(sys.stdin.readline().rstrip())

name_list = []
for i in range(0,n):
    age,name = sys.stdin.readline().rstrip().rsplit(" ")
    name_list.append([int(age),i,name,])

name_list.sort()


for i in name_list:
    print(i[0],i[2])