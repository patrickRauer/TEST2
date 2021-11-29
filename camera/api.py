from ninja import Router
from alpaca import Camera, FilterWheel
import time

from filter_wheel.models import Filter

from .schema import ImageExposureSchema

camera = Camera('127.0.0.1:11111', 0)
filter_wheel = FilterWheel('127.0.0.1:11111', 0)
router = Router(tags=['camera'])
states = {0: 'idle', 1: 'waiting', 2: 'exposing', 3: 'reading', 4: 'downloading', 5: 'error'}
filters = Filter.objects.all()


def _get_filter():
    filter_position = filter_wheel.position()
    if filter_position != -1:
        filter_name = filters.get(position=filter_position).name
    else:
        filter_name = 'moving'
    return {'position': filter_position, 'name': filter_name}


@router.get('status')
def get_status(request):

    return {'status': states[camera.camerastate()], 'temperature': camera.ccdtemperature(),
            'filter': _get_filter()['name']}


@router.get('image/ready')
def is_image_ready(request):
    return {
        'image': camera.imageready()
    }


@router.post('image')
def take_image(request, image_data: ImageExposureSchema):
    filter_wheel.position(filters.get(key=image_data.filter).position)
    while _get_filter()['position'] == -1:
        time.sleep(1)

    camera.startexposure(image_data.exposure_time, True)
    return {'exposure': 'started'}


@router.get('filter')
def get_filter(request):
    return _get_filter()
