import string
from collections import Counter

def word_cloud(a):
    words = [''.join([c for c in s if c not in string.punctuation]).lower() for s in a.split()]
    c = Counter(words)
    return c
    
print(word_cloud('After beating the eggs, Dana read the next step:'))