from requests import get, put


class FilterWheel:
    _url = None,
    _device_number = None
    _states = None

    def __init__(self, url, device_number):
        if url[-1] != '/':
            url += '/'
        self._url = f'{url}/filterwheel/{device_number}/'
        self._device_number = device_number
        self._states = {0: 'idle', 1: 'waiting', 2: 'exposing', 3: 'reading', 4: 'downloading', 5: 'error'}
        
    def focus_offset(self):
        return self._get('focusoffsets')
    
    def names(self):
        return self._get('names')
    
    def position(self):
        return self._get('position')
    
    def set_position(self, value):
        return self._put('position', data={'Position': value})

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
