# -*- coding: utf-8 -*-

import os
import re
import yaml
import subprocess

from up.templates import template


def run(*args, **kwargs):
    return subprocess.check_output(args, **kwargs).replace('\n', '')


class Stage(object):
    def __init__(self, stage):
        self._stage = stage

    def get(self, key):
        return self._stage.get(key)


class Settings(object):
    _context = {'project': {}, 'current': {}, 'stages': {}, 'plugins': {}}

    def __init__(self):
        self.__dict__ = self._context
        self.path = os.path.join(os.getcwd(), 'up/conf.yml')
        self.fd = open(self.path, 'r')
        self.yaml = yaml.load(self.fd)

        if self.yaml is None:
            raise ValueError('Invalid configuration file.')

        if not self.yaml.get('project'):
            raise ValueError('The "project" section is missing from the configuration file')

        # Fill up base context variables
        self._context['current']['hostname'] = run('hostname')
        self._context['current']['user'] = run('whoami')

    def set_plugin_defaults(self, plugin, defaults):
        self._context['plugins'][plugin] = defaults


    @property
    def plugins(self):
        if 'plugins' in self.yaml.get('up'):
            return self.yaml.get('up').get('plugins')
        else:
            return self.yaml.get('plugins').keys()

    def get_context(self, stage=None):
        self._context['project'] = self.yaml.get('project')
        current_stage = stage or self.get_stage()
        stage = self.yaml.get('stages').get(current_stage)
        dcontext = {}
        # Load plugins default context
        for plugin in self.plugins:
            dcontext[plugin] = self._context.get('plugins').get(plugin, {})
            print "LOADED PLUGIN CONTEXT: %s : %s" % (plugin, dcontext[plugin])
            if stage.get('extends') and stage.get('extends').get(plugin):
                dcontext[plugin].update(stage.get('extends').get(plugin))
                del stage['extends'][plugin]
            if stage.get(plugin):
                dcontext[plugin].update(stage.get(plugin))
                del stage[plugin]

        # Load base context if needed
        if stage.get('extends'):
            dcontext.update(stage.get('extends'))
            del stage['extends']
        # Stage context overrides base and default context
        dcontext.update(stage)
        print "ZZZ %s" % dcontext
        # Push everything back into main context and we're done
        self._context.update(self.interpolate(dcontext, context=self._context))
        print "+===============================================+++++"
        print "xxx %s" % self._context
        print "+===============================================+++++"
        return self._context

    def interpolate_string(self, s, context=None):
        if not context:
            context = self.get_context()
        return template(s, context)

    def interpolate(self, obj, context=None):
        """
        Accepts dict, list and string
        """
        out = obj
        if not context:
            context = self.get_context()

        if isinstance(obj, dict):
            for k,v in obj.iteritems():
                out[k] = self.interpolate(v, context=context)
        elif isinstance(obj, list):
            out = [self.interpolate(v, context=context) for v in obj]
        elif isinstance(obj, str):
            out = self.interpolate_string(obj, context=context)
        return out

    def set_stage(self, stage):
        self._context['current']['stage'] = stage

    @property
    def stages(self):
        if self.yaml.get('stages') is None:
            raise ValueError('You must define at least one stage.')
        return self.yaml.get('stages').keys()

    def get_stage(self):
        try:
            return self._context['current']['stage']
        except AttributeError:
            return None

    def get(self, key):
        if '.' not in key:
            return self._context[key]
        else:
            keys = key.split('.')
            obj = self._context[keys[0]]
            for k in keys[1:]:
                obj = obj.get(k)
            return obj
