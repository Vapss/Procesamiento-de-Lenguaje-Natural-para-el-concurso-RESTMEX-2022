from Preprocesamiento.lematizador import lematizar
import os, pickle
import pandas as pd
def load_corpus(corpus):
    corpus_lematizado = []

    corpus = corpus.replace('(','').replace(')','')
    for linea in corpus.split():
        corpus_lematizado.append(lematizar(linea))
    #print(corpus_lematizado)
    return (corpus_lematizado)

if __name__ == "__main__":
    corpus = pd.read_excel('Rest_Mex_2022_Sentiment_Analysis_Track_Train.xlsx', index_col=None)
    corpus_lematizado = []

    #print(corpus)
    #load lexicons

    if (os.path.exists('corpus_lematizado.pkl')):
        corpus_file = open ('corpus_lematizado.pkl' , 'rb')
        corpus_lematizado = pickle.load(corpus_file)

    else:
        for linea in range(len(corpus)):
                corpus_lematizado.append(load_corpus(str(corpus.loc[linea]['Title'])+ ' ' + str(corpus.loc[linea]['Opinion'])))
                #print('--------------------------------------------')
                #print ('no existe...')
                corpus_file = open ('corpus_lematizado.pkl', 'wb')
                pickle.dump(corpus_lematizado, corpus_file)
                corpus_file.close()

        #print (corpus_lematizado)
        #print('--------------------------------------------')
        #print (corpus_lematizado)
