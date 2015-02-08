import up.plugin as base
from up.conf import Settings

settings = Settings()


class Django(base.UpPlugin):
    """
    """
    name = 'django'
    description = 'Setup Django on remote stage(s)'
    default_conf = {
        'settings': 'local_settings.py',
        'up-templates': [
            ['{{ current.stage }}_settings.py',
             '/var/www/vhosts/{{ current.stage }}.{{ project.domain }}/{{ django.settings }}'],
        ]
    }

    def init(self):
        self.on('deploy-init', self.copy_templates)
        self.on('deploy-init', self.collect_static)

    def collect_static(self, context=None):
        self.sudo('django collect_static')

    def restart(self):
        self.sudo('service nginx restart')

