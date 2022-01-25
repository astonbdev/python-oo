from random import shuffle

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, url):
        self.url = url
        self.words = []

    def make_word_list(self):
        file = open(self.url)
        num_lines = 0

        for line in file:
            num_lines += 1
            self.words.append(line)

        file.close()

        print(f'{num_lines} words read')

    def random(self):

