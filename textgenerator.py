from faker import Faker
import os


class TextGenerator:
    def __init__(self, language, length, filename):
        self.__folder = 'languages/'
        self.language = language
        self.length = length
        self.filename = filename

    def generate(self):
        self.__create_folder()
        self.__create_file()

    def __create_folder(self):
        if not os.path.exists(self.__folder):
            os.mkdir(self.__folder)

    def __create_file(self):
        file = open(self.__folder + self.filename, 'w')
        for _ in range(self.length):
            file.write(self.__generate_text() + ' ')
        file.close()

    def __generate_text(self):
        return Faker(self.language).text(self.length)
