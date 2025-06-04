import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import get_vectorized_dataframe_colums

def test_vectorization_returns_arrays():
    df = pd.DataFrame({'Title': ['buen hotel', 'malo'],
                       'Opinion': ['me gusto', 'no me gusto']})
    result = get_vectorized_dataframe_colums(df.copy(), ['Title'])
    value = result['Title'].iloc[0]
    assert isinstance(value, (int, np.integer))
