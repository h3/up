import os
import re
import yaml
import subprocess


def run(*args, **kwargs):
    return subprocess.check_output(args, **kwargs).replace('\n', '')


class Stage(object):
    def __init__(self, stage):
        self._stage = stage

    def get(self, key):
        return self._stage.get(key)


class Settings(object):
    context = {'project': {}, 'current': {}, 'stages': {}, 'plugins': {}}

    def set_plugin_defaults(self, plugin, defaults):
        self.context['plugins'][plugin] = defaults

    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'up/conf.yml')
        self.fd = open(self.path, 'r')
        self.yaml = yaml.load(self.fd)

        if self.yaml is None:
            raise ValueError('Invalid configuration file.')

        if not self.yaml.get('project'):
            raise ValueError('The "project" section is missing from the configuration file')

        # Fill up base context variables
        self.context['current']['hostname'] = run('hostname')
        self.context['current']['user'] = run('whoami')

        for k,v in self.yaml.get('project').iteritems():
            self.context['project'][k] = v

        for k,v in self.yaml.get('stages').iteritems():
            self.context['stages'][k] = self.interpolate(v)

    def interpolate_string(self, s):
        pattern = re.compile(r'.*%\(([A-Za-z0-9-_.]+)\)(\w{1}).*')
        rs = pattern.match(s)
        if rs:
            path, flag = rs.groups()
            _str = '%(' + path + ')' + flag
            return s.replace(_str, self.get(path, cast=flag) or '')
        else:
            return s

    def interpolate(self, obj):
        """
        Accepts dict, list and string
        """
        out = obj
        if isinstance(obj, dict):
            for k,v in obj.iteritems():
                out[k] = self.interpolate(v)
        elif isinstance(obj, list):
            out = [self.interpolate(v) for v in obj]
        elif isinstance(obj, str):
            out = self.interpolate_string(obj)
        return out

    @property
    def plugins(self):
        try:
            return self.yaml.get('up').get('plugins')
        except AttributeError:
            return []

    @property
    def stages(self):
        if self.yaml.get('stages') is None:
            raise ValueError('You must define at least one stage.')
        return self.yaml.get('stages').keys()

    def get_stage(self):
        try:
            return settings.context['current']['stage']
        except AttributeError:
            return None

    def get(self, key, cast='s'):
        if '.' not in key:
            _str = '%' + cast
            return _str % self.context[key]
        else:
            keys = key.split('.')
            obj = self.context[keys[0]]
            for k in keys[1:]:
                obj = obj.get(k)
            return obj

settings = Settings()
