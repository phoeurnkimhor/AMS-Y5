from ml import load_data, train_model, evaluate_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

def test_load_data_correctly():
    X, y = load_data()
    
    # Check non-empty
    assert not X.empty, "Features X are empty"
    assert not y.empty, "Target y is empty"
    
    # Check correct columns
    expected_columns = ['F1', 'F2', 'F3']
    assert list(X.columns) == expected_columns, f"Expected columns {expected_columns}, got {list(X.columns)}"
    
    # Check y has name 'target'
    assert y.name == 'target', f"Expected target column name 'target', got '{y.name}'"

def test_train_model_runs_without_error():
    X, y = make_classification(n_samples=10, n_features=3, n_informative=2, n_redundant=0, random_state=42)
    X = pd.DataFrame(X, columns=['A', 'B', 'C'])
    model = train_model(X, y)
    assert hasattr(model, "predict"), "Model was not trained correctly"

def test_evaluate_model_accuracy_between_0_and_1():
    y_true = [0, 1, 0, 1, 1]
    y_pred = [0, 1, 0, 0, 1]
    acc = evaluate_model(y_true, y_pred)
    assert 0 <= acc <= 1, "Accuracy not between 0 and 1"

def test_full_pipeline_accuracy():
    # Generate synthetic classification dataset
    X, y = make_classification(n_samples=50, n_features=4, n_informative=2, n_redundant=0, random_state=42)
    X = pd.DataFrame(X, columns=['F1', 'F2', 'F3', 'F4'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = evaluate_model(y_test, y_pred)
    
    assert 0 <= acc <= 1, "Full pipeline accuracy not between 0 and 1"