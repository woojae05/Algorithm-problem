diceList = list(map(int, input().split()))
if diceList[0] == diceList[1] == diceList[2]:
    print(10000+(diceList[1]*1000))
elif diceList[0] == diceList[1] or diceList[1] == diceList[2] or diceList[0] == diceList[2]:
    for i in diceList:
        if diceList.count(i) > 1:
            print(1000+(i * 100))
            break
else:
    print((max(diceList)*100))
