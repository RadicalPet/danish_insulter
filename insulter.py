import argparse
from random import choice


def read_words(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get some Danish insults')
    parser.add_argument('--subject', help='add subject for the insult (han/hen/hun/min chef etc.) - default is "du"')
    args = parser.parse_args()

    subject = args.subject

    edder_list = read_words('edder.txt')
    disgusting_list = read_words('disgusting.txt')
    fucking_list = read_words('fucking.txt')
    insult_list = read_words('insult.txt')

    edder = choice(edder_list)
    disgusting = choice(disgusting_list)
    fucking = choice(fucking_list)
    insult = choice(insult_list)
    
    if not subject:
        print(f'du er {edder} {disgusting}, din {fucking} {insult}')
    else:
        print(f'{subject} er {edder} {disgusting}, den {fucking} {insult}')
