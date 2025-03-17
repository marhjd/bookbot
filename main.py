from stats import count_words, count_characters
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    report = print_report(path)
    print(report)

def get_text(path):
    with open(path, "r") as f:
        file_contents = f.read()
        return file_contents

def print_report(book_path):
    text = get_text(book_path)

    word_count = count_words(text)
    charcount = count_characters(text)
    charcount_sorted_desc = sorted(charcount.items(), key=lambda item: item[1], reverse=True)

    charcount_summary = ""
    for char_tuple in charcount_sorted_desc:
        if char_tuple[0].isalpha():
            charcount_summary += f"{char_tuple[0]}: {char_tuple[1]}\n"

    charcount_summary += "--- End report ---"

    return f"""--- Begin report of {book_path} ---
{word_count} words found in the document

{charcount_summary}"""

if __name__ == '__main__':
    main()
