import random

import const

class Generator(object):
    def __init__(self, data, title = "Hello, World", sentence = 1000, word = 100):
        self.data = data
        self.sentence = sentence
        self.title = title
        self.word = word

    def template_words(self, sentences):
        return [
            "        <p>" + sentence + "</p>\n" for sentence in sentences
        ]
    def template(self, title, sentences):
        return "".join([
            "<!DOCTYPE html>\n",
            "<html>\n",
            "    <head>\n",
            "        <meta charset=\"utf-8\">\n",
            "        <title>" + title + "</title>\n",
            "    </head>\n",
            "    <body>\n",
            *self.template_words(sentences),
            "    </body>\n",
            "</html>\n"
        ])
    def generate(self):
        __size = len(self.data)
        passage = []
        for __setence in range(self.sentence):
            sentence = "".join([
                self.data[random.randrange(__size)] + " "
                for __word in range(self.word)
            ])
            passage.append(sentence)
        return self.template(self.title, passage)
