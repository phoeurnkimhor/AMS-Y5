from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
import pandas as pd

def load_data():
    X, y = make_classification(
        n_samples=20, n_features=3, n_informative=2, n_redundant=0, random_state=42
    )
    X = pd.DataFrame(X, columns=['F1', 'F2', 'F3'])
    y = pd.Series(y, name='target')
    return X, y

def train_model(X, y):
    lr = LogisticRegression()
    return lr.fit(X, y)

def evaluate_model(y_true, y_pred):
    return accuracy_score(y_true, y_pred)


