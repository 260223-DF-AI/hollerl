from collections import OrderedDict

from datetime import datetime
from . import analyzer

def generate_text_report(analysis_result, analyze, output_path):
    """
    Generate a formatted text report.
    
    Sections:
    1. Document Overview
    2. Top Words
    3. Top Phrases (bigrams/trigrams)
    4. Readability Assessment
    """
    report = f"""=== Text Analysis Report ===
    Generated: {datetime.now():%Y-%m-%d %H:%M:%S}

    Document Statistics:
     - Word Count: {analysis_result[0]}
     - Unique Words: {analysis_result[1]}
     - Sentence Count: {analysis_result[2]}
     - Average Word Length: {analysis_result[3]:.2f}
     - Average Sentence Length: {analysis_result[4]:.2f}

    Top 10 Words (excluding stopwords):"""
    for index, word in enumerate(analyze[0]):
        report = report + f"\n     {index + 1}. {word[0]} ({word[1]}) - ({(word[1]/analysis_result[0]):.2f}%)"
    report = report + "\n\n     Top 5 Bigrams:"
    for index, bigram in enumerate(analyze[1]):
        report = report + f"\n     {index + 1}. \"{bigram[0]}\" ({bigram[1]})"

    report = report + "\n\n     Readability:" + f"\n     - Flesch Reading Ease: {analyze[2]:.2f} ({analyze[3]})"

    with open(output_path + "\output.txt", "w") as text_file:
        text_file.write(report)

def generate_word_cloud_data(word_frequencies):
    """
    Prepare data for word cloud visualization.
    Returns: OrderedDict of word -> weight (ordered by frequency)
    """
    return analyzer.get_word_frequencies()

def generate_frequency_table(word_frequencies):
    """
    Generate a formatted frequency table.
    Uses OrderedDict to maintain ranking order.
    """
    pass