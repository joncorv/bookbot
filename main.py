import operator


def main():
    path = "books/frankenstein.txt"
    full_text = get_book_text(path)
    word_count = get_word_count(full_text)
    char_freq = get_char_freq(full_text)
    report = make_report(path, char_freq, word_count)
    # print(report)
    # print(full_text, word_count, char_freq, report)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(full_text):
    count = len(full_text.split())
    return count

def get_char_freq(full_text):
    char_freq: Dict[str, int] = {}
    for char in full_text.lower():
        char_freq[char] = 1 + char_freq.get(char, 0)
    return char_freq

def make_report(path, char_freq, word_count):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'j', 'y', 'z']
    sorted_dict = dict(sorted(char_freq.items(), key=lambda x: x[1], reverse=True))
    line_01 = f"--- Begin report of {path} ---"
    line_02 = f"{word_count} words found in the document"
    line_03 = ""
    line_end = "--- End report ---"

    print(line_01, line_02, line_03, sep='\n')

    for key, value in sorted_dict.items():
        if key in chars:
            print(f"The '{key}' character was found {value} times")

    print(line_end)



if __name__ == "__main__":
    main()