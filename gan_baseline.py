'''
    Image GAN baseline model test
    Junho Shin, Dec.2021
    source 1 : https://wikidocs.net/86083
    source 2 : https://github.com/Dev93junho/Deep-Learning-Based-RobotArm-System

'''

# Import DL-library
import sklearn
from sklearn.datasets import load_files

from gensim.models.word2vec import Word2Vec
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.optim as optim
import torch.nn.functional as F

# Import Utils
import urllib.request
import re
import json

# Preprocess Korean
import nltk
from konlpy.tag import Kkma
kor_tagger = Kkma()


# Load Word2Vec
from gensim.models import word2vec


class brickillust(nn.Module):
    def __init__(self, text):
        self.text = text

        return text
    
    def word2vec(self):
        # Vectorize the words using Embedding
        train_data = 'a'
        word_set = ''
        pass
    
    def discriminate(self):
        pass
    
    def Generate_image(self):
        # Generate image
        pass
    
    



