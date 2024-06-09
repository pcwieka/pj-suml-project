from matplotlib import pyplot as plt
import wandb


class WandbMetrics:

    @staticmethod
    def log(data):
        wandb.log(data)

    @staticmethod
    def log_plot(array, title: str, x_label: str, y_label: str) -> None:
        plt.figure(figsize=(8, 6))
        plt.imshow(array, cmap='Blues', interpolation='nearest')
        plt.title(title)
        plt.colorbar()
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(ticks=range(len(array)), labels=range(len(array)))
        plt.yticks(ticks=range(len(array)), labels=range(len(array)))
        wandb.log({title: wandb.Image(plt)})
        plt.close()
