def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    print(text)
    print("wordcount: ", count_words(text))

def get_text(path):
    with open(path, "r") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    main()
