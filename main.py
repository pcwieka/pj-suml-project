import wandb
from sklearn.ensemble import RandomForestClassifier
from analytics.wandb.init_wandb import init_wandb
from helpers.parse_args import parse_args
from machine_learning.machine_learning import MachineLearning


class Main:

    def __init__(self):
        self.name = "PJA_ASI_12c_GR3"
        self.args = parse_args()
        print(f'Application arguments: {self.args}')
        self.filename = self.args.filename
        self.train_ratio = self.args.train_ratio
        self.test_ratio = self.args.test_ratio
        self.validation_ratio = self.args.validation_ratio
        self.seed = self.args.seed

    def run(self):
        print("Running: ", self.name)



        cols_to_remove = []
        cols_to_transform = {
            "family_history_with_overweight": {"yes": 1, "no": 0},
            "Gender": {"Male": 0, "Female": 1},
            "FAVC": {"yes": 1, "no": 0},
            "SMOKE": {"yes": 1, "no": 0},
            "SCC": {"yes": 1, "no": 0},
            "CAEC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3},
            "CALC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3},
            "MTRANS": {"Public_Transportation": 0, "Walking": 1, "Automobile": 2, "Motorbike": 3, "Bike": 4}
        }
        cols_to_normalize = ["Age", "Height", "Weight", "FCVC", "NCP", "CH2O", "FAF", "TUE"]
        target_column = 'NObeyesdad'

        model = RandomForestClassifier(random_state=42)

        machine_learning = MachineLearning(
            self.filename,
            cols_to_remove,
            cols_to_transform,
            cols_to_normalize,
            model,
            target_column,
            self.train_ratio,
            self.test_ratio,
            self.validation_ratio,
            self.seed
        )



        machine_learning.run()


if __name__ == "__main__":
    init_wandb()
    app = Main()
    app.run()