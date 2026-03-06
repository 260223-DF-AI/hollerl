from collections import Counter, defaultdict, namedtuple
from .models import WordFrequency, NGram, DocumentStats, AnalysisResult
from .tokenizer import tokenize, get_sentences, get_ngrams, remove_stopwords

from . import metrics

class TextAnalyzer:
    """Analyzes text documents for various metrics."""
    
    def __init__(self, text):
        self.text = text
        self.words = tokenize(text)
        self.sentences = get_sentences(text)
        self.word_counter = Counter(self.words)
    
    def get_word_frequencies(self, top_n=20, exclude_stopwords=True):
        """
        Get top N word frequencies.
        Returns: List of WordFrequency namedtuples
        """
        return Counter(self.words).most_common(top_n)
    
    def get_bigrams(self, top_n=10):
        """
        Get top N bigrams (2-word phrases).
        Returns: List of NGram namedtuples
        """
        return get_ngrams(self.words, 2)[:top_n]
    
    def get_trigrams(self, top_n=10):
        """
        Get top N trigrams (3-word phrases).
        Returns: List of NGram namedtuples
        """
        return get_ngrams(self.words, 3)[:top_n]
    
    def get_document_stats(self):
        """
        Calculate overall document statistics.
        Returns: DocumentStats namedtuple
        """
        avg_word = 0
        for word in self.words:
            avg_word += len(word)
        avg_word = avg_word / len(self.words)

        avg_sent = 0
        for sentence in self.sentences:
            avg_sent += len(sentence)
        avg_sent = avg_sent / len(self.words)
        DocumentStats = namedtuple("DocumentStats",
                                   ["num_words", "num_unique_words",
                                    "num_sentences", "avg_word_len", "avg_sent_len"])
        return DocumentStats(len(self.words),len(set(self.words)),
                               len(self.sentences), avg_word, avg_sent)
    
    def get_word_length_distribution(self):
        """
        Group words by length.
        Returns: defaultdict mapping length -> list of words
        """
        grouped = defaultdict(list)
        for word in self.words:
            grouped[len(word)].append(word)
        return grouped
    
    def analyze(self):
        """
        Run complete analysis.
        Returns: AnalysisResult namedtuple
        """

        score = metrics.flesch_reading_ease(len(self.words), len(self.sentences), metrics.count_syllables(self.words))
        grade = ""

        if score >= 90:
            grade = "Very Easy (5th Grade - 11-year-olds)"
        elif score >= 80:
            grade = "Easy (6th Grade)"
        elif score >= 70:
            grade = "Fairly Easy (7th Grade)"
        elif score >= 60:
            grade = "Standard (8th–9th Grade - 13–15 year olds)"
        elif score >= 50:
            grade = "Fairly Difficult (High School - 10th–12th Grade)"
        elif score >= 30:
            grade = "Difficult (College Level)"
        else:
            grade = "Very Difficult (College Graduate/Academic)"

        AnalysisResult = namedtuple("AnalysisResult", ["word_count", "bigrams", "score", "grade"])
        return AnalysisResult(self.get_word_frequencies(10), self.get_bigrams(5), score, grade)