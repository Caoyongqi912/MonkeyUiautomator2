import time
from Config.Setting import get_logger

from uiautomator2 import UiObjectNotFoundError


def pinduoduo(package_name, version_id, d):
    logger = get_logger(__name__)
    logger.info(package_name)

    if version_id == '4.59.0':

        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except Exception as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Ok .....')
            d(resourceId='com.xunmeng.pinduoduo:id/b7k').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Agree .....')
            d(resourceId='android:id/button1').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
        try:
            logger.info(' -> Wechat .....')
            d(resourceId='com.xunmeng.pinduoduo:id/ac0').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Close Windows .....')
            d(resourceId='com.xunmeng.pinduoduo:id/m_').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

    elif version_id == '4.58.0':
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except Exception as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Ok .....')
            d(resourceId='com.xunmeng.pinduoduo:id/b5j').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Agree .....')
            d(resourceId='android:id/button1').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Jump .....')
            d(resourceId='com.xunmeng.pinduoduo:id/b80').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Close Windows .....')
            d(resourceId='com.xunmeng.pinduoduo:id/m_').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
    elif version_id == '4.60.0':
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except Exception as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Ok .....')
            d(resourceId='com.xunmeng.pinduoduo:id/b8n').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Agree .....')
            d(resourceId='android:id/button1').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
        try:
            logger.info(' -> Wechat .....')
            d(resourceId='com.xunmeng.pinduoduo:id/acw').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Close Windows .....')
            d(resourceId='com.xunmeng.pinduoduo:id/mg').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')


    elif version_id == '4.61.0':
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except Exception as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Ok .....')
            d(resourceId='com.xunmeng.pinduoduo:id/ba9').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Agree .....')
            d(resourceId='android:id/button1').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
        try:
            logger.info(' -> Wechat .....')
            d(resourceId='com.xunmeng.pinduoduo:id/acp').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Close Windows .....')
            d(resourceId='com.xunmeng.pinduoduo:id/ly').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
