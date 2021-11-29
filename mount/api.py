from ninja import Router
from alpaca import Telescope


mount = Telescope('127.0.0.1:11111', 0)

router = Router()

direction = Router()
router.add_router('direction/', direction)


def deg2hms(value):
    value = value/360*24
    hour = int(value)
    value -= hour
    value *= 60
    minutes = int(value)
    value -= minutes
    value *= 60
    seconds = int(value)
    return f'{hour:02d}:{minutes:02d}:{seconds:02d}'


def deg2dms(value):
    degree = int(value)
    value -= degree
    value *= 60
    minutes = int(value)
    value -= minutes
    value *= 60
    seconds = int(value)
    return f'{degree:02d}:{minutes:02d}:{seconds:02d}'


@direction.get('all/')
def all_direction(request):
    out = {
        'ra': deg2dms(mount.rightascension()),
        'dec': deg2dms(mount.declination()),
        'alt': deg2dms(mount.altitude()),
        'az': deg2dms(mount.azimuth())
    }

    return out
