class Mock:
    def __init__(self):
        self._calls = []

    def assert_not_called(self):
        assert len(self._calls) == 0

    def assert_called_once(self):
        assert len(self._calls) == 1

    def assert_called_once_with(self, *args, **kwargs):
        count = 0
        for call in self._calls:
            if call == (args, kwargs):
                count += 1
        assert count == 1

    def __call__(self, *args, **kwargs):
        self._calls.append((args, kwargs))
