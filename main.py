from stats import count_words
from stats import count_chars
from stats import select_char_count

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
