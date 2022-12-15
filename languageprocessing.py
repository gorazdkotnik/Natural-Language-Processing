import collections
from ngrams import generate_ngrams_dict, generate_ngrams_for_word

class LanguageProcessing:
    def __init__(self, text_words_list, input_words_list, ngrams_range):
        self.__text_words_list = text_words_list
        self.__input_words_list = input_words_list

        self.__text_ngrams = []
        self.__input_ngrams = []

        self.ngrams_dict = collections.defaultdict(int)

        for n in ngrams_range:
            self.__generate_text_ngrams(n)
            self.__generate_input_ngrams(n)

        self.__text_ngrams = list(set(self.__text_ngrams))
        self.__input_ngrams = self.__input_ngrams

        self.ngrams_dict = generate_ngrams_dict(self.__text_ngrams)

        for ngram in self.__input_ngrams:
            if ngram in self.ngrams_dict:
                self.ngrams_dict[ngram] += 1

        self.ngrams_dict = dict(sorted(self.ngrams_dict.items(), key=lambda item: item[1], reverse=True))

    def __generate_text_ngrams(self, n):
        for word in self.__text_words_list:
            self.__text_ngrams.extend(generate_ngrams_for_word(word, n))

    def __generate_input_ngrams(self, n):
        for word in self.__input_words_list:
            self.__input_ngrams.extend(generate_ngrams_for_word(word, n))
