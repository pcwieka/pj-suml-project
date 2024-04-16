from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


class ModelValidator:

    def __init__(self, validate_set, target_column, model: BaseEstimator):
        self.model = model
        self.X_validate = validate_set.drop(target_column, axis=1)
        self.Y_validate = validate_set[target_column]

    def validate(self):
        y_pred_validate = self.model.predict(self.X_validate)
        accuracy = accuracy_score(self.Y_validate, y_pred_validate)
        conf_matrix = confusion_matrix(self.Y_validate, y_pred_validate)
        class_report = classification_report(self.Y_validate, y_pred_validate)
        print("Validation results:")
        print(f"Accuracy: {accuracy}")
        print("Confusion Matrix:")
        print(conf_matrix)
        print("Classification Report:")
        print(class_report)
