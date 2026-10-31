#!/usr/bin/env python

from os import unlink
from pathlib import Path
from random import choice, sample

def load_a_word(min_len: int = 10, max_len: int = 15,
               dict_path: str = "/usr/share/dict/words") -> str:
    """Return a word whose length is between min_len and max_len."""

    words = [line.lower() for line in Path(dict_path).read_text().splitlines()]
    words = list(
        filter(lambda w: min_len <= len(w) <= max_len and w.isalpha(), words))
    word = choice(words)
    return word

def main():
    ''' main() '''
    hint_file = '/tmp/word.txt'
    word = load_a_word()
    Path(hint_file).write_text(word)
    print(f"Guess the scrambled word: {''.join(sample(word,len(word)))}")
    while guess_word := input("What is your guess word? \n").lower():
        if guess_word == word:
            print("Congratulations!!! You have correctly guess the word.")
            break
    unlink(Path(hint_file))


if __name__ == "__main__":
    main()