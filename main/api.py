from ninja import Router
from astropy.time import Time
from datetime import datetime
router = Router()


@router.get('time')
def get_current_time(request):
    time = Time.now()
    local_time = datetime.now()
    out = {
        'utc': time.utc.iso.split(' ')[-1].split('.')[0],
        'local': local_time.strftime('%H:%M:%S'),
        'mjd': round(time.mjd, 4)
    }
    return out
