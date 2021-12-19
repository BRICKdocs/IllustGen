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

    def get_embedding(self, word):
        """
        Params:
            word (str)
        Return:
            Embedding (numpy.array)
        """
        return self.word_vectors[self.word_to_index[word]]

    def get_closet_to_vector(self, vector, n=1):
        """
        If you get 'vector', return the K-NN

        Params:
            vector (np.ndarray): SAME size with Annoy index
            n (int): return neighbors number
        Returns:
            [str, str, ....] : Nearest word with given Vector
            NOT Sorted word in order of distance
        """
        nn_indices = self.index.get_nns_by_vector(vector, n)
        return [self.index_to_word[neighbor] for in nn_indices]

    def compute_and_print_analogy(self, word1, word2, word3):
        vec1=self.get_embedding(word1)
        vec2=self.get_embedding(word2)
        vec3=self.get_embedding(word3)

        spatial_relationship = vec2 - vec1
        vec4 = vec3 + spatial_relationship

        closest_words=self.get_closest_to_vector(vec4, n=4)
        existing_words=set([word1,word2,word3])
        closest_words=[word for word in closest_words if word not in existing_words]

        if len(closest_words) == 0:
            print("Do not find Neareast neighbor")
            return
        for word4 in closest_words:
            print("{}:{}::{}:{}".format(word1,word2,word3,word4))


embeddings = \
    TextEmbeddings.from_embeddings_file('need to import train file')

class BrickGAN():
    def __init__(self):
        pass
    def WordEmbedding():
        pass
    def Discriminator():
        pass
    def Generator():
        pass