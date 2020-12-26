from collections import Counter

n = int(input())

words = [input() for _ in range(n)]
words_len = len(list(Counter(words).keys()))
distinct_words_len = ' '.join(str(x) for x in list(Counter(words).values()))

print(words_len)
print(distinct_words_len)