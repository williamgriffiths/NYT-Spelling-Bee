f = open('unique_words.txt','r')
g = open('pangrams.txt','w')

for word in f:
    word = word.strip()
    if len(word) >= 7 and len(set(word)) == 7:
        g.write(word+"\n")