from up.plugin import BaseHook


class Hook(BaseHook):
    name = 'uwsgi'
    command = 'service uwsgi %s'
    automap_args = True
    config_template = ['%(stage)s.uwsgi', 'default.uwsgi']
    commands = ['start', 'stop', 'status', 'restart',
                'reload', 'force-reload']
