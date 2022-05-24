import sqlite3
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec
from gensim.utils import simple_preprocess


def vectorize_new():
    connect = sqlite3.connect('nlp.sqlite3')
    cursor = connect.cursor()
    data = list(cursor.execute('SELECT КОНТЕКСТ FROM linguist'))
    tokenized = []
    for i in data:
        for g in i:
            tokenized.append(simple_preprocess(g.replace('\xa0', ' '), deacc=True))
    w2v_model = Word2Vec(tokenized, min_count=0, workers=cpu_count())
    vectorized = []
    for i in tokenized:
        for g in i:
            vectorized.append(w2v_model.wv[g])
