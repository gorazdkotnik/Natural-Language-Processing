import re
import collections

from languagetext import LanguageText

ROOT_TEXT_FILES_DIRECTORY = 'languages'


def main():
    slo_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, 'slo')
    hr_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, 'hr')
    en_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, 'en')

    for text in en_text.text_list:
        print(text)
        print()
    """
    file = FileInput('input.txt')

    input_text = file.get_content()

    en_text = FileInput('languages/en.txt').get_content()
    sl_text = FileInput('languages/sl.txt').get_content()
    hr_text = FileInput('languages/hr.txt').get_content()

    en_words = process_text(en_text)
    en_ngrams = generate_ngrams(en_words, 3)
    en_ngrams_dict = generate_ngrams_dict(en_ngrams)

    sl_words = process_text(sl_text)
    sl_ngrams = generate_ngrams(sl_words, 3)
    sl_ngrams_dict = generate_ngrams_dict(sl_ngrams)

    hr_words = process_text(hr_text)
    hr_ngrams = generate_ngrams(hr_words, 3)
    hr_ngrams_dict = generate_ngrams_dict(hr_ngrams)

    input_words = process_text(input_text)
    input_ngrams = generate_ngrams(input_words, 3)

    en_ngrams_dict = classify_ngrams(en_ngrams_dict, input_ngrams)
    sl_ngrams_dict = classify_ngrams(sl_ngrams_dict, input_ngrams)
    hr_ngrams_dict = classify_ngrams(hr_ngrams_dict, input_ngrams)

    print(sum_values(en_ngrams_dict))
    print(sum_values(sl_ngrams_dict))
    print(sum_values(hr_ngrams_dict))
    """


def process_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z ]', '', text)
    return text.split()


def generate_ngrams(words, n):
    ngrams = []
    for word in words:
        ngrams.extend(generate_ngrams_for_word(word, n))

    return list(set(ngrams))


def generate_ngrams_for_word(word, n):
    ngrams = []
    word = '_' * (n - 1) + word + '_' * (n - 1)
    for i in range(len(word) - n + 1):
        ngrams.append(word[i:i + n])
    return ngrams


def generate_ngrams_dict(ngrams):
    ngrams_dict = collections.defaultdict(int)
    for ngram in ngrams:
        ngrams_dict[ngram] = 0
    return ngrams_dict


def classify_ngrams(ngrams_dict, input_ngrams):
    for ngram in ngrams_dict:
        for input_ngram in input_ngrams:
            if ngram == input_ngram:
                ngrams_dict[ngram] += 1
    return ngrams_dict


# method to sum the values of the dictionary
def sum_values(ngrams_dict):
    return sum(ngrams_dict.values())


if __name__ == '__main__':
    main()
