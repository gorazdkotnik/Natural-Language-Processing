import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


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
