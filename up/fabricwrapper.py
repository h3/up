from fabric.api import env,  get, local, open_shell, prompt, put, sudo, run
from up.conf import Settings
from up.logger import get_logger

settings = Settings()
log = get_logger('up.fabric')
env.use_ssh_config = True

cmds = {
    'get': get,
    'open_shell': open_shell,
    'prompt': prompt,
    'put': put,
    'run': run,
    'sudo': sudo,
}


class FabricMixin(object):

    def cmd(self, cmd, *args, **kwargs):
        rs = []
        ctx = settings.get_context()

        if 'servers' in ctx:
            for host in ctx.get('servers'):
                env.host_string = host
                rs.append(cmds.get(cmd)(*args, **kwargs))
                if 'local_path' in kwargs:
                    print '%s' % kwargs.get('local_path').getvalue()
                log.info("[%s] %s: %s (%s)" % (host, cmd, args, kwargs))

        return rs

    def get(self, *args, **kwargs):
        return local(*args, **kwargs)

    def local(self, *args, **kwargs):
        return self.cmd('get', *args, **kwargs)

    def open_shell(self, *args, **kwargs):
        return self.cmd('open_shell', *args, **kwargs)

    def prompt(self, *args, **kwargs):
        return self.cmd('prompt', *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.cmd('put', *args, **kwargs)

    def run(self, *args, **kwargs):
        return self.cmd('run', *args, **kwargs)

    def sudo(self, *args, **kwargs):
        return self.cmd('sudo', *args, **kwargs)
