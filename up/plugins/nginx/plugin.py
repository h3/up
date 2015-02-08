import up.plugin as base
from up.conf import Settings

settings = Settings()


class Nginx(base.UpPlugin):
    """
    """
    name = 'nginx'
    description = 'Setup nginx on remote stage(s)'
    default_conf = {
        'server-name': '{{ current.stage }}.{{ project.domain }}',
        'up-templates': [
            ['{{ current.stage }}.{{ project.domain }}', '/etc/nginx/sites-enabled'],
        ],
    }

    def init(self):
        self.on('deploy-init', self.copy_templates)
        self.on('deploy-done', self.reload)

    def reload(self, context=None):
        self.sudo('service nginx reload')

    def restart(self, context=None):
        self.sudo('service nginx restart')
