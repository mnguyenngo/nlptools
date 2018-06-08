#!/usr/bin/env python3
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


import spacy
import pandas as pd

model = spacy.load('en')


def sentence_matrix(sentence):
    """Class object to represent sentences as a matrix to display nlp info

    Arguments:
        sentence (str)
    """
    doc = model(sentence)
    index, data = get_nlp_data(doc)
    mat = pd.DataFrame(data=data, index=index)
    return mat


def get_nlp_data(doc):
    """Parses doc and returns nlp data in a dict

    Arguments: doc (spaCy doc)
    Returns: token (list), data (dict)
    """
    token = [token for token in doc]
    dep = [token.dep_ for token in doc]
    lemma = [token.lemma_ for token in doc]
    is_stop = [token.is_stop for token in doc]
    is_alpha = [token.is_alpha for token in doc]
    shape = [token.shape_ for token in doc]
    tag = [token.tag_ for token in doc]

    nc = list(doc.noun_chunks)
    nc_flat = [token for chunk in nc for token in chunk]
    nc_bool = [token in nc_flat for token in doc]
    n_chunk = []
    for tok in token:
        if tok in nc_flat:
            for chunk in nc:
                if tok in chunk:
                    n_chunk.append(chunk)
        else:
            n_chunk.append(None)

    data = {
        'token': token,
        'dep': dep,
        'lemma': lemma,
        'is_stop': is_stop,
        'is_alpha': is_alpha,
        'shape': shape,
        'tag': tag,
        'nc_bool': nc_bool,
        'n_chunk': n_chunk
    }
    return token, data
