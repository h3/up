from up.logger import get_logger

log = get_logger('up.events')


class EventMixin(object):
    """
    This object uses the Borg pattern to ensure a shared
    state to act as a bus to allow plugins to communicate
    using an event based model.
    """
    _state = {'callbacks': {}}

    def __init__(self):
        self.__dict__ = self._state

    def on(self, eventName, callback, context=None):
        if eventName not in self._state['callbacks']:
            self._state['callbacks'][eventName] = []
        args = {
            'eventName': eventName,
            'callback': callback,
            'context': context,
        }
        log.warning('TEST')
        self._state['callbacks'][eventName].append(args)

    def trigger(self, eventName, context=None):
        if eventName in self._state['callbacks']:
            for callback in self._state['callbacks'][eventName]:
                ctx = {}
                if callback['context']:
                    ctx.update(callback['context'])
                if context:
                    ctx.update(context)
                callback['callback'](context)
