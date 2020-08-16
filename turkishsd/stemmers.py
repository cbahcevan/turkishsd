import os
import re
from turkishsd.tokenizers import white_space_tokenize, regex_tokenize
import pickle
import pkgutil


class WordStructure:
        def __init__(self, word_content, word_lemma1, word_suffix, word_advanced_pos, word_no):
            self.word_no = word_no
            self.word_content = word_content
            self.word_lemma1 = word_lemma1
            self.word_suffix = word_suffix
            # self.word_advanced_pos = word_advanced_pos
            self.word_pos = word_advanced_pos

            self.is_it_uppercase = word_content[0:1].isupper()

        def __str__(self):
            return str(self.word_no) + " " + self.word_lemma1 + " " + self.word_pos

class MapStemmer:





    turkish_lower_map = {
    "İ":"i",
    "Ö":"ö",
    "Ü":"ü",
    "Ğ":"ğ",
    "I":"ı"
}

    def turkishLowerCase(self,text):
        for current_letter in self.turkish_lower_map:
            text = text.replace(current_letter, self.turkish_lower_map[current_letter])
        return text.lower()
    
    negative_suffixes = ["mıyor", "ma", "miyor", "madın", "mediniz", "medi","madım"]

    negative_mode = False

    zargan_word_stem_list = None
    suffix_list = set()

    word_lemma_dict_tr = {}

    reverse_word_lemma_dict_tr = {}

    def __init__(self,fromdump=True,tokenizer=""):

        self.word_frequency_statistics = {}

        if tokenizer == "regex":
            self.default_tokenizer_function = regex_tokenize
        else:
            self.default_tokenizer_function = white_space_tokenize


        if fromdump:
            
            this_dir, this_filename = os.path.split(__file__)  


            word_lemma_path = os.path.join(this_dir, 'data/word_lemma_dict_tr.pkl')
            word_reverse_lemma_path = os.path.join(this_dir, 'data/reverse_word_lemma_dict_tr.pkl')

            self.word_lemma_dict_tr = pickle.loads(pkgutil.get_data(__package__, 'data/word_lemma_dict_tr.pkl'))
            self.reverse_word_lemma_dict_tr = pickle.loads(pkgutil.get_data(__package__, 'data/reverse_word_lemma_dict_tr.pkl'))

        else:


            stem_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data/word_forms_stems_and_frequencies_full.txt")

        

            self.zargan_word_stem_list = open(stem_file_path, encoding="utf-8").read().split(
            "\n")[7:]

            for line in self.zargan_word_stem_list:

                line_splitted = line.split("\t")
                if len(line_splitted) > 2:
                    raw_word = line_splitted[0]
                    word_lemma = line_splitted[1]
                    word_suffix_status = line_splitted[2]

                    word_raw_suffix = raw_word[len(word_lemma):]
                    self.suffix_list.add(word_raw_suffix)

                    current_mirket_word = WordStructure(raw_word, word_lemma, word_raw_suffix, word_suffix_status, 0)

                    #my_inner_dict = {"word_lemma": word_lemma, word_suffix_status: word_suffix_status}

                    self.word_lemma_dict_tr[raw_word] = current_mirket_word

                    if word_lemma not in self.reverse_word_lemma_dict_tr:
                        self.reverse_word_lemma_dict_tr[word_lemma] = [raw_word]
                    else:
                        self.reverse_word_lemma_dict_tr[word_lemma].append(raw_word)





    def stemWord(self, word):


        word = self.turkishLowerCase(word)

        results = []
        if word in self.word_lemma_dict_tr:
            current_stem = self.word_lemma_dict_tr[word]
            current_suffix = word[len(current_stem.word_lemma1):]
            if current_suffix in self.negative_suffixes and self.negative_mode:
                current_stem.word_lemma1 = current_stem.word_lemma1 + "+NEG"
                results.append(current_stem)
            else:
                results.append(current_stem)

        for i in range(len(word) - 1, -1, -1):
            current_word = word[0:i]
            suffix_part = word[i:]
            if current_word in self.word_lemma_dict_tr and suffix_part in self.suffix_list:
                results.append(self.word_lemma_dict_tr[current_word])
                break
        if len(results) < 1:
            results.append(WordStructure(word, word, "unknown", "unknown", 0))
        return results

    def stemSentence(self, sentence,tokenizer_selected=""):
        result_sentence = ""
        if tokenizer_selected == "":
            tokenized_version = self.default_tokenizer_function(sentence)

        elif tokenizer_selected == "regexTokenize":
            #print("Regex tokenized")
            tokenized_version = regex_tokenize(sentence)
        else:
            tokenized_version = white_space_tokenize(sentence)
        

        for word in tokenized_version:
            result_sentence = result_sentence + self.stemWord(word)[0].word_lemma1 + " "

        return result_sentence[0:len(result_sentence) - 1]

    def contains(self, word):
        return word in self.word_lemma_dict_tr

    def suffixcontains(self, suffix_part):
        return suffix_part in self.suffix_list

    
    def to_pickle(self,filename):
        with open(filename,"wb") as filehandler:

            pickle.dump(self, filehandler,protocol=pickle.HIGHEST_PROTOCOL)
        
        with open("word_lemma_dict_tr.pkl","wb") as filehandler:
            pickle.dump(self.word_lemma_dict_tr, filehandler,protocol=pickle.HIGHEST_PROTOCOL)

        with open("reverse_word_lemma_dict_tr.pkl","wb") as filehandler:
            pickle.dump(self.reverse_word_lemma_dict_tr, filehandler,protocol=pickle.HIGHEST_PROTOCOL)


    
def checkInt(word):
    try:
        int(word)
        return True
    except:
        return False


def checkIntChar(word):
    for c in word:
        if checkInt(word):
            return True
    return False


if __name__ == '__main__':
    my_stemmer = MapStemmer()
    my_stemmer.to_pickle("mapstemmer.pkl")
    


