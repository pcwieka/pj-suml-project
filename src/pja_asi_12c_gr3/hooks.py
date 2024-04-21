from kedro.framework.hooks import hook_impl
import wandb


class ProjectHooks:

    @hook_impl
    def before_pipeline_run(self, run_params, pipeline, catalog):
        wandb.init(project='pja_asi_12c_gr3', config=run_params)
        wandb.config.update(run_params)
