import collections


def generate_ngrams_for_word(word, n):
    ngrams = []
    word = '_' * (n - 1) + word + '_' * (n - 1)
    for i in range(len(word) - n + 1):
        ngrams.append(word[i:i + n])
    return ngrams


def generate_ngrams(words, n):
    ngrams = []
    for word in words:
        ngrams.extend(generate_ngrams_for_word(word, n))

    return ngrams


def generate_ngrams_dict(ngrams):
    ngrams_dict = collections.defaultdict(int)
    for ngram in ngrams:
        ngrams_dict[ngram] = 1
    return ngrams_dict


def add_to_dict(ngrams_dict, ngrams):
    for ngram in ngrams:
        if ngram in ngrams_dict:
            ngrams_dict[ngram] += 1


def classify_ngrams(input_ngrams_dict, language_ngrams_dict, frequency_table_length=300):
    language_distance = 0
    for ngram in input_ngrams_dict:
        if ngram in language_ngrams_dict:
            language_distance += abs(language_ngrams_dict[ngram] - input_ngrams_dict[ngram])
        else:
            language_distance += frequency_table_length

    return language_distance
