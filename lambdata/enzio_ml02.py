

# Make a function to create Matrix and Target pre validation split
import sklearn
from sklearn.model_selection import train_test_split
import pandas as pd

# How can I create a class that uses these functions?
# It seems like a need a MLProblemObject.
# that object has as attributes to Df's - X_Matrix and y_target
# so that would be given in the constructor


class ErgMLProblemObject():
    def __init__(self, df, target_string):
        """Explain what this is and how to use it.
        """
        self.original_df = df
        self.target = df[target_string]

    def create_xmatrix_ytarget(self):
        y_target = self.target
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


if __name__ == "__main__":
    df = pd.read_csv(
        "/Users/kellycho/Desktop/Repos/StarKells_Twitch_data/twitch_clean_data_Kelly02.csv")
    X_matrix, y_target = create_xmatrix_ytarget(df, "Total_Earnings")
    X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(
        X_matrix, y_target)
