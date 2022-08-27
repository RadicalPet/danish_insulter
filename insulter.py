import argparse
from random import choice
from pathlib import Path


def read_words(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def find_amplifiers(word, found_amplifiers):
    amplifiers = read_words('amplifiers.txt')
    for amplifier in amplifiers:
        if amplifier in word:
            found_amplifiers.append(amplifier)
    return found_amplifiers

def remove_amplifiers(word_list):
    amplifiers = read_words('amplifiers.txt')
    word_list_copy = word_list.copy()
    for word in word_list_copy:
        for amplifier in amplifiers:
            if amplifier in word:
                try:
                    word_list.remove(word)
                except:
                    continue
    return word_list

def write_log(insult, log_path):
    with open(log_path, 'a') as f:
        f.write(f'{insult}\n')

def remove_logged_words(word_list, log_path):
    with open(log_path, 'r') as f:
        log = f.read()
    word_list_copy = word_list.copy()
    for word in word_list_copy:
        if word in log:
            word_list.remove(word)

    return word_list


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get some Danish insults')
    parser.add_argument('--subject', help='add subject for the insult (han/hen/hun/min chef etc.) - default is "du"')
    parser.add_argument('--log', help='path for logfile to append insult to')
    parser.add_argument('--unique',
            help='keep insult values unique to logfile - will demand new logfile once all possible values have been used for any position',
            action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    subject = args.subject
    log = args.log
    unique = args.unique

    if not log and unique:
        print('--unique needs --log to be set')
        exit(0)

    if log:
        Path(log).touch()

    edder_list = read_words('edder.txt')
    disgusting_list = read_words('disgusting.txt')
    fucking_list = read_words('fucking.txt')
    insult_list = read_words('insult.txt')

    found_amplifiers = []

    if unique:
        edder_list = remove_logged_words(edder_list, log)

    if not edder_list:
        print('all possible edder-class words have been used - add new logfile, or remove unique flag')
        exit(0)

    edder = choice(edder_list)
    amplifiers = find_amplifiers(edder, found_amplifiers)

    if unique:
        disgusting_list = remove_logged_words(disgusting_list, log)

    remove_amplifiers(disgusting_list)
    if not disgusting_list:
        print('all possible disgusting words have been used - add new logfile, or remove unique flag')
        exit(0)
    disgusting = choice(disgusting_list)
    amplifiers = find_amplifiers(disgusting, found_amplifiers)

    if unique:
        fucking_list = remove_logged_words(fucking_list, log)

    remove_amplifiers(fucking_list)
    if not disgusting_list:
        print('all possible fucking words have been used - add new logfile, or remove unique flag')
        exit(0)
    fucking = choice(fucking_list)
    amplifiers = find_amplifiers(fucking, found_amplifiers)

    if unique:
        insult_list = remove_logged_words(insult_list, log)

    if not disgusting_list:
        print('all possible insult words have been used - add new logfile, or remove unique flag')
        exit(0)

    remove_amplifiers(insult_list)
    insult = choice(insult_list)

    if not subject:
        insult = f'du er {edder} {disgusting}, din {fucking} {insult}'
        if log:
            write_log(insult, log)
        print(insult)
    else:
        insult = f'{subject} er {edder} {disgusting}, den {fucking} {insult}'
        if log:
            write_log(insult, log)
        print(insult)
