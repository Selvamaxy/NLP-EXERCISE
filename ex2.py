
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing"
tokens = word_tokenize(text)

print("The word Tokens are:")
print(tokens)