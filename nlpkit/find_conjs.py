#!/usr/bin/env python3
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


def find_conjs(doc, context=None):
    """Returns a dictionary with a list of the conjunctions found in a sentence

    Arguments:
        doc (spaCy doc object)
        context (str): name of source document for future reference
            example: "Washington 2015 Building Code"

    Returns:
        conj_dict_list (dict)
            objects (list): list of objects found in doc that are part of a
                            conj
            context (str)
    """
    conjs = [token for token in doc if token.dep_ is 'conj']
    conj_chunk = []
    conj_chunk_flat = set()
    for conj in conjs:
        ancestors = list(conj.ancestors)
        objs = [token for token in ancestors
                if token.dep_ in ['pobj', 'nsubj']]
        if len(objs) > 0:
            for obj in objs:
                if obj in conj_chunk_flat:
                    for chunk in conj_chunk:
                        if obj.lemma_ in chunk:
                            chunk.append(conj.lemma_)
                else:
                    conj_chunk.append([obj.lemma_, conj.lemma_])
                conj_chunk_flat.add(obj)
                conj_chunk_flat.add(conj)
    conj_dict_list = []
    for conj in conj_chunk:
        conj_dict = dict()
        conj_dict['objects'] = conj
        if context is not None:
            conj_dict['context'] = context
        conj_dict_list.append(conj_dict)
    return conj_dict_list
