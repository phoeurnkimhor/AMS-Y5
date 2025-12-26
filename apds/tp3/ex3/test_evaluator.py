from evaluator import evaluate_model

def test_perfect_predictions():
    y_true = [1, 0, 1, 0]
    y_pred = [1, 0, 1, 0]  # perfect prediction
    result = evaluate_model(y_true, y_pred)
    assert result['accuracy'] == 1.0, "Accuracy should be 1.0 for perfect predictions"

def test_all_wrong_predictions():
    y_true = [1, 0, 1, 0]
    y_pred = [0, 1, 0, 1]  # all wrong
    result = evaluate_model(y_true, y_pred)
    assert result['f1_score'] == 0.0, "F1 score should be 0.0 when all predictions are wrong"

def test_output_contains_keys():
    y_true = [1, 0]
    y_pred = [1, 0]
    result = evaluate_model(y_true, y_pred)
    assert 'accuracy' in result, "Output should contain 'accuracy' key"
    assert 'f1_score' in result, "Output should contain 'f1_score' key"
