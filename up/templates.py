# -*- coding: utf-8 -*-

import os
import StringIO

from jinja2 import Template


def template(s, context={}, stringio=False):
    tpl = Template(s.decode('utf-8'))
    tpl.globals['pathjoin'] = os.path.join
   #print "ZZZ %s" % context
   #import IPython
   #IPython.embed()
    out = tpl.render(context)
    if stringio:
        tmp = StringIO.StringIO()
        tmp.write(out)
        return tmp
    else:
        return out
