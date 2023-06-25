N = int(input())

word = [input() for _ in range(N)]
new_word = []

left, right = 0, N-1

while left <= right:
    left_word = word[left:right+1]
    right_word = word[left:right+1][::-1]

    if left_word < right_word:
        new_word.append(word[left])
        left += 1
    else:
        new_word.append(word[right])
        right -= 1

for i in range(0, len(new_word), 80):
    print(''.join(new_word[i:i+80]))