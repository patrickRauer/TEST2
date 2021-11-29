from celery import shared_task
from .models import Tracker
from archive.models import Image
from observation.models import ObservationList
from astropy.io import fits
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy import units as u
from alpaca import Camera, Telescope
import time

camera = Camera('127.0.0.1:11111', 0)
mount = Telescope('127.0.0.1:11111', 0)

location = EarthLocation(lat=50.980897*u.deg, lon=11.71098558*u.deg, height=330*u.m)


def to_frame():
    return f'[{camera.startx()}:{camera.numx()},{camera.starty()}:{camera.numy()}]'


def create_header(image):
    time = Time(image.exposure_started, format='datetime')
    coords = SkyCoord(
        image.target.ra*u.deg, image.target.dec*u.deg,
    ).transform_to(AltAz(obstime=time, location=location))
    header = fits.Header()
    header['Date'] = image.exposure_started.today()
    header['JD'] = time.jd
    header['telescope'] = 'TEST'
    header['Object'] = image.name
    header['IMATYPE'] = image.type.name
    header['Observer'] = image.observer.username
    header['EXP_TIME'] = image.exposure_time
    header['Observat'] = 'TLS'
    header['Detsize'] = '[4096:4096]'
    header['CCDSEC'] = to_frame()
    header['FLTNR'] = image.filter.position
    header['FLTName'] = image.filter.name
    header['TEMP_CHIP'] = camera.ccdtemperature()
    header['HA'] = coords.hangles
    header['LST'] = coords.l
    header['TARGETRA'] = image.target.ra
    header['TARGETDE'] = image.target.dec

    return header


@shared_task
def download_image():
    Tracker(action='download').save()
    image_data = camera.imagearray()
    image = Image.objects.last()

    with fits.open('temp.fits', mode='write') as fi:
        fi.data = fits.PrimaryHDU(data=image_data, header=create_header(image))

    with open('./temp.fits') as fi:
        image.data.save(f'{image.name}.fits', fi)
    image.save()


@shared_task
def flats_and_darks():
    obs_list = ObservationList.objects.filter(done=False, dars_gte=0)

    exposure_times = []
    for olist in obs_list:
        observations = olist.observation_set.all()
        for obs in observations:
            if obs.exposure_time not in exposure_times:
                for i in olist.darks:
                    # todo: use start exposure not directly
                    camera.startexposure(obs.exposure_time, False)
                    while camera.camerastate() != 0:
                        time.sleep(5)