import up.plugin as base
from up.conf import settings


class Deploy(base.UpPlugin):
    """
    $ up deploy alpha
    """
    name = 'deploy'
    description = 'Deploys project on remote stage(s)'

    def init(self):
        self.on(self.name, self.run)

    def argparse(self, subparsers):
        # Adds the "deploy" command
        p = subparsers.add_parser(self.name, help=self.description)
        p.add_argument('stages', type=str, metavar='stages',
                      #choices=settings.stages,
                       help='Stage(s) to deploy to')

    def run(self, context=None):
        stage = settings.get_stage()
        if stage in context.get('stages').split(','):
            context = settings.get_context()
            stage_context = context.get('stages').get(stage)
            project_root = stage_context.get('project_root')
            self.remote('git clone on %s' % project_root)
            self.trigger('deploy-done')
