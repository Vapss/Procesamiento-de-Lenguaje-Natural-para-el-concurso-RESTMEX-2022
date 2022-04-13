from Preprocesamiento.lematizador import lematizar
import os, pickle
import sys
import csv
import pandas as pd

def load_corpus(corpus):
	print("Lematizando {} lineas".format(len(corpus)))
	_corpus_lematizado = []
	
	for linea in corpus:
		_corpus_lematizado.append(lematizar(linea))

	return (_corpus_lematizado)

def read_csv_by_line(file_name):
	corpus = []
	with open(file_name, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		for row in reader:
			corpus.append(row[0])
	return (corpus)

class Corpus_Lematizado:
	def __init__(self):
		self.columnas = []
		self.corpus_lematizado = []

	def set_columnas(self, columnas):
		self.columnas = columnas

	def add_corpus(self, corpus):
		self.corpus_lematizado.append(corpus)

if __name__ == "__main__":
	corpus = ['¡Pésimo! No gastes tu dinero ahí malas condiciones, deplorable. Definitivamente no gastes tu dinero ahí, mejor ve a gastarlo en dulces en la tienda de La catrina.',
          'La mejor vista de Guanajuato. Es un mirador precioso y con la mejor vista de la ciudad de Guanajuato. El monumento es impresionante. Frente al monumento (por la parte de atrás del Pípila) hay una serie de locales en donde venden artesanías... si te gusta algo de ahí, cómpralo. A mí me pasó que vi algo y no lo compré pensando que lo vería más tarde en otro lado y no fue así. Te recomiendo que llegues hasta ahí en taxi, son MUY económicos, porque como está en un lugar muy alto, es muy cansado llegar caminando, aunque no está lejos del centro. PEROOOO... bájate caminando por los mini callejones. ¡Es algo precioso!Te lleva directamente por un lado del Teatro Juárez.'
	]

	if len(sys.argv) > 1:
		#Load lexicons
		if (os.path.exists('corpus_lematizado.pkl')):
			corpus_file = open ('corpus_lematizado.pkl','rb')
			corpus_lematizado = pickle.load(corpus_file)
		else:
			print ('no existe...')
			
			df = pd.read_excel(sys.argv[1])
			print(df.columns)
			
			#numer_of_columns = input("Cuantas columnas desea lematizar? [1-{}]".format(len(df.columns)))
			number_of_columns = 2
			res_cols = df.columns[0:int(number_of_columns)]

			#Se obtienen los datos para lematizar dependiendo de las columnas
			to_lematize_cols = []
			for i in range(len(res_cols)):
				to_lematize_cols.append(df[res_cols[i]].values.tolist())
			
			data = {}			
			#Se obtienen las columnas lematizadas
			for i in range(len(res_cols)):
				aux_corpus = load_corpus(to_lematize_cols[i])
				data[res_cols[i]] = aux_corpus


			#Se agregan las columnas restantes a data
			for i in range(len(df.columns)):
				if df.columns[i] not in res_cols:
					data[df.columns[i]] = df[df.columns[i]].values.tolist()

			#Se guarda el dataframe
			aux_df = pd.DataFrame(data, columns=df.columns)
			aux_df.to_excel('corpus_lematizado_dataframe.xlsx', index=False)
			
			corpus_file = open ('corpus_lematizado.pkl','wb')
			pickle.dump(aux_df, corpus_file)
			corpus_file.close()

			print ("Done")	
	else:
		print("Ingrese el .cvs pra lematizar")


