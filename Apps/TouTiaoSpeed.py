import time
from Config.Setting import get_logger

from uiautomator2 import UiObjectNotFoundError


def tt_speed(package_name, version_id, d):
    logger = get_logger(__name__)
    logger.info(package_name)
    if version_id in ['6.9.5', '6.9.2', '6.9.6', "6.9.9"]:
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            pass
        try:
            logger.info(' -> Agree ....')
            d(resourceId='android:id/button1').click()
            time.sleep(3)
            logger.info(' -> Done')
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Close window ....')
            d(resourceId='com.ss.android.article.lite:id/z0').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
