import pandas as pd
from models import train_polarity_model, train_attraction_model

if __name__ == "__main__":
    df = pd.read_excel('Rest_Mex_2022_Sentiment_Analysis_Track_Train.xlsx')
    polarity_model, polarity_acc = train_polarity_model(df)
    attraction_model, attraction_acc = train_attraction_model(df)
    print(f"Polarity accuracy: {polarity_acc:.3f}")
    print(f"Attraction accuracy: {attraction_acc:.3f}")
