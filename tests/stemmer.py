import unittest
import sys
import os
print(os.getcwd())


from turkishstemmerdeasciifier import stemmers

print(stemmers.stemmer.stemSentence("gözüm ağrıyor"))