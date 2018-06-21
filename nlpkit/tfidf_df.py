from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
import pandas as pd


def tfidf_df(s):
    """Returns a dataframe with tfidf weights with words as the index and
    sentences as the columns.

    Arguments:
        s (str)

    Returns
        df (dataframe)
    """
    model = spacy.load('en')
    doc = model(s)

    # Use spacy to parse the sentences from the string
    sent_list = [sent.text for sent in doc.sents]

    # initiate the vectorizor and run the tfidf calculation on the string input
    vectorizor = TfidfVectorizer()
    sparse_mat = vectorizor.fit_transform(sent_list)
    dense_mat = sparse_mat.todense()

    # get the words to use as the index of the dataframe
    feat_names = vectorizor.get_feature_names()
    df = pd.DataFrame(dense_mat.T, index=feat_names)

    return df
