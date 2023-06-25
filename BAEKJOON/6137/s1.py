N = int(input())

new_word = []

word = [input() for _ in range(N)]

first = 0
last = N-1

while first <= last:
    if first == last:
        new_word.append(word[first])
        break
    if word[first] < word[last]:
        new_word.append(word[first])
        first += 1
    elif word[last] < word[first]:
        new_word.append(word[last])
        last -= 1
    else:
        temp_first = first
        temp_last = last
        while word[temp_first] == word[temp_last]:
            if temp_first + 1 < temp_last and word[temp_first+1] <= word[temp_last-1]:
                new_word.append(word[first])
                first += 1
                break
            elif temp_first + 1 < temp_last and word[temp_first+1] > word[temp_last-1]:
                new_word.append(word[last])
                last -= 1
                break
            temp_first += 1
            temp_last -= 1
        else:
            new_word.append(word[first])
            first += 1

for i in range(0, len(new_word), 80):
    print(''.join(new_word[i:i+80]))
