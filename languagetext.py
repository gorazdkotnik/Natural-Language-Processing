import os
import re


def process_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    return text.split();


class LanguageText:
    def __init__(self, root_directory, language):
        self.root_directory = root_directory
        self.language = language
        self.text_list = []

        self.__read_text()

    def __read_text(self):
        files = os.listdir(self.root_directory + '/' + self.language)

        for file in files:
            if file.endswith('.txt'):
                with open(self.root_directory + '/' + self.language + '/' + file, 'r') as f:
                    contents = f.read()
                    self.text_list.append(process_text(contents))
