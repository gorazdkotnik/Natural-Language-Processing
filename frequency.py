import collections
from ngrams import generate_ngrams, generate_ngrams_dict, add_to_dict


class Frequency:
    def __init__(self, words_list, ngrams_range):
        self.__words_list = words_list

        self.__ngrams = []
        self.__ngrams_dict = collections.defaultdict(int)

        for n in ngrams_range:
            self.__ngrams.extend(generate_ngrams(self.__words_list, n))

        self.__ngrams_dict = generate_ngrams_dict(list(set(self.__ngrams)))

        add_to_dict(self.__ngrams_dict, self.__ngrams)

        self.__ngrams_dict = dict(sorted(self.__ngrams_dict.items(), key=lambda item: item[1], reverse=True)[:300])

    def get_frequency_table(self):
        return self.__ngrams_dict
