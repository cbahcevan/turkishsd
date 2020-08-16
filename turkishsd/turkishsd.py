from turkishsd.stemmers import MapStemmer
from turkishsd.deasciifier import deasciifySentence
import os
import pickle
from loguru import logger
import pkgutil
import pkg_resources


class TurkishStemmerDeasciifier:

    def __init__(self,negative_mode=False):

        logger.debug((os.path.dirname(os.path.dirname(__file__))))

        logger.debug(os.listdir(os.path.dirname(__file__)))


        if True:

            logger.debug("Loading from pkl file")
            


            #self.stemmer = pickle.loads(pkgutil.get_data(__package__, 'data/mapstemmer.pkl'))

            self.stemmer = MapStemmer(fromdump=True)
        
        else:

            logger.debug("Loading from static file")

            self.stemmer = MapStemmer(fromdump=False)
                

        self.stemmer.negative_mode = negative_mode

    
    
    def stemSentence(self,sentence):
        stemmed_sentence =  self.stemmer.stemSentence(sentence)
        if len(stemmed_sentence)  > 0 and stemmed_sentence[0] == " ":
            return stemmed_sentence[1:]
        return stemmed_sentence
    
    def deasciifySentence(self,sentence):

        sentence_deasciified =  deasciifySentence(sentence, self.stemmer)
        if len(sentence_deasciified)  >  0 and sentence_deasciified[0] == " ":
            return sentence_deasciified[1:]
        return sentence_deasciified
    
    def processWholeSentence(self,sentence):
        sentence_processed = self.deasciifySentence(sentence)
        stemmed_processed_sentence = self.stemmer.stemSentence(sentence_processed)
        return stemmed_processed_sentence

