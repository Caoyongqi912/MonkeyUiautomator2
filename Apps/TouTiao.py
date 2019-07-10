import time
from Config.Setting import get_logger

from uiautomator2 import UiObjectNotFoundError


def toutiao(package_name, version_id, d):
    logger = get_logger(__name__)
    logger.info(package_name)

    if version_id in ['7.2.9', "7.3.0"]:
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> I Know ....')
            d(resourceId='com.ss.android.article.news:id/a4u').click()
            time.sleep(3)
            logger.info(' -> Done')
        except UiObjectNotFoundError as  e:
            logger.info(' -> Not Found ....')


    elif version_id == '7.2.7':
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> I Know ....')
            d(resourceId='com.ss.android.article.news:id/a4r').click()
            time.sleep(3)
            logger.info(' -> Done')
        except UiObjectNotFoundError as  e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> I Agree ....')
            d(resourceId='android:id/button1').click()
            time.sleep(6)
            logger.info(' -> Done')
        except UiObjectNotFoundError as  e:
            logger.info(' -> Not Found ....')
    elif version_id == '7.4.2':
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> I Know ....')
            d(resourceId='com.ss.android.article.news:id/a4j').click()
            time.sleep(3)
            logger.info(' -> Done')
        except UiObjectNotFoundError as  e:
            logger.info(' -> Not Found ....')
