import collections
import json
from ngrams import generate_ngrams, generate_ngrams_dict, add_to_dict


class Frequency:
    def __init__(self, frequency_name, words_list, ngrams_range, read_json=False, frequency_table_length=300):
        self.__words_list = words_list
        self.__language = frequency_name
        self.__frequency_table_length = frequency_table_length

        self.__ngrams = []
        self.__ngrams_dict = collections.defaultdict(int)

        if read_json:
            with open('frequency/' + self.__language + '.json', 'r') as f:
                self.__ngrams_dict = json.load(f)
        else:
            self.__generate_frequency_table(ngrams_range)

    def __generate_frequency_table(self, ngrams_range):
        for n in ngrams_range:
            self.__ngrams.extend(generate_ngrams(self.__words_list, n))

        self.__ngrams_dict = generate_ngrams_dict(list(set(self.__ngrams)))
        add_to_dict(self.__ngrams_dict, self.__ngrams)
        self.__ngrams_dict = dict(
            sorted(self.__ngrams_dict.items(), key=lambda item: item[1], reverse=True)[:self.__frequency_table_length])

        with open('frequency/' + self.__language + '.json', 'w') as f:
            json.dump(self.__ngrams_dict, f)

    def get_frequency_table(self):
        return self.__ngrams_dict
