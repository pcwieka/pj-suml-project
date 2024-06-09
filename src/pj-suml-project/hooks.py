from kedro.framework.hooks import hook_impl
import wandb


class ProjectHooks:

    @hook_impl
    def before_pipeline_run(self, run_params, pipeline, catalog):
        wandb.init(project='pj-suml-project', config=run_params)
        wandb.config.update(run_params)
