from stats import count_words
from stats import count_characters
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    num_words = count_words(contents)
    print(f"Analyzing book found at {filepath}")
    print("Word Count")
    print(f"Found {num_words} total words")
    report = count_characters(contents)
    report = sort_dict(report)
    for pair in report:
        print(f"{pair[0]}: {pair[1]}")


main()