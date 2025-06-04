import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models import train_polarity_model, train_attraction_model


def test_train_polarity_model_returns_score():
    df = pd.DataFrame({
        'Title': ['bueno', 'malo', 'excelente', 'pesimo'],
        'Opinion': ['me gusto', 'no me gusto', 'muy bueno', 'muy malo'],
        'Polarity': [5, 1, 5, 1],
        'Attraction': ['Hotel', 'Hotel', 'Restaurant', 'Restaurant']
    })
    model, score = train_polarity_model(df, cv=2)
    assert 0 <= score <= 1
    assert hasattr(model, 'predict')


def test_train_attraction_model_returns_score():
    df = pd.DataFrame({
        'Title': ['bueno', 'malo', 'excelente', 'pesimo'],
        'Opinion': ['me gusto', 'no me gusto', 'muy bueno', 'muy malo'],
        'Polarity': [5, 1, 5, 1],
        'Attraction': ['Hotel', 'Hotel', 'Restaurant', 'Restaurant']
    })
    model, score = train_attraction_model(df, cv=2)
    assert 0 <= score <= 1
    assert hasattr(model, 'predict')
