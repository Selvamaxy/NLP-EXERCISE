def chunk(sentence):
    
    words = sentence.split()


    for i in range(len(words)-1):

        if words[i].lower() in ['a','an','the']:
            print("NP ->", words[i], words[i+1])
sentence = "The smart student solved a complex problem"

chunk(sentence)