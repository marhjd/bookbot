def main():
    path = "books/frankenstein.txt"

    report = print_report(path)
    print(report)

def get_text(path):
    with open(path, "r") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count = {}
    for c in text:
        lowered = c.lower()
        if lowered in count:
            count[lowered] += 1
        else:
            count[lowered] = 1
    return count

def print_report(book_path):
    text = get_text(book_path)

    word_count = count_words(text)
    charcount = count_characters(text)
    charcount_sorted_desc = sorted(charcount.items(), key=lambda item: item[1], reverse=True)

    charcount_summary = ""
    for char_tuple in charcount_sorted_desc:
        if char_tuple[0].isalpha():
            charcount_summary += f"The '{char_tuple[0]}' character was found {char_tuple[1]} times\n"

    charcount_summary += "--- End report ---"

    return f"""--- Begin report of {book_path} ---
{word_count} words found in the document

{charcount_summary}"""

if __name__ == '__main__':
    main()
