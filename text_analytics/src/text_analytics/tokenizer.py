import re
from collections import Counter

default_stop_words = (
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", 
    "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", 
    "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", 
    "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", 
    "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", 
    "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", 
    "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", 
    "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", 
    "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", 
    "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", 
    "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", 
    "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", 
    "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", 
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", 
    "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", 
    "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", 
    "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", 
    "yours", "yourself", "yourselves")

def tokenize(text):
    """
    Split text into words.
    - Convert to lowercase
    - Remove punctuation
    - Remove extra whitespace
    Returns: List of words
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.split()
    return text

def get_sentences(text):
    """
    Split text into sentences.
    - Handle abbreviations (Dr., Mr., etc.)
    - Handle multiple punctuation (!! or ...)
    Returns: List of sentences
    """
    return re.split(r'(?<!\b\w\.)(?<!\bMr\.)(?<!\bMrs\.)(?<!\bDr\.)(?<=[.?!])\s+(?=[A-Z])', text)

def get_ngrams(words, n):
    """
    Generate n-grams from a list of words.
    Example: get_ngrams(['a', 'b', 'c'], 2) -> [('a', 'b'), ('b', 'c')]
    Returns: List of tuples
    """
    x=0
    n_grams = []
    while x < len(words) - n + 1:
        element = []
        y = x
        while y < x + n:
            element.append(words[y])
            y += 1
        n_grams.append(tuple(element))
        x += 1
    return n_grams

def remove_stopwords(words, stopwords=default_stop_words):
    """
    Remove common stopwords from word list.
    Use a default set if stopwords not provided.
    Returns: Filtered list of words
    """
    filtered = filter(lambda word: word not in stopwords, words)

    return list(filtered)
