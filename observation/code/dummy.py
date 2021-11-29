from threading import Thread
import time


class Dummy(Thread):

    _consumer = None
    _active = True

    def __init__(self):
        Thread.__init__(self)
        self._active = True
        self._consumer = []

    def add_consumer(self, consumer):
        self._consumer.append(consumer)

    def remove_consumer(self, i):
        self._consumer.pop(i)

    def send(self, data):
        for c in self._consumer:
            try:
                c.send_status_update(data)
            except AttributeError:
                pass

    def stop(self):
        self._active = False


class DummyWheel(Dummy):
    _next_filter = None
    _current_filter = None

    def __init__(self):
        Dummy.__init__(self)
        self._current_filter = 'U'
        self.start()

    def run(self):
        while self._active:
            if self._next_filter is not None:
                self.send_update('moving')
                time.sleep(1)
                self.send_update(self._next_filter)
                self._next_filter = None
            time.sleep(0.1)
            pass

    def send_update(self, current_filter):
        self.send(
            {
                'device': 'filter_wheel',
                'command': 'change',
                'command_id': 0,
                'filter_wheel': current_filter,
                'successes': True
            }
        )

    def change_filter(self, new_filter):
        self._next_filter = new_filter


class DummyTelescope(Dummy):
    _command = None

    def __init__(self):
        Dummy.__init__(self)
        self.start()

    def run(self):
        while self._active:

            if 'slew' == self._command:
                self.send_update('slewing')
                time.sleep(1)
                self.send_update('tracking')
                self._command = None
                pass
            elif 'park' == self._command:
                self.send_update('parking')
                time.sleep(1)
                self.send_update('parked')
                self._command = None
                pass

            time.sleep(0.1)
        pass

    def park(self):
        self._command = 'park'
        pass

    def slew(self):
        self._command = 'slew'
        pass

    def send_update(self, telescope_status):
        self.send(
            {
                'device': 'telescope',
                'command': self._command,
                'status': telescope_status,
                'command_id': 0,
                'ra': 0.0,
                'dec': 0.0
            }
        )
