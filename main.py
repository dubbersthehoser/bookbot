import sys

from stats import count_words
from stats import count_chars

def select_char_count(line):
    number = line[3:]
    return int(number)

def main():
    if len(sys.argv) == 1:
        sys.exit(1)

    path_to_file = sys.argv[1]

    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)

    char_count_lines = []
    for k, v in char_count.items():
        line = f"{k}: {v}"
        char_count_lines.append(line)

    char_count_lines.sort(key=select_char_count, reverse=True)
    
    output_lines = [
        f"============ BOOKBOT ============"
        f"Analyzing book found at {path_to_file}...",
        "----------- Word Count ----------",
        f"Found {word_count} total words",
        "--------- Character Count -------",
        *char_count_lines,
        f"============= END ==============="
        ]

    print('\n'.join(output_lines))




if __name__ == '__main__':
    main()
