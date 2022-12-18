from languagetext import LanguageText
from fileinput import FileInput
from frequency import Frequency
from ngrams import classify_ngrams
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT_TEXT_FILES_DIRECTORY = 'languages'
NGRAMS_RANGE = range(2, 5)
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


def draw_distance_bar_chart(language_distances):
    for language_distance in language_distances:
        if language_distances[language_distance] == min(language_distances.values()):
            plt.bar(language_distance, language_distances[language_distance], color='green', width=0.5)
        else:
            plt.bar(language_distance, language_distances[language_distance], color='red', width=0.5)

    plt.xticks(range(len(language_distances)), language_distances.keys())

    plt.title('Distance between input text and language n-grams')
    plt.xlabel('Language')
    plt.ylabel('Distance')

    legend_elements = [Line2D([0], [0], color='green', lw=4, label='Predicted language'),
                       Line2D([0], [0], color='red', lw=4, label='Other languages')]
    plt.legend(handles=legend_elements)

    plt.show()


def draw_top_ngrams_bar_chart(title, language_ngrams_dict):
    top_ngrams = dict(list(language_ngrams_dict.items())[:10])
    top_ngrams = dict(sorted(top_ngrams.items(), key=lambda item: item[1], reverse=False))

    for ngram in top_ngrams:
        plt.barh(ngram, top_ngrams[ngram])

    plt.yticks(range(len(top_ngrams)), top_ngrams.keys())

    plt.title('Top 10 n-grams for ' + title + ' language')
    plt.xlabel('Frequency')
    plt.ylabel('N-gram')

    plt.show()


if __name__ == '__main__':
    main()
