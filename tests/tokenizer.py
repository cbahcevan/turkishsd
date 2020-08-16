import unittest
from turkishstemmerdeasciifier import tokenizers

class TokenizerTest(unittest.TestCase):
    def whitespace_basic_test(self):

        sentence = "deneme 1 2 3. a"
        sentence_tokenized = tokenizers.white_space_tokenize(sentence)

        expected_output = ["deneme","1","2","3.","a"]

        self.assertEqual(sentence_tokenized,expected_output)
    
    def regex_tokenizer_test(self):
        pass


unittest.main()
