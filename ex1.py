import re
text ="Data science and machine learning are importent in AI Apllication"

pattern1=r'\band\b'
pattern2=r"\b\D{4}\b"
pattern3=r"\b[a-zA-Z]{7}\b"


def detect_word_pattern(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        print(matches)
        print("word pattern detected")
    else:
        print("word pattern not detected")   
detect_word_pattern(pattern1,text)         
detect_word_pattern(pattern2,text)         
detect_word_pattern(pattern3,text)         