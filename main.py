from languagetext import LanguageText
from fileinput import FileInput
from frequency import Frequency
from ngrams import classify_ngrams
from graphs import draw_distance_bar_chart, draw_top_ngrams_bar_chart

ROOT_TEXT_FILES_DIRECTORY = 'languages'
NGRAMS_RANGE = range(2, 6)
READ_JSON = True


def main():
    # Read all the text files in the languages directory
    slo_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='slo', read_json=READ_JSON)
    hr_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='hr', read_json=READ_JSON)
    en_text = LanguageText(ROOT_TEXT_FILES_DIRECTORY, language='en', read_json=READ_JSON)

    # Create a frequency dictionary for each language
    slo_frequency = Frequency(slo_text.get_language(), slo_text.get_words_list(), NGRAMS_RANGE,
                              read_json=READ_JSON)
    hr_frequency = Frequency(hr_text.get_language(), hr_text.get_words_list(), NGRAMS_RANGE,
                             read_json=READ_JSON)
    en_frequency = Frequency(en_text.get_language(), en_text.get_words_list(), NGRAMS_RANGE,
                             read_json=READ_JSON)

    # Create a frequency dictionary for the input text
    input_frequency = Frequency('input', FileInput('input.txt').get_content(), NGRAMS_RANGE)

    # Classify the input text
    slo_distance = classify_ngrams(input_frequency.get_frequency_table(), slo_frequency.get_frequency_table())
    hr_distance = classify_ngrams(input_frequency.get_frequency_table(), hr_frequency.get_frequency_table())
    en_distance = classify_ngrams(input_frequency.get_frequency_table(), en_frequency.get_frequency_table())

    # Plot the results
    language_distances = {'slovene': slo_distance, 'croatian': hr_distance, 'english': en_distance}
    print('The input text is most likely written in',
          (min(language_distances, key=language_distances.get)).upper() + '.')

    draw_distance_bar_chart(language_distances)

    draw_top_ngrams_bar_chart('slovene', slo_frequency.get_frequency_table())
    draw_top_ngrams_bar_chart('croatian', hr_frequency.get_frequency_table())
    draw_top_ngrams_bar_chart('english', en_frequency.get_frequency_table())


if __name__ == '__main__':
    main()
