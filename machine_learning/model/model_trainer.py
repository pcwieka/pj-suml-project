from sklearn.base import BaseEstimator


class ModelTrainer:

    def __init__(self, train_set, test_set, target_column, model: BaseEstimator):
        self.model = model
        self.train_set = train_set
        self.test_set = test_set
        self.target_column = target_column
        self.X_train = self.train_set.drop(self.target_column, axis=1)
        self.Y_train = self.train_set[self.target_column]
        self.X_test = self.test_set.drop(self.target_column, axis=1)
        self.Y_pred = None

    def train(self):
        self.model.fit(self.X_train, self.Y_train)

    def predict(self):
        self.Y_pred = self.model.predict(self.X_test)
