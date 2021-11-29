from requests import get, put


class Camera:
    _url = None,
    _device_number = None
    _states = None

    def __init__(self, url, device_number):
        if url[-1] != '/':
            url += '/'
        self._url = f'{url}/camera/{device_number}/'
        self._device_number = device_number
        self._states = {0: 'idle', 1: 'waiting', 2: 'exposing', 3: 'reading', 4: 'downloading', 5: 'error'}

    def status(self, as_int=False):
        state = self._get('camerastate')
        if as_int:
            return state
        else:
            return self._states[state]
        
    def bin_x(self):
        return self._get('binx')
    
    def set_bin_x(self, value):
        return self._put('binx', data={'BinX': value})
    
    def bin_y(self):
        return self._get('biny')
    
    def set_bin_y(self, value):
        return self._put('biny', data={'BinY': value})
        
    def cooler_status(self):
        return self._get('cooleron')
    
    def set_cooler_status(self, on=True):
        return self._put('cooloron', data={'CoolerOn': on})
    
    def cooler_power(self):
        return self._get('coolerpower')

    def image_ready(self):
        ready = self._get('imageready')
        return ready

    def get_image(self):
        image = self._get('imagearray')
        return image

    def num_x(self):
        return self._get('numx')

    def set_num_x(self, value):
        return self._put('numx', data={'NumX': value})

    def num_y(self):
        return self._get('numy')

    def set_num_y(self, value):
        return self._put('numy', data={'NumY': value})

    def process_percentage(self):
        return self._get('percentcompleted')

    def get_set_temperature(self):
        return self._get('setccdtemperature')

    def set_temperature(self, temperature):
        return self._put('setccdtemperature', data={'SetCCDTemperature': temperature})
    
    def start_x(self):
        return self._get('startx')
    
    def set_start_x(self, value):
        return self._put('startx', data={'StartX': value})

    def start_y(self):
        return self._get('starty')

    def set_start_y(self, value):
        return self._put('starty', data={'StartY': value})

    def abort_exposure(self):
        return self._put('abortexposure')

    def start_exposure(self, exposure_time, dark=False):
        return self._put('startexposure', data={'Duration': exposure_time, 'Light': not dark})

    def stop_exposure(self):
        return self._put('stopexposure')
    
    def temperature(self):
        return self._get('ccdtemperature')

    def frame(self):
        return f'[{self.start_x()}:{self.num_x()},{self.start_y()}:{self.num_y()}]'

    def _put(self, uri, data=None):
        resp = put(
            f'{self._url}{uri}',
            data=data
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            raise ValueError(resp.text)

    def _get(self, uri, data=None):
        resp = get(
            f'{self._url}{uri}',
            data=data
        )
        if resp.status_code == 200:
            return resp.json()['Value']
        else:
            raise ValueError(resp.text)
