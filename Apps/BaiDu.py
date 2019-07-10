import time
from Config.Setting import get_logger

from uiautomator2 import UiObjectNotFoundError


def baidu(package_name, version_id,d):
    logger = get_logger(__name__)
    logger.info(package_name)
    if version_id in ['11.9.0.11', '11.8.0.10', '11.10.0.12']:

        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except Exception as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Agree and continue ..... ')
            d(resourceId='com.baidu.searchbox:id/positive_button').click()
            logger.info(' -> Done .....')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Agree One ...')
            d(resourceId='android:id/button1').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
        try:
            logger.info(' -> Agree Permission ...')
            d(resourceId='android:id/button1').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
        try:
            logger.info(' -> Agree Local ...')
            d(resourceId='android:id/button1').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
        try:
            logger.info(' -> Not Update ...')
            d(resourceId='com.baidu.searchbox:id/update_close').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
        logger.info(" -> Done ...")
