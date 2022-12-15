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
        self.words_list = []

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
