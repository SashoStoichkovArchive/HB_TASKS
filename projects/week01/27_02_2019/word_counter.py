from week01_solutions import palindrome
import sys

arr = []
word = str(input())
arr_h, arr_w = map(int, input().split())

if len(word) > arr_h and len(word) > arr_w:
    print("Invalid number of rows or columns!")
    sys.exit(0)

for i in range(arr_h):
    arr.append([str(j) for j in input().split()])

word_index = 0
result = 0

for h in range(arr_h):
    for w in range(arr_w):
        if arr[h][w] == word[0]:
            # upwards
            word_index = 0
            if h >= len(word) - 1:
                word_index += 1
                for i in range(h - 1, h - len(word), -1):
                    if arr[i][w] == word[word_index]:
                        if word_index == len(word) - 1:
                            result += 1
                        else:
                            word_index += 1
            # to the right
            word_index = 0
            if w <= arr_w - len(word):
                word_index += 1
                for i in range(w + 1, w + len(word)):
                    if arr[h][i] == word[word_index]:
                        if word_index == len(word) - 1:
                            result += 1
                        else:
                            word_index += 1
            # downwards
            word_index = 0
            if h <= arr_h - len(word):
                word_index += 1
                for i in range(h + 1, h + len(word)):
                    if arr[i][w] == word[word_index]:
                        if word_index == len(word) - 1:
                            result += 1
                        else:
                            word_index += 1
            # to the left
            word_index = 0
            if w >= len(word) - 1:
                word_index += 1
                for i in range(w - 1, w - len(word), -1):
                    if arr[h][i] == word[word_index]:
                        if word_index == len(word) - 1:
                            result += 1
                        else:
                            word_index += 1
            # to the up-right
            word_index = 0
            if h >= len(word) - 1 and w <= arr_w - len(word):
                word_index += 1
                for i in range(1, len(word)):
                    if arr[h - i][w + i] == word[word_index]:
                        if word_index == len(word) - 1:
                            result += 1
                        else:
                            word_index += 1
            # to the down-right
            word_index = 0
            if h <= arr_h - len(word) and w <= arr_w - len(word):
                word_index += 1
                for i in range(1, len(word)):
                    if arr[h + i][w + i] == word[word_index]:
                        if word_index == len(word) - 1:
                            result += 1
                        else:
                            word_index += 1
            # to the down-left
            word_index = 0
            if h <= arr_h - len(word) and w >= len(word) - 1:
                word_index += 1
                for i in range(1, len(word)):
                    if arr[h + i][w - i] == word[word_index]:
                        if word_index == len(word) - 1:
                            result += 1
                        else:
                            word_index += 1
            # to the up-left
            word_index = 0
            if h >= len(word) - 1 and w >= len(word) - 1:
                word_index += 1
                for i in range(1, len(word)):
                    if arr[h - i][w - i] == word[word_index]:
                        if word_index == len(word) - 1:
                            result += 1
                        else:
                            word_index += 1

if palindrome(word):
    result //= 2
    print(result)

else:
    print(result)