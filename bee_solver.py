dct = open('unique_words.txt','r')

def anagram(word,letters):
    word = word.strip()
    for letter in word:
        if letter not in letters:
            return False
    return True

def words(letters,centre):
    answers = []
    for word in dct:
        word = word.strip()
        if anagram(word,letters) == True:
            if centre in word:
                answers.append(word)
    return sorted(answers,key=len, reverse=True)


# print(words('gtneibx','e'))