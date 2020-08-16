import re


PAT_ALPHABETIC = re.compile(r'(((?![\d])\w)+)', re.UNICODE)


turkish_sign_operators = {
        "...": " ...",
        "!": " !",
        ",": " ,",
        "?": " ?",
        ":": " :",
        ";": "   ;",
        "-": " _",
        "\\": " \\",
        "@": ""
    }

def white_space_tokenize(sentence):
        if not isinstance(sentence, str) or len(sentence) < 1:
            assert False, "Input should be in string format"
        for operator in turkish_sign_operators:
            sentence = sentence.replace(operator, turkish_sign_operators[operator])
        sentence_splitted_form = sentence.split(" ")
        return sentence_splitted_form


def regex_tokenize(sentence):
        new_sentence_tokenized = []

        for element in PAT_ALPHABETIC.finditer(sentence):

            current_word = element.group()



            new_sentence_tokenized.append(current_word)

        return new_sentence_tokenized