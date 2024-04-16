from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


class ModelEvaluator:

    def __init__(self, test_set, Y_pred, target_column):
        self.Y_test = test_set[target_column]
        self.Y_pred = Y_pred

    def evaluate(self):
        accuracy = accuracy_score(self.Y_test, self.Y_pred)
        conf_matrix = confusion_matrix(self.Y_test, self.Y_pred)
        class_report = classification_report(self.Y_test, self.Y_pred)
        print("Evaluation results:")
        print(f"Accuracy: {accuracy}")
        print("Confusion Matrix:")
        print(conf_matrix)
        print("Classification Report:")
        print(class_report)
