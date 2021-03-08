import numpy as np
import pandas as pd
import requests
import os
import sys
import tensorflow as tf
print("[LOAD]", tf.__version__)

import keras
np.random.seed(42)
import pickle
import json

with open("./genres_dict.pickle", "rb") as f:
    genres_dict = pickle.load(f)
    genres_dict_reverse = {i: g for g, i in genres_dict.items()}
    print("[LOAD] Genres dict loaded")

with open("./vocabs.pickle", "rb") as f:
    vocab, vocab_reverse = pickle.load(f)
    print("[LOAD] Vocabs loaded")

import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
print("[LOAD] nltk loaded")

def tokenize(line):
    return [lemmatizer.lemmatize(w) for w in nltk.word_tokenize(line.lower()) if w not in stopwords and w.isalnum()]

MODEL_URL = "http://localhost:8501/v1/models/functional_1/versions/1:predict"

def call_model(text, genre):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f">>>TESTING \n `{text}`\n\n")
    tokens = tokenize(text)
    print(">>> Tokenization is: ", tokens, "\n")
    sequence = [[1] + [vocab[w] for w in tokens if w in vocab] + [2]]
    print(">>> Sequence is: ", sequence, "\n")
    request_data = json.dumps({
        "signature_name": "serving_default",
        "instances": sequence
    })
    headers = {"content-type": "application/json"}
    json_response = requests.post(MODEL_URL, data=request_data, headers=headers)
    print(">>> JSON response is ", json_response.text, "\n")
    proba = json.loads(json_response.text)['predictions'][0]
    print(">>> Proba is: ", proba, "\n")
    predicted_genre = np.random.choice(len(proba), p=np.array(proba)/np.sum(proba))
    print(f">>> PREDICTED genre is :{genres_dict_reverse[predicted_genre]} ({predicted_genre})", "\n")
    print(f">>> TRUE genre is      :{genre}", "\n\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    


if __name__ == "__main__":
    print("[LOAD] Working in __main__ mode!")
    df = pd.read_csv("./test_data_solution.txt", sep=" ::: ", header=None, verbose=False)
    df.columns = ["index", "name", "genre", "desc"]
    print("[LOAD] test csv loaded")
    print(f"Tensorflow serving at {MODEL_URL}")
    print("====== LOADING FINISHED ======")
    while True:
        test_i = np.random.choice(range(len(df)))
        c = input("Hit ENTER to test TF model serving...")
        text = df.loc[test_i, "desc"]
        genre = df.loc[test_i, "genre"]
        call_model(text, genre)