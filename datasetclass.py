from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec
#from gensim.utils import simple_preprocess
from torch.utils.data import Dataset, DataLoader
import sqlite3
#from torchvision import transforms, utils
from gensim.utils import simple_preprocess
import torch


class FFUFUDUFUFUF(Dataset):
    def __init__(self):
        connect = sqlite3.connect('nlp.sqlite3')
        cursor = connect.cursor()
        self.mark = list(cursor.execute('SELECT НАЛИЧИЕ FROM linguist'))
        self.sent = []
        beyonder = []
        g = list(cursor.execute('SELECT КОНТЕКСТ FROM  linguist'))
        for i in g:
            for sentence in i:
                beyonder.append((simple_preprocess((sentence.replace('#', '')).replace('\xa0', ' '), deacc=True)))
        w2v_model = Word2Vec(beyonder, min_count=0, workers=cpu_count())
        for i in beyonder:
            for word in i:
                g = w2v_model.wv[word]
                self.sent.append(torch.tensor(g))
                break

    def __len__(self):
        return len(self.sent)

    def __getitem__(self, item: int):
        return [self.sent[item], self.mark[item]]


q = FFUFUDUFUFUF()
