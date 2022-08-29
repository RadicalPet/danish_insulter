import argparse
from pathlib import Path
from random import choice


def read_words(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]


def find_amplifiers(word, found_amplifiers):
    amplifiers = read_words("amplifiers.txt")
    for amplifier in amplifiers:
        if amplifier in word:
            found_amplifiers.append(amplifier)
    return found_amplifiers


def remove_found_amplifiers(word_list, found_amplifiers):
    word_list_copy = word_list.copy()
    for word in word_list_copy:
        for amplifier in found_amplifiers:
            if amplifier in word:
                try:
                    word_list.remove(word)
                except:
                    continue
    return word_list


def write_log(insult, log_path):
    with open(log_path, "a") as f:
        f.write(f"{insult}\n")


def remove_logged_words(word_list, log_path):
    with open(log_path, "r") as f:
        log = f.read()
    word_list_copy = word_list.copy()
    for word in word_list_copy:
        if word in log:
            word_list.remove(word)

    return word_list


def find_word_starting_with_letter(word_list, letter):
    words_starting_with_letter = []
    for word in word_list:
        if word.startswith(letter):
            words_starting_with_letter.append(word)
    if words_starting_with_letter:
        return choice(words_starting_with_letter)
    else:
        return choice(word_list)


def get_word(word_list, found_amplifiers, word_type, log, unique, alliteration):

    if unique:
        word_list = remove_logged_words(word_list, log)

    word_list = remove_found_amplifiers(word_list, found_amplifiers)

    if not word_list:
        print(
            f"all possible {word_type}  words have been used - add new logfile, or remove unique flag"
        )
        exit(0)
    if alliteration:
        word = find_word_starting_with_letter(word_list, alliteration)
    else:
        word = choice(word_list)
    found_amplifiers = find_amplifiers(word, found_amplifiers)
    return word, found_amplifiers


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Get some Danish insults")
    parser.add_argument(
        "--subject",
        help='add subject for the insult (han/hen/hun/min chef etc.) - default is "du"',
    )
    parser.add_argument("--log", help="path for logfile to append insult to")
    parser.add_argument(
        "--unique",
        help="keep insult values unique to logfile - will demand new logfile once all possible values have been used for any position",
        action=argparse.BooleanOptionalAction,
    )
    parser.add_argument(
        "--alliteration",
        help="the insulter will try to use alliterations where possible",
        action=argparse.BooleanOptionalAction,
    )

    args = parser.parse_args()

    subject = args.subject
    log = args.log
    unique = args.unique
    alliteration = args.alliteration

    if not log and unique:
        print("--unique needs --log to be set")
        exit(0)

    if log:
        Path(log).touch()

    edder_list = read_words("edder.txt")
    disgusting_list = read_words("disgusting.txt")
    fucking_list = read_words("fucking.txt")
    insult_list = read_words("insult.txt")

    found_amplifiers = []
    letter = None

    edder, found_amplifiers = get_word(
        edder_list, found_amplifiers, "edder class", log, unique, letter
    )
    if alliteration:
        letter = edder[0]
    disgusting, found_amplifiers = get_word(
        disgusting_list, found_amplifiers, "disgusting", log, unique, letter
    )
    letter = None
    fucking, found_amplifiers = get_word(
        fucking_list, found_amplifiers, "fucking", log, unique, letter
    )
    if alliteration:
        letter = fucking[0]
    insult, found_amplifiers = get_word(
        insult_list, found_amplifiers, "insult", log, unique, letter
    )

    if not subject:
        insult = f"du er {edder} {disgusting}, din {fucking} {insult}"
        if log:
            write_log(insult, log)
        print(insult)
    else:
        insult = f"{subject} er {edder} {disgusting}, den {fucking} {insult}"
        if log:
            write_log(insult, log)
        print(insult)
