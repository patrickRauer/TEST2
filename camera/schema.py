from ninja import Schema


class ImageExposureSchema(Schema):
    exposure_time: int
    ra: float
    dec: float
    filter: str
