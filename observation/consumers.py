import json
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from .code.dummy import DummyWheel, DummyTelescope

dw = DummyWheel()
dt = DummyTelescope()


class StatusConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps(
            {
                'message': 'connected'
            }
        ))
        dw.add_consumer(self)
        dt.add_consumer(self)

    def disconnect(self, close_code):
        dw.stop()
        dt.stop()
        pass

    def receive(self, text_data):
        print('status update')
        text_data_json = json.loads(text_data)

        for k in text_data_json:
            print(k, ':', text_data_json[k])

        try:
            message = text_data_json['message']
        except KeyError:
            message = 'test'

        out = {
            'message': message
        }
        if 'device' in text_data_json:
            out['device'] = text_data_json['device']
            if 'filter_wheel' == text_data_json['device']:
                dw.change_filter(text_data_json['filter_wheel'])
            elif 'telescope' == text_data_json['device']:
                if 'slew' == text_data_json['command']:
                    dt.slew()
                elif 'park' == text_data_json['command']:
                    dt.park()

        self.send(text_data=json.dumps(
            out
        ))

    def send_status_update(self, status):
        # status['time'] = datetime.utcnow().strftime('%Y-%M-%d %h:%m%:%s')
        self.send(text_data=json.dumps(
            status
        ))


class ImageConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

    def send_image(self, image):
        """

        :param image:
        :type image: ndarray
        :return:
        """
        self.send(
            bytes_data=json.dumps(
                {
                    'image': image.tobytes()
                }
            )
        )
