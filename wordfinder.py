from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """takes in url, sets to self.url, initializes self.words"""
        self.words = self.filter_list(self.parse_file(path))

    def parse_file(self, path):
        """uses self.url for file path, opens file and reads 
        line by line, appending word to self.words"""
        file = open(path)
        parsed_words = []
        parsed_words = [line for line in file]

        file.close()

        print(f'{len(parsed_words)} words read')
        return parsed_words

    def filter_list(self, words):
        # filter list by stripping
        words = [word.strip() for word in words]
        return words

    def random(self):
        """ returns random word from words, uses random.choice"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: find random words from dictionary
    , filters out new lines and comment lines"""

    def filter_list(self, words):
        """filters out elements from words 
        list that start with # or are an empty string"""
        words = super().filter_list(words)
        words = [word for word in words if not (word == "" or word.startswith("#"))]
        return words
        