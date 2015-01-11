# -*- coding: utf-8 -*-

import os

from jinja2 import Template

def template(s, context={}):
    tpl = Template(s.decode('utf-8'))
    tpl.globals['pathjoin'] = os.path.join
    return tpl.render(context)
