from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def train_model(train_set, model_params):
    """

    Args:
        train_set: train set
        model_params: model parameters

    Returns: trained model

    """
    model = RandomForestClassifier(n_estimators=model_params.get('n_estimators', 100), random_state=model_params.get('random_state', 42))

    x_train = train_set.drop(columns=[model_params['target_column']])
    y_train = train_set[model_params['target_column']]

    model.fit(x_train, y_train)
    train_accuracy = model.score(x_train, y_train)
    print(f"Train accuracy: {train_accuracy}")

    return model


def predict_model(test_set, model, model_params):
    """

    Args:
        test_set: test set
        model: model
        model_params: model parameters

    Returns: predictions

    """
    x_test = test_set.drop(columns=[model_params['target_column']])
    y_pred = model.predict(x_test)
    return y_pred


def evaluate_model(test_set, y_pred, model_params):
    """

    Args:
        test_set: test set
        y_pred: predictions
        model_params: model parameters

    Returns: evaluation metrics

    """
    y_test = test_set[model_params['target_column']]
    eval_accuracy = accuracy_score(y_test, y_pred)
    print(f"Evaluation accuracy: {eval_accuracy}")
    eval_conf_matrix = confusion_matrix(y_test, y_pred)
    eval_class_report = classification_report(y_test, y_pred)
    return str(eval_accuracy), repr(eval_conf_matrix), eval_class_report


def validate_model(validate_set, model, model_params):
    """

    Args:
        validate_set: validation set
        model: model
        model_params: model parameters

    Returns: validation metrics

    """
    x_validate = validate_set.drop(columns=[model_params['target_column']])
    y_validate = validate_set[model_params['target_column']]
    y_pred_validate = model.predict(x_validate)
    val_accuracy = accuracy_score(y_validate, y_pred_validate)
    print(f"Validation accuracy: {val_accuracy}")
    val_conf_matrix = confusion_matrix(y_validate, y_pred_validate)
    val_class_report = classification_report(y_validate, y_pred_validate)
    return str(val_accuracy), repr(val_conf_matrix), val_class_report
