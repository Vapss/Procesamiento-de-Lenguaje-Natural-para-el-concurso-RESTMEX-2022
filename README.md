# RESTMEX 2022 NLP Project

This repository contains a collection of scripts used for experimenting with Spanish text preprocessing and sentiment analysis for the RESTMEX 2022 competition.

## Setup

1. Install Python 3.8 or newer.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install FreeLing and its Python bindings if you plan to use the lemmatization utilities.

## Usage

The typical workflow is:

1. **Generate the lemmatized corpus**
   ```bash
   python preprocesamiento_lematizador.py
   ```
   This reads the training spreadsheet and stores a pickled file named `corpus_lematizado.pkl`.

2. **Train the models**
   ```bash
   python main.py
   ```
   The script vectorizes the text columns and trains logistic regression models to predict polarity and attraction.

   Alternatively you can import the utilities in `models.py` to train
   cross‑validated TF‑IDF logistic regression models:

   ```python
   from models import train_polarity_model, train_attraction_model
   ```

Datasets are expected in the `data/` directory. Large data files and pickles should not be committed to the repository.

## Testing

Unit tests can be executed with:

```bash
pytest
```

A GitHub Actions workflow is provided in `.github/workflows/python-tests.yml` to run these tests automatically.

## License

See the `LICENSE` file for licensing information.
