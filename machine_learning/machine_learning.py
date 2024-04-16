import os

from sklearn.base import BaseEstimator

from machine_learning.data.data_cleaner import DataCleaner
from machine_learning.data.data_loader import DataLoader
from machine_learning.data.data_splitter import DataSplitter
from machine_learning.model.model_deployment import ModelDeployment
from machine_learning.model.model_evaluator import ModelEvaluator
from machine_learning.model.model_trainer import ModelTrainer
from machine_learning.model.model_validator import ModelValidator


def setup():
    os.makedirs(os.path.dirname('output/'), exist_ok=True)


class MachineLearning:

    def __init__(self,
                 filename,
                 cols_to_remove,
                 cols_to_transform,
                 cols_to_normalize,
                 model: BaseEstimator,
                 target_column,
                 train_ratio,
                 test_ratio,
                 validation_ratio,
                 seed
                 ):
        self.filename = filename
        self.cols_to_remove = cols_to_remove
        self.cols_to_transform = cols_to_transform
        self.cols_to_normalize = cols_to_normalize
        self.model = model
        self.target_column = target_column
        self.train_ratio = train_ratio
        self.test_ratio = test_ratio
        self.validation_ratio = validation_ratio
        self.seed = seed

    def run(self):
        setup()

        dataloader = DataLoader(self.filename)
        dataset = dataloader.get_dataset()

        data_cleaner = DataCleaner(dataset, self.cols_to_remove, self.cols_to_transform, self.cols_to_normalize)
        data_cleaner.clean_data()

        data_splitter = DataSplitter(data_cleaner.dataset, self.train_ratio, self.test_ratio, self.validation_ratio, self.seed)
        data_splitter.split_data()

        model_trainer = ModelTrainer(data_splitter.train_set, data_splitter.test_set, self.target_column, self.model)
        model_trainer.train()
        model_trainer.predict()

        model_evaluator = ModelEvaluator(model_trainer.test_set, model_trainer.Y_pred, self.target_column)
        model_evaluator.evaluate()

        model_validator = ModelValidator(data_splitter.validate_set, self.target_column, model_trainer.model)
        model_validator.validate()

        model_deployment = ModelDeployment(model_trainer.model)
        model_deployment.deploy()
