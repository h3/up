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
        if settings.get_stage() in context.get('stages').split(','):
            self.remote('git clone on %s' % settings.context.get('current').get('stage'))
            self.trigger('deploy-done')



#from fabric.api import *
#
#from up import log
#from up.conf import settings
#from up.plugin import BaseHook
#
#
#class Hook(BaseHook):
#    name = 'deploy'
#
#    def __init__(self, subparsers):
#        super(Hook, self).__init__(subparsers)
#
#        self.parser.add_argument('--syncdb', action='store_true')
#        self.parser.set_defaults(func=self._deploy)
#
#    def _deploy(self, args):
#        log.info("Executing %s on %s" % (
#            self.name,
#            ', '.join(args.on),
#        ))
#
#        for stagename in args.on:
#            stage = settings.get_stage_by_name(stagename)
#            env.host_string = stage.get('host')
#            run("uptime")
