from random import choice
from pathlib import Path
from typing import List

amplifier_path = 'amplifiers.txt'
edder_path = 'edder.txt'
disgusting_path = 'disgusting.txt'
fucking_path = 'fucking.txt'
insult_path = 'insult.txt'


class Insult:

    def __init__(self, subject: str = None, unique: bool = False, alliteration: bool = False):
        self.subject = subject
        self.unique = unique
        self.alliteration = alliteration

        self.amplifier_list = self.read_words(amplifier_path)
        self.edder_list = self.read_words(edder_path)
        self.disgusting_list = self.read_words(disgusting_path)
        self.fucking_list = self.read_words(fucking_path)
        self.insult_list = self.read_words(insult_path)

        self.found_amplifiers = []

    def read_words(self, file_path: str):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            return [line.rstrip() for line in lines]

    def find_amplifiers(self, word: str) -> List:
        for amplifier in self.amplifier_list:
            if amplifier in word:
                self.found_amplifiers.append(amplifier)

    def remove_found_amplifiers(self, word_list: List) -> List:
        word_list_copy = word_list.copy()
        for word in word_list_copy:
            for amplifier in self.found_amplifiers:
                if amplifier in word:
                    try:
                        word_list.remove(word)
                    except:
                        continue

        return word_list

    def get_word(self, word_list):
        word_list = self.remove_found_amplifiers(word_list)
        return choice(word_list)

    def get_insult(self):
        edder = self.get_word(self.edder_list)
        disgusting = self.get_word(self.disgusting_list)
        fucking = self.get_word(self.fucking_list)
        insult = self.get_word(self.insult_list)
        full_insult = f'du er {edder} {disgusting}, din {fucking} {insult}'
        return full_insult
