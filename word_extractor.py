from typing import Callable

import nltk
from nltk.stem import WordNetLemmatizer
import logging
from nltk.corpus import stopwords


class WordExtractor(Callable):
    def __init__(self):
        # 首次使用需要下载wordnet词典
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('stopwords')

        self.word_collection = dict()
        self.lemmatizer = WordNetLemmatizer()

        self.stop_words = set(stopwords.words('english'))

    def tokenize(self, sentence: str) -> list[str]:
        return nltk.word_tokenize(sentence)

    def is_stop_word(self, word: str):
        return word in self.stop_words

    def tag(self, tokens: list[str]) -> dict[str, list]:
        words = dict()
        tagged = nltk.pos_tag(tokens)
        words['nouns'] = [word for word, pos in tagged if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
        words['verbs'] = [word for word, pos in tagged if pos in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]
        words['adjs'] = [word for word, pos in tagged if pos in ['JJ', 'JJR', 'JJS']]
        words['advs'] = [word for word, pos in tagged if pos in ['RB', 'RBR', 'RBS']]
        words['pronouns'] = [word for word, pos in tagged if pos in ['PRP', 'PRP$', 'WP', 'WP$']]
        words['preps'] = [word for word, pos in tagged if pos in ['IN']]
        words['conjs'] = [word for word, pos in tagged if pos in ['CC']]
        words['articles'] = [word for word, pos in tagged if pos in ['DT']]
        words['interjections'] = [word for word, pos in tagged if pos in ['UH']]

        return words

    def lemmatize_a_word(self, word: str, tag: str):
        if tag == 'nouns':
            return self.lemmatizer.lemmatize(word, 'n')
        if tag == 'verbs':
            return self.lemmatizer.lemmatize(word, 'v')
        if tag == 'adjs':
            return self.lemmatizer.lemmatize(word, 'a')
        if tag == 'advs':
            return self.lemmatizer.lemmatize(word, 'r')

        return word

    def collect(self, words: dict[str, list]):
        for tag, word_list in words.items():
            if tag in (
                "interjections",
                "articles",
                "pronouns",
                "preps",
                "conjs"
            ):
                continue
            for word in word_list:
                if self.is_stop_word(word):
                    logging.debug(f"stop word: {word}")
                    continue

                word = self.lemmatize_a_word(word, tag)
                if word not in self.word_collection:
                    logging.debug(f"new word: {word}")
                self.word_collection[word] = self.word_collection.get(word, 0) + 1

    def __call__(self, sentence: str):
        tokens = self.tokenize(sentence)

        words = self.tag(tokens)

        self.collect(words)

    def get_word_collection(self):
        return self.word_collection
