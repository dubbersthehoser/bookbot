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


def select_char_count(line):
    p1 = line.find('found') + len('found ')
    p2 = line.find(' times')
    number = line[p1:p2]
    return int(number)

def main():
    path_to_file = 'books/frankenstein.txt'

    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)

    char_count_lines = []
    for k, v in char_count.items():
        line = f"the '{k}' character was found {v} times"
        char_count_lines.append(line)

    char_count_lines.sort(key=select_char_count, reverse=True)
    
    output_lines = [
        f"--- Begin report of {path_to_file} ---",
        f"{word_count} words found in the document",
        "",
        "",
        *char_count_lines,
        f"--- End report ---"
        ]

    print('\n'.join(output_lines))

main()
