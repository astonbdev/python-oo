from email.utils import parsedate
from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """takes in url, sets to self.url, initializes self.words"""
        self.words = self.parse_file(path)
        #self.make_word_list()
        #make_word_list(open(url))

    def parse_file(self, path):
        """uses self.url for file path, opens file and reads 
        line by line, appending word to self.words"""
        file = open(path)
        num_lines = 0
        parsed_words = []
        parsed_words = [parsed_words.append(line) for line in file]

        file.close()

        print(f'{len(parsed_words)} words read')
        return parsed_words

    def filter_list(self):
        #filter list by stripping
        self.words = [word.strip() for word in self.words]

    def random(self):
        """ returns random word from words, uses random.choice"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: find random words from dictionary
    , filters out new lines and comment lines"""

    def __init__(self, url):
        super().__init__(url)
        self.filter_list()
#make_word...
    def filter_list(self):
        #filter by stripping and removing #
        """filters out elements from words 
        list that start with # or are an empty string"""
        #in super().
        self.words = [word for word in self.words
                      if not (word == "" or word.startswith("#"))]

                      #return list
