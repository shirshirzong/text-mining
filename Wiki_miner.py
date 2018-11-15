import wikipedia
import string
import pickle

# class Page(object):
#     def __init__(self, page, pagename):
#         self.page = wikipedia.page(pagename)
#         self.pagename = pagename or ""


# babson = wikipedia.page("Babson College")
# print(babson.title)
# print(babson.url)
# print(babson.content)

def process_page(pagename):
    """Makes a histogram that contains the words from a page.
    pagename: string
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = wikipedia.page(pagename)

    for line in fp:
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist


def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.
    returns: list of (frequency, word) pairs
    """
    t = []

    stopwords = process_file('stopwords.txt', False)

    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)





# bu= wikipedia.page ("Boston University")
# print (bu.title)
# print (bu.url)
# print (bu.content)

# bc= wikipedia.page ("Boston College")
# print (bc.title)
# print (bc.url)
# print (bc.content)

# bentley= wikipedia.page ("Bentley University")
# print (bentley.title)
# print (bentley.url)
# print (bentley.content)


def main():
    hist = process_page('Babson College')
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist, False)

    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    print_most_common(hist)



if __name__ == '__main__':
    main()