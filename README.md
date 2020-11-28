# Simple Turkish Stemmer and Deasciifier 

It is a simple corpus based Turkish stemmer and deasciifier. Generally, it tries to produce all letter(vowel, consonant) manipulation combinations of the word and search that candidates in the corpus.

- It works in Python3.6+
-  based on @akoksal lemmatizer project


## Installation

```
pip install git+https://github.com/cbahcevan/turkishsd.git
```

Installation for Ubuntu

```
git clone https://github.com/cbahcevan/turkishsd.git
cd turkishsd
sudo python3 setup.py install
```

Installation of Windows
```
git lfs clone https://github.com/cbahcevan/turkishsd.git
cd turkishsd
python3 setup.py install
```

## Usage Example

```
from turkishsd.turkishsd import TurkishStemmerDeasciifier

deasciifier = TurkishStemmerDeasciifier()

deasciifier.stemSentence("gözüm ağrıyor") # -> 'göz ağrı'

deasciifier.processWholeSentence("gozum agriyor") # ->  'göz ağrı'

deasciifier.deasciifySentence("gozum agriyor") # -> 'gözüm ağrıyor'

```

## Licence 

MIT
