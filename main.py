from traceback import print_tb
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from utils import *

import numpy as np
import pandas as pd
import os
import pickle


# Se recupera el corpus guardado en pickle
if not (os.path.exists('corpus_lematizado.pkl')):
    print('no se ha generado el corpus lematizado')
else:
    corpus_file = open('corpus_lematizado.pkl', 'rb')
    corpus_lematizado = pickle.load(corpus_file)


# Ya que se almaceno en forma de dataframe, se carga
corpus_lematizado = pd.read_pickle('corpus_lematizado.pkl')

# Se obtienn las columnas 'Title' y 'Opinion' vectorizadas
get_vectorized_dataframe_colums(corpus_lematizado, ['Title', 'Opinion'])

corpus_lematizado.loc[corpus_lematizado["Attraction"]
                      == "Hotel", "Attraction"] = 1
corpus_lematizado.loc[corpus_lematizado["Attraction"]
                      == "Restaurant", "Attraction"] = 2
corpus_lematizado.loc[corpus_lematizado["Attraction"]
                      == "Attraction", "Attraction"] = 3

X = corpus_lematizado.drop(['Polarity', 'Attraction'], axis=1).values
y_polarity = corpus_lematizado['Polarity'].values
y_attraction = corpus_lematizado['Attraction'].values

# Datos para el modelo de regresión logística que predice la polaridad
X_train_polarity, X_test_polarity, y_train_polarity, y_test_polarity = train_test_split(
    X, y_polarity, test_size=0.2, random_state=0)


# Datos para el modelo de regresión logística que predice la atracción
X_train_attraction, X_test_attraction, y_train_attraction, y_test_attraction = train_test_split(
    X, y_attraction, test_size=0.2, random_state=0)

# Se almacenan los datos en validation set
polarity_dataset_validation_set = validation_set(
    X_train_polarity, y_train_polarity, X_test_polarity, y_test_polarity)
attraction_dataset_validation_set = validation_set(
    X_train_attraction, y_train_attraction, X_test_attraction, y_test_attraction)

# Se obtienen los pliegues
polarity_dataset_kfold = get_dataset_kfolds(
    polarity_dataset_validation_set, 10)
attraction_dataset_kfold = get_dataset_kfolds(
    attraction_dataset_validation_set, 10)


accuracy = []
precision = []
recall = []
f1 = []

# Se recorren los pliegues
for i in range(polarity_dataset_kfold.n_fold):
    # Para cada pliegue se obtiene X_train, X_test, y_train, y_test
    _X_train = polarity_dataset_kfold.data_set.validation_set[i].X_train
    _y_train = polarity_dataset_kfold.data_set.validation_set[i].y_train
    _X_test = polarity_dataset_kfold.data_set.validation_set[i].X_test
    _y_test = polarity_dataset_kfold.data_set.validation_set[i].y_test

    clf = LogisticRegression(
        solver='saga', penalty="l1", max_iter=100000000)
    clf.fit(_X_train, _y_train)
    y_pred = clf.predict(_X_test)
    acc = accuracy_score(_y_test, y_pred)
    # pre = precision_score(_y_test, y_pred)
    # rec = recall_score(_y_test, y_pred)
    # f1s = f1_score(_y_test, y_pred)
    print(acc)
    accuracy.append(acc)
    # precision.append(pre)
    # recall.append(rec)
    # f1.append(f1s)
    # print('Clase real{}\nClase predicha{}'.format(
    #     _y_test[0:10], y_pred[0:10]))

accuray_prom = np.sum(accuracy) / len(accuracy)
precision_prom = np.sum(precision) / len(precision)
recall_prom = np.sum(recall) / len(recall)
f1_prom = np.sum(f1) / len(f1)
print("Accuracy promedio: {}".format(accuray_prom))
print("Precision promedio: {}".format(precision_prom))
print("Recall promedio: {}".format(recall_prom))
print("F1 promedio: {}".format(f1_prom))
