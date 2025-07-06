class Observable:
    def __init__(self):
        self._callbacks = []

    def detach(self, callback):
        self._callbacks.remove(callback)

    def attach(self, callback):
        self._callbacks.append(callback)

    def notify(self, *args, **kwargs):
        for callback in list(self._callbacks):
            callback(*args, **kwargs)
