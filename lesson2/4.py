words = input('Input words: ')
words_list = words.split(' ')
for i, n in enumerate(words_list, start=1):
    print(i, n[0:10])
