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
