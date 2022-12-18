import re
import collections

from languagetext import LanguageText
from fileinput import FileInput
from frequency import Frequency

ROOT_TEXT_FILES_DIRECTORY = 'languages'


def main():
    slo_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='slo')
    hr_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='hr')
    en_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='en')

    slo_frequency = Frequency(slo_text.words_list, ngrams_range=range(2, 5))
    print(slo_frequency.get_frequency_table())


if __name__ == '__main__':
    main()
