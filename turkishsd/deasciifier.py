

turkish_entry_possible_deascii_map = {
        "i":"ı",
        "u":"ü",
        "g":"ğ",
        "o":"ö",
        "c":"ç",
        "s":"ş",
        "ı":"i"
    }

deascii_characters_for_turkish = list(turkish_entry_possible_deascii_map.keys())


    # Recursively generate all possible candidates
def generateCandidates(word,start_index):
        if len(word) == start_index :
            return []
        elif word[start_index] in turkish_entry_possible_deascii_map:

            word_manipulated = list(word)
            word_manipulated[start_index] = turkish_entry_possible_deascii_map[word[start_index]]
            word_manipulated = "".join(word_manipulated)

            return [word,word_manipulated] + generateCandidates(word,start_index + 1) + generateCandidates(word_manipulated,start_index + 1)

        return generateCandidates(word,start_index+1)


def generateCandidate(word):

        return generateCandidates(word,0)


def selectPossibleCandidate(candidates,stemmer):
    for candidate in candidates:
        if stemmer.contains(candidate):
            return candidate
    return ""
   
def deasciifySentence(sentence,stemmer):
    new_sentence = ""
    word_splitted = sentence.split(" ")
    for word in word_splitted:

            if stemmer.contains(word):
                new_sentence = new_sentence + " " + word
            else:
                possible_deascii_candidates =  generateCandidate(word)
                candidateSelected = selectPossibleCandidate(candidates=possible_deascii_candidates,stemmer=stemmer)
                if candidateSelected != "":
                        new_sentence = new_sentence + " " + candidateSelected
                else:
                        new_sentence = new_sentence + " " + word
    return new_sentence