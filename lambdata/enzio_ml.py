import pandas as pd

# Make a function to create Matrix and Target pre validation split


def create_xmatrix_ytarget(df, target_string):
    y_target = df[target_string]
    X_matrix = df.drop(target_string, axis=1)
    return (X_matrix, y_target)
