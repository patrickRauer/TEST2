from ninja import NinjaAPI, Router
from main.api import router as main_router
from mount.api import router as mount_router
from camera.api import router as camera_router

api = NinjaAPI()

router_v1 = Router()
router_v1.add_router('', main_router)
router_v1.add_router('mount/', mount_router)
router_v1.add_router('camera/', camera_router)
api.add_router('v1', router_v1)

