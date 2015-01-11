import up.plugin as base
from up.conf import Settings

settings = Settings()


class Uwsgi(base.UpPlugin):
    """
    """
    name = 'uwsgi'
    description = 'Setup uwsgi on remote stage(s)'
    default_conf = {
        'processes': 2,
        'up-templates': [
            ['{{ current.stage }}.{{ project.domain }}.ini', '/etc/uwsgi/app-enabled'],
        ]
    }

    def init(self):
        self.on('deploy-init', self.copy_templates)
