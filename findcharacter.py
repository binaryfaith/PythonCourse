# input
word_list = ['hello','world','my','name','is','Anna']
char = set('o')
new = []
for word in word_list:
    if char & set(word):
        new.append(word)
print new