import os
import yaml


class Stage(object):
    def __init__(self, stage):
        self._stage = stage

    def get(self, key):
        return self._stage.get(key)



class Settings(object):
    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'up/conf.yml')
        self.fd = open(self.path, 'r')
        self.yaml = yaml.load(self.fd)

        if self.yaml is None:
            raise ValueError('Invalid configuration file.')

       #for k in self.yaml.keys():
       #    v = self.yaml.get(k)
       #    if isinstance(v, str):
       #        return self._interpolate(v)

       #import IPython
       #IPython.embed()

    @property
    def stages(self):
        if self.yaml.get('stages') is None:
            raise ValueError('You must define at least one stage.')
        return [s.get('name') for s in self.yaml.get('stages')]

    def get_stage_by_name(self, name):
        for s in self.yaml.get('stages'):
            if s.get('name') == name:
                return Stage(s)
        return None

settings = Settings()

setattr(settings, 'STAGES_KWARGS', {
    'type': str,
    'choices': settings.stages,
    'metavar': 'STAGES',
    'nargs': '*',
    'help': 'Target stages',
})
