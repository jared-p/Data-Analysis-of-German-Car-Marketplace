import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt

def load_and_process(path):
    df = (
        pd.read_csv(path)
        .pipe(lambda x: x.drop(x.loc[lambda row : row["gear"].isna()].index))
        .reset_index(drop = "true")
        .pipe(lambda x: x.drop(x.loc[lambda row : row["hp"].isna()].index))
        .reset_index(drop = "true")
        .pipe(lambda x: x.drop(x.loc[lambda row : row["make"] == "Others"].index))
        .reset_index(drop = "true")
        .assign(transmission = lambda x : x.gear)
        .drop("gear", axis = "columns")
        .reindex(columns = ["mileage", "make", "model", "fuel", "transmission", "offerType", "price", "hp", "year"])
        .pipe(lambda x: x.drop(x.loc[lambda row : row["fuel"] == "-/- (Fuel)"].index))
        .reset_index(drop = "true")
        .pipe(lambda x: x.drop(x.loc[lambda row : row["fuel"] == "Others"].index))
        .reset_index(drop = "true")
    )
    return df
