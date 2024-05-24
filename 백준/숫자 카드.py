import sys
n = int(sys.stdin.readline().rstrip())
num_cards = list(map(int,sys.stdin.readline().rstrip().split(" ")))
m = int(sys.stdin.readline().rstrip())
having_cards = list(map(int,sys.stdin.readline().rstrip().split(" ")))

card_dic = {}
for card in num_cards:
    card_dic[card]=True

answer = []
for card in having_cards:
    if(card_dic.get(card)):
        answer.append(1)
    else:answer.append(0)
print(*answer)