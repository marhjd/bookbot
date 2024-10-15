def main():
    path = "books/frankenstein.txt"

    text = get_text(path)
    print("text:", text)

    wordcount = count_words(text)
    print("wordcount:", wordcount)

    charcount = count_characters(text)
    print("charcount:", charcount)

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

if __name__ == '__main__':
    main()
