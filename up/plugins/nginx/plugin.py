from up.plugin import BaseHook


class Hook(BaseHook):
    name = 'nginx'
    command = 'service nginx %s'
    automap_args = True
    config_template = ['%(stage)s.nginx', 'default.nginx']
    commands = ['start', 'stop', 'restart', 'reload',
                'force-reload', 'status', 'configtest']
