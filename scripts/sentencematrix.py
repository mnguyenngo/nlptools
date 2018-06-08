#!/usr/bin/env python3
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


import spacy
import pandas as pd


class SentenceMatrix(object):
    """Class object to represent sentences as a matrix to display nlp info

    Arguments:
        sentence (str)
    """
    def __init__(self, sentence, model_name=None):
        if model_name is not None:
            self.nlp = spacy.load(model_name)
        else:
            self.nlp = spacy.load('en')
        self.sentence = sentence
        self.doc = self.nlp(sentence)

    def matrix(self):
        index, data = self.get_nlp_data()
        mat = pd.DataFrame(data=data, index=index)
        return mat

    def get_nlp_data(self):
        token = [token for token in self.doc]
        dep = [token.dep_ for token in self.doc]
        lemma = [token.lemma_ for token in self.doc]
        is_stop = [token.is_stop for token in self.doc]
        is_alpha = [token.is_alpha for token in self.doc]
        shape = [token.shape_ for token in self.doc]
        tag = [token.tag_ for token in self.doc]

        nc = list(self.doc.noun_chunks)
        nc_flat = [token for chunk in nc for token in chunk]
        nc_bool = [token in nc_flat for token in self.doc]
        data = {
            'token': token,
            'dep': dep,
            'lemma': lemma,
            'nc_bool': nc_bool,
            'is_stop': is_stop,
            'is_alpha': is_alpha,
            'shape': shape
        }
        return token, data
