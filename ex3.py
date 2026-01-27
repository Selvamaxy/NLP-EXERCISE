import nltk
import re
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

# ================= DOWNLOADS (RUNS ONLY FIRST TIME) =================
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')
# ====================================================================

# ================= INPUT =================
text = input("Enter text: ").lower()

# ================= CLEANING =================
text = re.sub(r'[^a-z ]', '', text)

# ================= TOKENIZATION =================
tokens = nltk.word_tokenize(text)

# ================= STOP WORD REMOVAL =================
stop_words = set(stopwords.words('english'))

# ================= POS TAG MAPPING =================
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# ================= POS TAGGING =================
pos_tags = nltk.pos_tag(tokens)

# ================= LEMMATIZATION =================
lemmatizer = WordNetLemmatizer()
final_words = []

for word, tag in pos_tags:
    if word not in stop_words:
        wn_tag = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word, wn_tag)
        final_words.append(lemma)

# ================= OUTPUT =================
print("\nAfter preprocessing:")
print(final_words)
