import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
import json
import pickle
import numpy as np


word = []
classes = []
word_tags_wods = []
ignore_words = ["?", ":", "!", ".", ","]
train_data_file = open("intents.json").read()
intents = json.loads(train_data_file)
