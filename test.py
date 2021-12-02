'''
    Text-To-Image GAN model test file
    Junho Shin, Dec.2021
    source 1 : https://wikidocs.net/86083

'''

# import library
import sklearn
from sklearn.datasets import load_files

from gensim.models.word2vec import Word2Vec
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.optim as optim
import torch.nn.functional as F
import re
import json

import nltk
from konlpy.tag import Kkma
kor_tagger = Kkma()


class brickimage():
    def __init__(self, text):
        self.text = text

        return text
    
    def Embedding(self):
        # Vectorize the words using Embedding
        train_data = 'a'
        word_set = ''
        pass
    
    def Generate_image(self):
        # Generate image
        pass



