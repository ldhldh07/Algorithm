import sys

arr = list(sys.stdin.readline().strip())
word_list = {}
for a in arr:
    a = a.upper()
    if a not in word_list:
        word_list[a] = 1
    else:
        word_list[a] += 1

ans_list = []
for k, v in word_list.items():
    if v == max(word_list.values()):
        ans_list.append(k)

if len(ans_list) > 1:
    print('?')
else:
    print(ans_list[0])