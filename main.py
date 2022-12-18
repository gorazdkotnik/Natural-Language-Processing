import re
import collections

from languagetext import LanguageText
from fileinput import FileInput
from frequency import Frequency
from ngrams import classify_ngrams

ROOT_TEXT_FILES_DIRECTORY = 'languages'


def main():
    slo_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='slo', read_json=True)
    hr_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='hr', read_json=True)
    en_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='en', read_json=True)

    slo_frequency = Frequency(slo_text.get_language(), slo_text.get_words_list(), ngrams_range=range(2, 5),
                              read_json=True)
    hr_frequency = Frequency(hr_text.get_language(), hr_text.get_words_list(), ngrams_range=range(2, 5),
                             read_json=True)
    en_frequency = Frequency(en_text.get_language(), en_text.get_words_list(), ngrams_range=range(2, 5),
                             read_json=True)

    input_frequency = Frequency('input', FileInput('input.txt').get_content(), ngrams_range=range(2, 5))

    slo_distance = classify_ngrams(input_frequency.get_frequency_table(), slo_frequency.get_frequency_table())
    hr_distance = classify_ngrams(input_frequency.get_frequency_table(), hr_frequency.get_frequency_table())
    en_distance = classify_ngrams(input_frequency.get_frequency_table(), en_frequency.get_frequency_table())

    language_distances = {'slovene': slo_distance, 'croatian': hr_distance, 'english': en_distance}
    print('The input text is most likely written in',
          (min(language_distances, key=language_distances.get)).upper() + '.')


if __name__ == '__main__':
    main()
