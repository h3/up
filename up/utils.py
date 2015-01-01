def import_module(name, package=None):
    try:
        from django.utils.importlib import import_module
        return import_module(name, package)
    except ImportError:
        path = [m for m in name.split('.')]
        print name
        print path
        return __import__(name, {}, {}, path[-1])


def import_class(classpath):
    classname = classpath.split('.')[-1]
    classpath = '.'.join(classpath.split('.')[:-1])
    return getattr(import_module(classpath), classname, None)
