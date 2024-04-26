import sys

si = sys.stdin.readline
word = si().strip()
count_a = 0
for char in word:
    count_a += char == 'a'
    
double_word = word * 2

answer = float('inf')
for start_index in range(len(word)):
    slicing_word = double_word[start_index:start_index + count_a]
    answer = min(answer, slicing_word.count('b'))

print(answer)
