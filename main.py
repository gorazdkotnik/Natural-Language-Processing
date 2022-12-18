import re
import collections

from languagetext import LanguageText
from fileinput import FileInput
from frequency import Frequency

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

    print('Slovenian frequency table:')
    print(slo_frequency.get_frequency_table())
    print('Croatian frequency table:')
    print(hr_frequency.get_frequency_table())
    print('English frequency table:')
    print(en_frequency.get_frequency_table())


if __name__ == '__main__':
    main()
