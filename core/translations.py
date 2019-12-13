import builtins
import csv
import os


class Translator:
    def __init__(self):
        self.language = os.getenv('language')
        self.texts = {}
        self.generate_texts()

    def generate_texts(self):
        with open(f'languages/{self.language}.csv') as f:
            reader = csv.reader(f, dialect='unix')

            for n, row in enumerate(reader):
                if n != 0:
                    self.texts[row[0]] = row[1]

    def translate(self, identifier):
        return self.texts.get(identifier, identifier)


def init():
    builtins._ = Translator().translate
