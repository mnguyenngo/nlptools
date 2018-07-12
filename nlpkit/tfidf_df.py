from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import stop_words
import spacy
import pandas as pd
from string import punctuation

nlp = spacy.load('en')


def spacy_tok(text, lemmatize=False):
    doc = nlp(text)
    if lemmatize:
        tokens = [tok.lemma_ for tok in doc]
    else:
        tokens = [tok.text for tok in doc]
    return tokens


def tfidf_df(s, lemmatize=False, remove_stopwords=False, remove_punct=False):
    """Returns a dataframe with tfidf weights with words as the index and
    sentences as the columns.

    Arguments:
        s (str)

    Returns
        df (dataframe)
    """
    # initiate stopwords
    if remove_stopwords:
        stopwords = set(stop_words.ENGLISH_STOP_WORDS)
    else:
        stopwords = set()
    # add punctuations to stopwords
    if remove_punct:
        stopwords.update(punctuation)

    # initiate spacy model
    doc = nlp(s)

    # Use spacy to parse the sentences from the string
    sent_list = [sent.text for sent in doc.sents]

    # initiate the vectorizor and run the tfidf calculation on the string input
    if lemmatize:
        vectorizor = TfidfVectorizer(stop_words=stopwords,
                                     tokenizer=lambda x: spacy_tok(x, True))
    else:
        vectorizor = TfidfVectorizer(stop_words=stopwords, tokenizer=spacy_tok)
    sparse_mat = vectorizor.fit_transform(sent_list)
    dense_mat = sparse_mat.todense()

    # get the words to use as the index of the dataframe
    feat_names = vectorizor.get_feature_names()
    df = pd.DataFrame(dense_mat.T, index=feat_names)

    return df
