from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import os, pickle

if not (os.path.exists('corpus_lematizado.pkl')):
	print ('no se ha generado el corpus lematizado')
else:
	corpus_file = open ('corpus_lematizado.pkl','rb')
	corpus_lematizado = pickle.load(corpus_file)
 
	corpuslower = [[word.lower() fpr word in text.split] for text in corpus_lematizado]

#~ list_stop_words = ['aunque', 'atrás', 'con', 'de', 'el']

# Representación vectorial binarizada
vectorizador_binario = CountVectorizer(binary=True)
#~ vectorizador_binario = CountVectorizer(binary=True, stop_words=list_stop_words)
X = vectorizador_binario.fit_transform(corpus_lematizado)
print (vectorizador_binario.get_feature_names_out())
print (X)#sparse matrix
print (type(X.toarray()))#dense ndarray
print ('Representación vectorial binarizada')
print (X.toarray())#dense ndarray

#Representación vectorial por frecuencia
vectorizador_frecuencia = CountVectorizer()
X = vectorizador_frecuencia.fit_transform(corpus_lematizado)
print('Representación vectorial por frecuencia')
print (X.toarray())

#~ #Representación vectorial tf-idf
vectorizador_tfidf = TfidfVectorizer()
X = vectorizador_tfidf.fit_transform(corpus_lematizado)
print ('Representación vectorial tf-idf')
print (X.toarray())

