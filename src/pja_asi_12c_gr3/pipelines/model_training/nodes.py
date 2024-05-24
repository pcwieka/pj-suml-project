from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from pja_asi_12c_gr3.utils.wandb_metrics import WandbMetrics


def train_model(train_set, model_params):
    #model = RandomForestClassifier(n_estimators=model_params.get('n_estimators', 100), random_state=model_params.get('random_state', 42))
    model = LogisticRegression(max_iter=model_params.get('max_iter', 1000), random_state=model_params.get('random_state', 42))

    X_train = train_set.drop(columns=[model_params['target_column']])
    Y_train = train_set[model_params['target_column']]

    model.fit(X_train, Y_train)
    train_accuracy = model.score(X_train, Y_train)
    WandbMetrics.log(
        {"train_accuracy": train_accuracy,
         "n_estimators": model_params.get('n_estimators', 100),
         "random_state": model_params.get('random_state', 42)}
    )
    return model


def predict_model(test_set, model, model_params):
    X_test = test_set.drop(columns=[model_params['target_column']])
    Y_pred = model.predict(X_test)
    return Y_pred


def evaluate_model(test_set, Y_pred, model_params):
    Y_test = test_set[model_params['target_column']]
    eval_accuracy = accuracy_score(Y_test, Y_pred)
    eval_conf_matrix = confusion_matrix(Y_test, Y_pred)
    eval_class_report = classification_report(Y_test, Y_pred)
    WandbMetrics.log({"eval_accuracy": eval_accuracy})
    WandbMetrics.log_plot(eval_conf_matrix, 'Test Confusion Matrix', 'Predicted', 'True')
    return str(eval_accuracy), repr(eval_conf_matrix), eval_class_report


def validate_model(validate_set, model, model_params):
    X_validate = validate_set.drop(columns=[model_params['target_column']])
    Y_validate = validate_set[model_params['target_column']]
    Y_pred_validate = model.predict(X_validate)
    val_accuracy = accuracy_score(Y_validate, Y_pred_validate)
    val_conf_matrix = confusion_matrix(Y_validate, Y_pred_validate)
    val_class_report = classification_report(Y_validate, Y_pred_validate)
    WandbMetrics.log({"val_accuracy": val_accuracy})
    WandbMetrics.log_plot(val_conf_matrix, 'Validation Confusion Matrix', 'Predicted', 'True')
    return str(val_accuracy), repr(val_conf_matrix), val_class_report
