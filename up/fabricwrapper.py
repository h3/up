from fabric.api import env, sudo, run
from fabric.operations import put
from up.conf import Settings

settings = Settings()
env.use_ssh_config = True

cmds = {
    'run': run,
    'sudo': sudo,
    'put': put,
}


class FabricMixin(object):

    def cmd(self, cmd, *args, **kwargs):
        rs = []
        ctx = settings.get_context()

        if 'servers' in ctx:
            for host in ctx.get('servers'):
                print "[%s] %s: %s (%s)" % (host, cmd, args, kwargs)
                env.host_string = host
                rs.append(cmds.get(cmd)(*args, **kwargs))
        return rs

    def put(self, *args, **kwargs):
        return self.cmd('put', *args, **kwargs)

    def run(self, *args, **kwargs):
        return self.cmd('run', *args, **kwargs)

    def sudo(self, *args, **kwargs):
        return self.cmd('sudo', *args, **kwargs)
