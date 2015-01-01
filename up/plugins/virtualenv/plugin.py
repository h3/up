from yapsy.IPlugin import IPlugin
from up.events import Event


class Virtualenv(IPlugin, Event):
    name = 'test'
    description = 'Virtualenv'

#   def argparse(self, subparsers):
#       subparsers.add_parser(self.name, help=self.description)
#          >>> parser_a.add_argument('bar', type=int, help='bar help')

    def set_name(self, name):
        self.name = name

    def print_name(self):
        print "This is plugin 1: %s" % self.name



#from up.plugin import BaseHook
##'virt'from up.utils import get_plugin_by_name
#
#def get_plugins_by_name(stage, plugin):
#    return [
#        plugin for plugin in stage.get('plugins')
#        if plugin.get('name') == name
#    ]
#
#def FL(cmd, *args, **kwargs):
#    return {
#        'command': cmd,
#        'args': args,
#        'kwargs': kwargs,
#    }
#
#
#class Hook(BaseHook):
#    name = 'virtualenv'
#    command = 'virtualenv %s'
#    commands = []
#
#    def __init__(self, subparsers):
#        import sys
#        print sys.argv
#        print subparsers
#
#        for stagename in self.args.on:
#            stage = settings.get_stage_by_name(stagename)
#            env.host_string = stage.get('host')
#            plugins = get_plugin_by_name(stage, self.name)
#            print plugins
#            for plugin in plugins:
#                path = plugin.get('path', '')
#
#            settings.get('branch')
#            stage.get('branch')
#
#        FL('version', {'help': 'show program\'s version number and exit'}),
#        FL('h,help', {'help': 'show this help message and exit'}),
#        FL('v,verbose'),
#        FL('q,quiet'),
#        FL('p,python', {
#            'type': str,
#            'metavar': 'PYTHON_EXE',
#            'help': """The Python interpreter to use, e.g.,
#--python=python2.5 will use the python2.5 interpreter
#to create the new environment.  The default is the
#interpreter that virtualenv was installed with (/usr/bin/python)"""}),
#        FL('clear'),
#        FL('no-site-packages'),
#        FL('unzip-setuptools'),
#        FL('relocatable'),
#        FL('distribute'),
#        FL('extra-search-dir'),
#        FL('never-download'),
#        FL('prompt')
#    ]
#def setup_virtualenv():
#    """
#    Setup virtualenv
#    """
#    dispatch_event(env, 'on-setup-virtualenv')
#    puts("Setuping virtualenv on %s" % env.host)
#    venv_root = os.path.join(get_conf(env, 'document-root'), 'virtualenv')
#
#    if not files.exists(venv_root):
#        sudo('mkdir -p %s' % venv_root)
#
#    with cd(venv_root):
#        sudo("virtualenv --distribute --no-site-packages %s" % env.site['project'])
#
#    user  = get_conf(env, 'user')
#    group = get_conf(env, 'group')
#
#    if user and group:
#        sudo("chown -R %s:%s %s" % (user, group, venv_root))
#    elif user:
#        sudo("chown -R %s %s" % (user, venv_root))
#    dispatch_event(env, 'on-setup-virtualenv-done')
