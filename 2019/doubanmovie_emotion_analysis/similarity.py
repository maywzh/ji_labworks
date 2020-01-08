import codecs
from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim import corpora, models
import numpy as np
import jieba

import sys

def get_dict(filepath):
    train = []
    fp = codecs.open(filepath, 'r', encoding='utf8')
    stopwords = ['的', '吗', '我', '会', '使用', '跟', '了', '有', '什么',
                 '这个', '下', '或者', '能', '要', '怎么', '呢', '吧', '都']
    for line in fp:
        line = list(jieba.cut(line))
        train.append([w for w in line if w not in stopwords])
    dictionary = Dictionary(train)
    return dictionary, train


def train_model():
    dictionary = get_dict()[0]
    train = get_dict()[1]
    corpus = [dictionary.doc2bow(text) for text in train]
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=7)
    lda.save('test_lda.model')


def lda_sim(s1, s2):
    lda = models.ldamodel.LdaModel.load('test_lda.model')
    test_doc = list(jieba.cut(s1))
    dictionary = get_dict()[0]
    doc_bow = dictionary.doc2bow(test_doc)
    doc_lda = lda[doc_bow]
    # print(doc_lda)
    list_doc1 = [i[1] for i in doc_lda]
    # print('list_doc1',list_doc1)

    test_doc2 = list(jieba.cut(s2))
    doc_bow2 = dictionary.doc2bow(test_doc2)
    doc_lda2 = lda[doc_bow2]
    # print(doc_lda2)
    list_doc2 = [i[1] for i in doc_lda2]
    # print('list_doc2',list_doc2)
    try:
        sim = np.dot(list_doc1, list_doc2) / \
            (np.linalg.norm(list_doc1) * np.linalg.norm(list_doc2))
    except ValueError:
        sim = 0
    # 得到文档之间的相似度，越大表示越相近
    return sim


if __name__ == "__main__":
    print(lda_sim(str(sys.argv[0]), str(sys.argv[1])))
