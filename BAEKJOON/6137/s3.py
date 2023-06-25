import sys

N = int(input())
word = [sys.stdin.readline().strip() for _ in range(N)]
new_word = []

left, right = 0, N - 1

while left <= right:
    left_char = word[left]
    right_char = word[right]
    
    if left_char < right_char:
        new_word.append(left_char)
        left += 1
    elif right_char < left_char:
        new_word.append(right_char)
        right -= 1
    else:
        temp_left, temp_right = left, right
        while temp_left < temp_right and word[temp_left] == word[temp_right]:
            temp_left += 1
            temp_right -= 1

        if word[temp_left] <= word[temp_right]:
            new_word.append(left_char)
            left += 1
        else:
            new_word.append(right_char)
            right -= 1

for i in range(0, len(new_word), 80):
    print(''.join(new_word[i:i+80]))
