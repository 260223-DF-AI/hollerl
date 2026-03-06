import pytest
from text_analytics.analyzer import TextAnalyzer
from text_analytics.tokenizer import tokenize, get_ngrams, get_sentences, remove_stopwords

def test_tokenize_basic():
    """Test basic tokenization."""
    assert (tokenize("Clifford the dog is a dog that is a very very big dog.") ==
            ['clifford', 'the', 'dog', 'is', 'a', 'dog', 'that', 'is', 'a', 'very', 'very', 'big', 'dog'])

def test_get_ngrams():
    """Test get_ngrams function."""
    assert (get_ngrams(['clifford', 'the', 'dog', 'is', 'a', 'dog', 'that', 'is', 'a', 'very', 'very', 'big', 'dog'],
                       2) ==
            [('clifford', 'the'), ('the', 'dog'), ('dog', 'is'), ('is', 'a'), ('a', 'dog'), ('dog', 'that'), ('that', 'is'), ('is', 'a'), ('a', 'very'), ('very', 'very'), ('very', 'big'), ('big', 'dog')])

def test_get_sentences():
    """Test get_sentences function."""
    assert(get_sentences("Clifford is a dog. He is a very big dog.") ==
           ['Clifford is a dog.', 'He is a very big dog.'])

def test_remove_stopwords():
    """Test remove_stopwords function."""
    assert(remove_stopwords(['clifford', 'the', 'dog', 'is', 'a', 'dog', 'that', 'is', 'a', 'very', 'very', 'big', 'dog']) ==
           ['clifford', 'dog', 'dog', 'big', 'dog'])