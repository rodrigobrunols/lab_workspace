import unittest
from TextAnalyzer import TextAnalyzer

class TestTextAnalyser(unittest.TestCase):

    def setUp(self):
        self.analyzer = TextAnalyzer("hello world hello again")

    def test_word_count(self):
        self.assertEqual(self.analyzer.word_count(), 4)

    def test_char_counter(self):
        self.assertEqual(self.analyzer.char_count(), 20)

    def test_most_common_word(self):
        self.assertEqual(self.analyzer.most_common_word(), "hello")

    def test_contains_word(self):
        self.assertTrue(self.analyzer.contains("again"))
        self.assertFalse(self.analyzer.contains("banana"))

    def testTopNFrequentyWords(self):
        result = self.analyzer.topNFrequentyWords()
        self.assertEqual(result, ['hello', 'world', 'again'])

    def testLongestWord(self):
        newAnalyzer = TextAnalyzer("Hello Rodrigo")
        # print(newAnalyzer.longest_word())
        self.assertEqual(newAnalyzer.longest_word(), "Rodrigo")
#
# if __name__ == '__main__':
#     unittest.main()
