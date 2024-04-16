import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Process the dataset for ML model training")
    parser.add_argument('--filename', type=str, default='ObesityDataSet.csv', help='Filename of the dataset')
    parser.add_argument('--train_ratio', type=float, default=0.8, help='Training set ratio')
    parser.add_argument('--test_ratio', type=float, default=0.15, help='Test set ratio')
    parser.add_argument('--validation_ratio', type=float, default=0.05, help='Validation set ratio')
    parser.add_argument('--seed', type=int, default=50, help='Seed for random operations')
    # add more arguments as needed
    # parser.add_argument('--model_type', type=str, default='linear', help='Type of model to train')
    # parser.add_argument('--learning_rate', type=float, default=0.01, help='Learning rate for the optimizer')

    args = parser.parse_args()
    return args
