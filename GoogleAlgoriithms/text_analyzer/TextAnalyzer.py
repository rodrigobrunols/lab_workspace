from collections import Counter
from typing import List


# from types import List
class TextAnalyzer:

    def __init__(self, text):
        self.text = text
        self.words = self.text.split()

    def word_count(self):
        return len(self.words)

    def char_count(self):
        return sum(1 for word in self.words for char in word)

    def most_common_word(self):
        # return a list in order from the most to least common
        return Counter(self.words).most_common()[0][0]

    def contains(self, word):
        return word in set(self.words)

    def topNFrequentyWords(self, n=3) -> List[str]:
        return [word for word, freq in Counter(self.words).most_common()[:n]]

    def longest_word(self) -> str:
        """Return the longest word in the text."""
        return max(self.words, key=len)
