def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(get_letter_count(text))
    print_char_report(text, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if c in chars:
            chars[lowered]+=1
        else:
            chars[lowered] = 1
    return chars

def print_char_report(text, path):
    print(f"--- Begin report of {path} ---")
    print(f"{get_word_count(text)} words found in the document")
    char_report = get_letter_count(text)
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]



main()