'''
    Text-to-Image GAN baseline model 
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
from torch.nn.modules.activation import LeakyReLU
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

# GPU import
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# DataLoader
'''
Please import  DataLoader source code
'''

# Vectorlize Docs    
def docs2vec(self):
    # Vectorize the words using Embedding
    train_data = 'a'
    word_set = ''
    pass
# Generator : input random vector z, output fake 
class Generator(nn.Module):
    # Network Layer
    def __init__(self):
        super(Generator, self).__init__()
        self.main= nn.Sequential(
            nn.Linear(in_features=100, out_features=256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(in_features=256, out_features=512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(in_features=512, out_features=1024),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(in_features=1024, out_features=28*28),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Tanh()
        )
        
    def forward(self, inputs):
        return self.main(inputs).view(-1, 1, 28, 28)
    
# Discriminator : input fake from Generator, discriminate data state like real or fake
class Discriminator(nn.Module):
    # Network Layer
    def __init__(self):
        super(Discriminator, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(in_features=28*28, out_features=1024),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(inplace=True),
            nn.Linear(in_features=1024, out_features=512),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(inplace=True),
            nn.Linear(in_features=512, out_features=256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(inplace=True),
            nn.Linear(in_features=256, out_features=1),
            nn.Sigmoid()            
        )
    def forward(self, inputs):
        inputs=inputs.view(-1, 28*28)
        return self.main(inputs)


# initialize brickillust
class brickillust(nn.Module):
    def __init__(self, text):
        self.text = text

        return text
    pass
    

    
    



