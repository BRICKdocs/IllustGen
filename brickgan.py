"""
BrickGAN init

Author : Junho Shin
Source: NLP with Pytorch
"""

import numpy as np
from annoy import AnnoyIndex # import k-Neighborhood Nearest algorithm

#Embedding Text
class TextEmbeddings(object):
    def __init__(self, word_to_index, word_vectors):
        """
        Describe params

        PARAMS:
            word_to_index (dict): mapping word to int
            word_vectors (numpy array)
        """
        self.word_to_index = word_to_index
        self.word_vectors = word_vectors
        self.index_to_word = \
            {v: k for k, v in self.word_to_index()}
        self.index = AnnoyIndex(len(word_vectors[0]),
                                metric='euclidean')
        for _, i in self.word_to_index.items():
            self.index.add_item(i, self.word_vectors[i])
        self.index.build(50)
    @classmethod
    def from_embeddings_file(cls, embedding_file):
        """
        create object from pretrained vector

        Params:
            embedding_file (str): file locale
        Returns:
            TextEmbedding's Instance
        """
        word_to_index ={}
        word_vectors=[]
        with open(embedding_file) as fp:
            for line in fp.readlines():
                line=line.split("")
                word=line[0]
                vec=np.array([float(x) for x in line[1:]])
                word_to_index[word] = len(word_to_index)
                word_vectors.append(vec)
            return cls(word_to_index, word_vectors)

class BrickGAN():
    def __init__(self):
        pass
    def WordEmbedding():
        pass
    def Discriminator():
        pass
    def Generator():
        pass