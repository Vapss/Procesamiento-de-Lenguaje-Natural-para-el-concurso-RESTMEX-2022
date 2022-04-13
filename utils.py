from pyparsing import col
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing
import numpy as np

# Clases auxiliares


class validation_set:
    """
    Representación de un conjunto de datos validación

    Attributes:
        X_train: Conjunto de datos de entrenamiento
        y_train: target de entrenamiento
        X_test: Conjunto de datos de prueba
        y_test: target de prueba
    """

    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test


class test_set:
    """
    Representación de un conjunto de datos de prueba

    Attributes:
        X_test: Conjunto de datos
        y_test: target
    """

    def __init__(self, X_test, y_test):
        self.X_test = X_test
        self.y_test = y_test


class data_set:
    """
    Representación de un dataset

    Attributes:
        validation_set: Conjunto de datos de validación (X_train, y_train, X_test, y_test)
        test_set: Conjunto de datos de prueba (X_test, y_test)
    """

    def __init__(self, validation_set, test_set):
        self.validation_set = validation_set
        self.test_set = test_set


class folds_set:
    """
    Representación del algorimo KFold

    Attributes:
        n_fold: Número de pliegues
        data_set: Representación de un conjunto de datos
    """

    def __init__(self, n_fold, data_set):
        self.n_fold = n_fold
        self.data_set = data_set


def get_dataset_kfolds(corpus_validation_set, n_splits):
    """
    Función para obtener un dataset con los pliegues resultantes de utilizar el algorimot KFold

    Args:
        corpus_validation_set: contiene X_train, y_train, X_test y y_test
        n_splits: Número de pliegues para el algorimo KFold

    Return:
        fold_set:
            n_splits: Número de splits
            data_set: validation_set, test_set
    """
    validation_sets = []
    kf = KFold(n_splits=n_splits)
    print("n_splits:", n_splits)
    for train_index, test_index in kf.split(corpus_validation_set.X_train):
        X_train_, X_test_ = corpus_validation_set.X_train[
            train_index], corpus_validation_set.X_train[test_index]
        y_train_, y_test_ = corpus_validation_set.y_train[
            train_index], corpus_validation_set.y_train[test_index]
        validation_sets.append(validation_set(
            X_train_, y_train_, X_test_, y_test_))

    print("folds shape:")
    print(" X_train: ", validation_sets[0].X_train.shape)
    print(" y_train: ", validation_sets[0].y_train.shape)
    print(" X_test: ", validation_sets[0].X_test.shape)
    print(" y_test: ", validation_sets[0].y_test.shape)

    # Se guarda el conjunto de prueba
    my_test_set = test_set(corpus_validation_set.X_test,
                           corpus_validation_set.y_test)

    # Guarda el dataset con los pliegues del conjunto de validaciĆ³n y el conjunto de pruebas
    my_data_set = data_set(validation_sets, my_test_set)

    return folds_set(n_splits, my_data_set)


# Función para vectorizar el dataframe utilizando CountVectorizer
def get_vectorized_dataframe_colums(dataframe, col_names):

    for i in range(len(col_names)):
        vectorizador_binario = CountVectorizer(binary=True)
        aux = dataframe[col_names[i]].values
        res = vectorizador_binario.fit_transform(aux)
        dataframe[col_names[i]] = res.toarray()

    return dataframe
