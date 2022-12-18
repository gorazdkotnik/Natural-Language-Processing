import os
import re
import json


def process_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    return text.split();


class LanguageText:
    def __init__(self, root_directory, language, read_json=False):
        self.root_directory = root_directory
        self.language = language
        self.words_list = []

        if read_json:
            with open(self.root_directory + '/' + self.language + '.json', 'r') as f:
                self.words_list = json.load(f)
        else:
            self.__read_text()

    def __read_text(self):
        files = os.listdir(self.root_directory + '/' + self.language)

        text_words_list = []

        for file in files:
            if file.endswith('.txt'):
                with open(self.root_directory + '/' + self.language + '/' + file, 'r') as f:
                    contents = f.read()
                    text_words_list.append(process_text(contents))

        self.__generate_words_list(text_words_list)

    def __generate_words_list(self, text_words_list):
        self.words_list = []
        for sublist in text_words_list:
            for item in sublist:
                self.words_list.append(item)

        self.words_list = list(set(self.words_list))

        with open(self.root_directory + '/' + self.language + '.json', 'w') as f:
            json.dump(self.words_list, f)

    def get_words_list(self):
        return self.words_list

    def get_language(self):
        return self.language
