dictionary = {

"bank": [

"financial institution that keeps money",

"side of a river"

]

}

def lesk(word, sentence):

    context = set(sentence.lower().split())

    best_sense, max_overlap = None, 0


    for sense in dictionary[word]:

        gloss = set(sense.split())

        overlap = len(context & gloss)


    if overlap > max_overlap:

            best_sense, max_overlap = sense, overlap
    return best_sense


sentence = "He went to the bank to deposit money"

word = "bank"


print("Word:", word)

print("Best Sense:", lesk(word, sentence))