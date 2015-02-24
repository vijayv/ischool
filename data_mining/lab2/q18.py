import numpy as np
import pandas as pd

df = pd.read_csv("yelp_reviews.txt", delimiter="|")
by_business = df.groupby("business_id")["review_id"].count().reset_index()
merged = pd.merge(df, by_business, on="business_id")

merged = merged.groupby("user_id")["review_id_y"].median()

merged.to_csv("q18.feature")
