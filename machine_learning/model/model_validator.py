from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import wandb
import matplotlib.pyplot as plt


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

        wandb.log({"Validation Accuracy": accuracy})

        plt.figure(figsize=(8, 6))
        plt.imshow(conf_matrix, cmap='Blues', interpolation='nearest')
        plt.title('Validation Confusion Matrix')
        plt.colorbar()
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.xticks(ticks=range(len(conf_matrix)), labels=range(len(conf_matrix)))
        plt.yticks(ticks=range(len(conf_matrix)), labels=range(len(conf_matrix)))
        wandb.log({"Validation Confusion Matrix": wandb.Image(plt)})
        plt.close()

        class_report_dict = classification_report(self.Y_validate, y_pred_validate, output_dict=True)
        for metric, value in class_report_dict.items():
            if isinstance(value, dict):
                for sub_metric, sub_value in value.items():
                    wandb.log({f"Validation Classification Report/{metric}/{sub_metric}": sub_value})
            else:
                wandb.log({f"Validation Classification Report/{metric}": value})
