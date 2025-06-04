from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
import pandas as pd
from typing import Tuple


def train_polarity_model(df: pd.DataFrame, cv: int = 5) -> Tuple[Pipeline, float]:
    """Train a logistic regression model to predict polarity.

    Args:
        df: DataFrame with columns 'Title', 'Opinion' and 'Polarity'.
        cv: Number of folds for cross-validation.

    Returns:
        A fitted Pipeline and the mean cross-validation accuracy.
    """
    X = df['Title'] + ' ' + df['Opinion']
    y = df['Polarity']
    pipe = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    scores = cross_val_score(pipe, X, y, cv=cv, scoring='accuracy')
    pipe.fit(X, y)
    return pipe, scores.mean()


def train_attraction_model(df: pd.DataFrame, cv: int = 5) -> Tuple[Pipeline, float]:
    """Train a logistic regression model to predict attraction type.

    Args:
        df: DataFrame with columns 'Title', 'Opinion' and 'Attraction'.
        cv: Number of folds for cross-validation.

    Returns:
        A fitted Pipeline and the mean cross-validation accuracy.
    """
    X = df['Title'] + ' ' + df['Opinion']
    y = df['Attraction']
    pipe = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=1000))
    ])
    scores = cross_val_score(pipe, X, y, cv=cv, scoring='accuracy')
    pipe.fit(X, y)
    return pipe, scores.mean()
