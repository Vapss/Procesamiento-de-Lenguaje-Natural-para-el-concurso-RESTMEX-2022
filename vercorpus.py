# Ver el corpus

import pickle

corpus_file = open ('corpus_lematizado.pkl','rb')
corpus_lematizado = pickle.load(corpus_file)
 
print(corpus_lematizado)