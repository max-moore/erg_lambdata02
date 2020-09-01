

# Make a function to create Matrix and Target pre validation split
import sklearn
# from sklearn.model_selection import train_test_split
import pandas as pd


def create_xmatrix_ytarget(df, target_string):
    y_target = df[target_string]
    X_matrix = df.drop(target_string, axis=1)
    return (X_matrix, y_target)


# 3 way split given X_matrix and y_target


def train_val_test_split(X_matrix, y_target):
    X_train_temp, X_test, y_train_temp, y_test = train_test_split(
        X_matrix, y_target, train_size=0.80, test_size=0.20,
        random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_temp, y_train_temp, train_size=0.80, test_size=0.20,
        random_state=42)

    return X_train, X_val, X_test, y_train, y_val, y_test
