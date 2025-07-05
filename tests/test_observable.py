import unittest
from unittest.mock import Mock

from observable import Observable


class ObserverTestCase(unittest.TestCase):
    def test_observable_detaching_unattached_callback_throws_exception(self):
        observable = Observable()
        callback = Mock()
        with self.assertRaises(ValueError):
            observable.detach(callback)

    def test_observable_detaching_attached_callback_does_not_throw_exception(self):
        observable = Observable()
        callback = Mock()
        observable.attach(callback)
        observable.detach(callback)

    def test_observable_notifies_attached_callbacks(self):
        observable = Observable()
        callback = Mock()
        observable.attach(callback)
        observable.notify()
        callback.assert_called_once()

    def test_observable_does_not_notify_detached_callbacks(self):
        observable = Observable()
        callback = Mock()
        observable.attach(callback)
        observable.detach(callback)
        observable.notify()
        callback.assert_not_called()

    def test_self_detaching_callback_does_not_derail_notify(self):
        observable = Observable()
        class SelfDetachingCallback:
            def callback(self):
                observable.detach(self.callback)
        callback = SelfDetachingCallback()
        observable.attach(callback.callback)

        other_callback = Mock()
        observable.attach(other_callback)

        observable.notify()
        other_callback.assert_called_once()

    def test_observable_forwards_args_to_callbacks(self):
        arg = object()
        observable = Observable()
        callback = Mock()
        observable.attach(callback)
        observable.notify(arg)
        callback.assert_called_once_with(arg)

    def test_observable_forwards_kwargs_to_callbacks(self):
        arg = object()
        observable = Observable()
        callback = Mock()
        observable.attach(callback)
        observable.notify(key=arg)
        callback.assert_called_once_with(key=arg)


if __name__ == '__main__':
    unittest.main()
