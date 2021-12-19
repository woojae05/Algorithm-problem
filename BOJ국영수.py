name = [input().split() for _ in range(int(input()))]
name.sort(key=lambda a: (-int(a[1]), int(a[2]), -int(a[3]), a[0]))
for i in name:
    print(i[0])