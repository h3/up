from fabric.api import env, sudo, run

from up import log
from up.utils import import_class
from up.conf import settings

env.use_ssh_config = True

CORE_PLUGINS = [
    'up.contrib.deploy.plugin',
    'up.contrib.virtualenv.plugin',
    'up.contrib.uwsgi.plugin',
    'up.contrib.nginx.plugin',
]


def load_plugins(subparsers):

    for plugin in CORE_PLUGINS:
        try:
            hook = import_class('%s.Hook' % plugin)(subparsers)
        except ImportError:
            log.error('Could not load plugin: %s', plugin)


class BaseHook(object):
    name = 'untitled'
    on_stages = True
    automap_args = False
    command = None

    def __init__(self, subparsers):
        self.parser = subparsers.add_parser(self.name)

        if self.on_stages:
            self.parser.add_argument('on', **settings.STAGES_KWARGS)

        if self.automap_args:
            name = self.name
            commands = self.commands

            for cmd in commands:
                self.parser.add_argument('--%s' % cmd, action='store_true')

            def factory(args):
                self.args = args
                command = self.command
                for cmd in commands:
                    if getattr(args, cmd.replace('-', '_')):
                        for stagename in self.args.on:
                            stage = settings.get_stage_by_name(stagename)
                            env.host_string = stage.get('host')
                            plugins = [
                                plugin for plugin in stage.get('plugins')
                                if plugin.get('name') == name
                            ]
                            if plugins:
                                command = plugins[0].get('command', command)
                            if command:
                                sudo(command % cmd)

            self.parser.set_defaults(func=factory)

    def run(self, *args, **kwargs):
        """
        Runs fabric's "run" on all stages
        """
        for stagename in self.args.on:
            stage = settings.get_stage_by_name(stagename)
            env.host_string = stage.get('host')
            run(*args, **kwargs)

    def sudo(self, *args, **kwargs):
        """
        Runs fabric's "sudo" on all stages
        """
        for stagename in self.args.on:
            stage = settings.get_stage_by_name(stagename)
            env.host_string = stage.get('host')
            sudo(*args, **kwargs)
