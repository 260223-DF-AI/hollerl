import pytest
from text_analytics.analyzer import TextAnalyzer
from text_analytics.tokenizer import tokenize, get_ngrams

def test_word_frequency_ranking():
    """Test that words are ranked correctly by frequency."""
    analyzer_instance = TextAnalyzer("Clifford the dog is a dog that is a very very big dog.")
    assert (analyzer_instance.get_word_frequencies() ==
            [('dog', 3), ('is', 2), ('a', 2), ('very', 2), ('clifford', 1), ('the', 1), ('that', 1), ('big', 1)])

def test_bigram_generation():
    """Test bi-gram generation."""
    analyzer_instance = TextAnalyzer("Clifford the dog is a dog that is a very very big dog.")
    assert(analyzer_instance.get_bigrams() ==
           [('clifford', 'the'), ('the', 'dog'), ('dog', 'is'), ('is', 'a'), ('a', 'dog'), ('dog', 'that'), ('that', 'is'), ('is', 'a'), ('a', 'very'), ('very', 'very')])

def test_trigram_generation():
    """Test trigram generation."""
    analyzer_instance = TextAnalyzer("Clifford the dog is a dog that is a very very big dog.")
    assert(analyzer_instance.get_trigrams(5) ==
           [('clifford', 'the', 'dog'), ('the', 'dog', 'is'), ('dog', 'is', 'a'), ('is', 'a', 'dog'), ('a', 'dog', 'that')])

def test_get_document_stats():
    """Test getting document statistics."""
    analyzer_instance = TextAnalyzer("Clifford the dog is a dog that is a very very big dog.")
    assert(analyzer_instance.get_document_stats()[0] == 13)