from autogluon.tabular import TabularPredictor
from sklearn.metrics import confusion_matrix, classification_report


def train_autogluon_model(train_set, model_params):
    predictor = TabularPredictor(label=model_params['target_column']).fit(train_set)
    return predictor


def evaluate_autogluon_model(test_set, trained_model, model_params):
    X_test = test_set.drop(columns=[model_params['target_column']])
    y_test = test_set[model_params['target_column']]

    evaluation_metrics = trained_model.evaluate(test_set)

    predictions = trained_model.predict(X_test)

    conf_matrix = confusion_matrix(y_test, predictions)
    class_report = classification_report(y_test, predictions)

    return str(evaluation_metrics['accuracy']), str(conf_matrix), class_report


def validate_autogluon_model(validate_set, trained_model, model_params):
    X_validate = validate_set.drop(columns=[model_params['target_column']])
    y_validate = validate_set[model_params['target_column']]

    evaluation_metrics = trained_model.evaluate(validate_set)

    predictions = trained_model.predict(X_validate)

    conf_matrix = confusion_matrix(y_validate, predictions)
    class_report = classification_report(y_validate, predictions)

    return str(evaluation_metrics['accuracy']), str(conf_matrix), class_report
