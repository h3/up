print "CCC"
class Event(object):
    """
    This object uses the Borg pattern to ensure a shared
    state to act as a bus to allow plugins to communicate
    using an event based model.

    >>> from up.events import Event
    >>> from yapsy.IPlugin import IPlugin
    >>>
    >>> class MyPlugin(IPlugin, UpEvent):
    >>>     def __init__(self):
    >>>         self.trigger('my-event', context={'some': 'data'})
    >>>         self.on('some-event', self.on_some_event)
    >>>
    >>>     def on_some_event(self, context):
    >>>         print context
    """
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

    def on(self, eventName, callback, context=None):
        pass

    def trigger(self, eventName, context=None):
        pass
