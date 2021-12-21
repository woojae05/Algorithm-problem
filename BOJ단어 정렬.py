n = int(input())
words = []
for i in range(n):
    words.append(input())

words = set(words)
words = sorted(words,key=lambda a:(len(a),a))

for words in words:
    print(words)
