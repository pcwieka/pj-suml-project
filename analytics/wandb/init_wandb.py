import wandb


def init_wandb():
    try:
        wandb.init(project='pja_asi_12c_gr3')
    except wandb.errors.AuthenticationError as e:
        print(e)
        wandb.login()