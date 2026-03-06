import sys
from . import reports
from . import analyzer



from . import tokenizer
def main(input_file, output_file):
    """Main entry point for the text analyzer."""
    # Parse command line arguments
    # Load text file
    # Run analysis
    # Generate reports

    text = "Clifford the dog is a dog that is a very very big dog."
    #instance = tokenizer()
    print(tokenizer.tokenize(text))

    with open(sys.argv[1], "r") as f:
        text = f.read()
    analyzer_instance = analyzer.TextAnalyzer(text)
    reports.generate_text_report(analyzer_instance.get_document_stats(),
                                 analyzer_instance.analyze(), sys.argv[2])

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])