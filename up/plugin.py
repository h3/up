# -*- coding: utf-8 -*-

import os

from yapsy.IPlugin import IPlugin
from fabric.api import env, sudo, run

from up import log
from up.utils import import_class
from up.conf import Settings
from up.events import EventMixin
from up.fabricwrapper import FabricMixin
from up.templates import template

settings = Settings()


class UpPlugin(IPlugin, EventMixin, FabricMixin):
    """
    Base plugin class
    """

    def copy_templates(self, context):
        rs = []
        tpl_context = settings.get_context()
        if 'up-templates' in tpl_context.get(self.name):
            for tpl in tpl_context.get(self.name).get('up-templates'):
                rs.append(self.copy_template(tpl[0], tpl[1], context=tpl_context))
        return rs

    def copy_template(self, src, dst, context={}):
        with open (os.path.join(os.getcwd(), 'up/templates/', self.name, src), 'r') as fd:
            tpl = template(fd.read(), context, stringio=True)
            return self.put(local_path=tpl, remote_path=dst, use_glob=False)
