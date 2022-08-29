import os
import sqlite3
import uuid
from pathlib import Path
from random import choice
from typing import List, Union

amplifier_path = "word_lists/amplifiers.txt"
edder_path = "word_lists/edder.txt"
disgusting_path = "word_lists/disgusting.txt"
fucking_path = "word_lists/fucking.txt"
insult_path = "word_lists/insult.txt"

db = "insults.db"


class ListExhaustedException(Exception):
    def __init__(self, word_type):
        message = f"All possible {word_type} words have been used - request new id, or remove unique flag."
        super().__init__(message)


class Insult:
    def __init__(
        self,
        id: Union[str, None] = None,
        subject: Union[str, None] = None,
        unique: bool = False,
        alliteration: bool = False,
        nolog: bool = False,
    ):
        self.id = id
        self.subject = subject
        self.unique = unique
        self.alliteration = alliteration
        self.nolog = nolog

        self.con = self.get_db_con()

        self.amplifier_list = self.read_words(amplifier_path)
        self.edder_list = self.read_words(edder_path)
        self.disgusting_list = self.read_words(disgusting_path)
        self.fucking_list = self.read_words(fucking_path)
        self.insult_list = self.read_words(insult_path)

        self.found_amplifiers = []

    def get_db_con(self):
        if not os.path.isfile(db):
            con = sqlite3.connect(db)
            cur = con.cursor()
            cur.execute(
                """
                CREATE TABLE insults (
                    insult TEXT NOT NULL
                );
                """
            )
            cur.execute(
                """
                CREATE TABLE uuid_insult (
                    uuid TEXT NOT NULL,
                    insult_id INTEGER NOT NULL,
                    FOREIGN KEY(insult_id) REFERENCES insults(id)
                )
                """
            )
            return con
        return sqlite3.connect(db)

    def read_words(self, file_path: str):
        with open(file_path, "r") as f:
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

    def get_all_loged_insults(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT * FROM uuid_insult WHERE uuid = ?", (self.id,))
        rows = list(cur.fetchall())
        return rows

    def remove_logged_words(self, word_list):
        logged_insults = self.get_all_loged_insults()
        logged_insults_word_list = []
        for insult in logged_insults:
            for word in insult.split():
                logged_insults_word_list.appned(word)
        word_list_copy = word_list.copy()
        for word in word_list_copy:
            if word in logged_insults_word_list:
                word_list.remove(word)
        return word_list

    def log_insult(self, insult):
        cur = self.con.cursor()
        cur.execute("INSERT INTO insults VALUES(?)", (insult,))
        insult_id = cur.lastrowid
        self.con.commit()
        cur.execute("INSERT INTO uuid_insult VALUES(?,?)", (self.id, insult_id))
        self.con.commit()

    def get_word(self, word_list, word_type) -> Union[str, None]:
        if self.unique:
            word_list = self.remove_logged_words(word_list)
        word_list = self.remove_found_amplifiers(word_list)
        if not word_list:
            raise ListExhaustedException(word_type)
        return choice(word_list)

    def get_insult(self) -> (bool, str):

        if self.nolog and self.unique:
            return ("unique and nolog can not be used together", "")

        if self.unique and not self.id:
            self.id = str(uuid.uuid1())

        edder = self.get_word(self.edder_list, "edder type")
        disgusting = self.get_word(self.disgusting_list, "disgusting")
        fucking = self.get_word(self.fucking_list, "fucking")
        insult = self.get_word(self.insult_list, "insult")

        if not self.subject:
            full_insult = f"du er {edder} {disgusting}, din {fucking} {insult}"
        else:
            full_insult = (
                f"{self.subject} er {edder} {disgusting}, den {fucking} {insult}"
            )

        if not self.nolog:
            self.log_insult(full_insult)
        return (None, full_insult)