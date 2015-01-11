import up.plugin as base
from up.conf import Settings

settings = Settings()


class Deploy(base.UpPlugin):
    """
    $ up deploy alpha
    """
    name = 'deploy'
    description = 'Deploys project on remote stage(s)'

    def init(self):
        self.on(self.name, self.do_deploy)

    def argparse(self, subparsers):
        # Adds the "deploy" command
        p = subparsers.add_parser(self.name, help=self.description)
        p.add_argument('stages', type=str, metavar='stages',
                      #choices=settings.stages,
                       help='Stage(s) to deploy to')

    def do_deploy(self, context=None):
        stage = settings.get_stage()
        if stage in context.get('stages').split(','):
            self.trigger('deploy-init', context={'stage': stage})
            tpl_context = settings.get_context()
            project_root = tpl_context.get('project_root')
            self.run('git clone on %s' % project_root)
            self.trigger('deploy-done', context={'stage': stage})
