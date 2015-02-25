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
        """
        Binds an event to a callback, also accept a context
        which will be updated by the trigger's context
        """
        if eventName not in self._state['callbacks']:
            self._state['callbacks'][eventName] = []
        args = {
            'eventName': eventName,
            'callback': callback,
            'context': context,
        }
        self._state['callbacks'][eventName].append(args)
        log.info(u'%s (context: %s)' % (eventName, context))

    def trigger(self, eventName, context=None):
        """
        Loops throught all callbacks binded to a given eventName
        and call them with a given context.
        """
        if eventName in self._state['callbacks']:
            for callback in self._state['callbacks'][eventName]:
                ctx = {}
                if callback['context']:
                    ctx.update(callback['context'])
                if context:
                    ctx.update(context)
                callback['callback'](context)
