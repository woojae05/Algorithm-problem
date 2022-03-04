hour, minnit = map(int, input().split())
time = int(input())
hour = hour + time//60
minnit = minnit + time % 60
if minnit >= 60:
    minnit -= 60
    hour += 1
if hour >= 24:
    hour -= 24
print(hour, minnit)
