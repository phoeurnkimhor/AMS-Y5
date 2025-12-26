from sklearn.metrics import accuracy_score, f1_score

def evaluate_model(y_true, y_pred):
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'f1_score': f1_score(y_true, y_pred, zero_division=0)
    }

