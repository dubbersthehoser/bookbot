def count_words(content):
    words = content.split()
    while '' in words:
        words.remove('')
    return len(words)

def count_chars(content):
    count_map = {}
    for c in content:
        if c.isalpha():
            count_map.setdefault(c.lower(), 0)
            count_map[c.lower()] += 1
    return count_map


