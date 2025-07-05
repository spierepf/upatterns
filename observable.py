class Observable:
    def __init__(self):
        self.callbacks = []

    def detach(self, callback):
        self.callbacks.remove(callback)

    def attach(self, callback):
        self.callbacks.append(callback)

    def notify(self, *args, **kwargs):
        for callback in list(self.callbacks):
            callback(*args, **kwargs)
