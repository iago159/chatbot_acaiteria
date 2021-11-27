import spacy
import unidecode
import re

nlp = spacy.load("pt_core_news_md")


class Clean_text():

    def __init__(self, docs):
        self.docs = docs

    @property
    def docs(self):
        return self.__docs

    @docs.setter
    def docs(self, docs):
        if not isinstance(docs, list):
            docs = [docs]

        docs = self.strip_accent_punc_spaces(docs)
        docs = self.word_to_vec(docs)
        self.__docs = self.lemmatizer(docs)

    def strip_accent_punc_spaces(self, docs):
        new_docs = []
        for doc in docs:
            doc = re.sub(r'[^\w\s\d]+', '', doc.strip())
            doc = re.sub(r'\s{2,}', ' ', doc)
            doc = unidecode.unidecode(doc)
            new_docs.append(doc)
        return new_docs

    def word_to_vec(self, docs):
        words_vec = []
        [words_vec.append(nlp(word.lower())) for word in docs]
        return words_vec

    def lemmatizer(self, docs):
        new_docs = []
        for doc in docs:
            new_doc = nlp(" ".join([token.lemma_ for token in doc]))
            new_docs.append(new_doc)
        return new_docs
