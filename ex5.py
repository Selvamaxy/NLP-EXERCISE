def ngrams(text, n):
    words = text.split()
    for i in range(len(words)-n+1):
        print(words[i:i+n])

sentence = "I love learning artificial intelligence"
ngrams(sentence, 2)

def char_ngrams(text, n):
    text = text.replace(" ", "")   
    for i in range(len(text)-n+1):
        print(text[i:i+n])

sentence1 = "HELLO"
char_ngrams(sentence1, 2)
