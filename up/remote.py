from fabric.api import env, sudo, run
from up.conf import settings

env.use_ssh_config = True


class FabricMixin(object):

    def remote(self, *args, **kwargs):
        print "RUNNING: %s" % args
       #import IPython
       #IPython.embed()
       #env.host_string = stage.get('host')
       #run(*args, **kwargs)
