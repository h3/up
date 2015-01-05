import up.plugin as base
from up.conf import settings


class Virtualenv(base.UpPlugin):
    name = 'virtualenv'
    description = 'Generic virtualenv support'

    default_conf = {
       'path': '/%(project.root)s/venv',
       'requirements': '/%(project.root)s/requirements.pip',
    }

    def init(self):
        self.on('deploy-done', self.run)

    def run(self, context=None):
        pass


#
#
#
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
