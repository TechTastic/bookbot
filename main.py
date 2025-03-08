import sys
from stats import get_word_count
from stats import get_unique_character_counts
from stats import split_and_sort_character_counts

def get_book_text(path):
    print(f"Analyzing book found at {path}...")
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    book_file = sys.argv[1]
    book = get_book_text(book_file)

    print("----------- Word Count ----------")
    word_count = get_word_count(book)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    unique_char_count = get_unique_character_counts(book)
    sorted_counts = split_and_sort_character_counts(unique_char_count)
    for count in sorted_counts:
        char = count["char"]
        if (char.isalpha()):
            print(f"{char}: {count["count"]}")

    print("============= END ===============")

main()