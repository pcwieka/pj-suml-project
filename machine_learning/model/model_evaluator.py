from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import wandb
import matplotlib.pyplot as plt


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

        wandb.log({"Test Accuracy": accuracy})

        class_report_dict = classification_report(self.Y_test, self.Y_pred, output_dict=True)
        for metric, value in class_report_dict.items():
            if isinstance(value, dict):
                for sub_metric, sub_value in value.items():
                    wandb.log({f"Test Classification Report/{metric}/{sub_metric}": sub_value})
            else:
                wandb.log({f"Test Classification Report/{metric}": value})

        plt.figure(figsize=(8, 6))
        plt.imshow(conf_matrix, cmap='Blues', interpolation='nearest')
        plt.title('Test Confusion Matrix')
        plt.colorbar()
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.xticks(ticks=range(len(conf_matrix)), labels=range(len(conf_matrix)))
        plt.yticks(ticks=range(len(conf_matrix)), labels=range(len(conf_matrix)))
        wandb.log({"Test Confusion Matrix": wandb.Image(plt)})
        plt.close()
