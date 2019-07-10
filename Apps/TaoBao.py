import time
from Config.Setting import get_logger, USERNAME, PASSWORD

from uiautomator2 import UiObjectNotFoundError


def taobao(package_name, version_id, d):
    logger = get_logger(__name__)
    logger.info(package_name)

    if version_id == '8.8.0':

        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
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
            logger.info(' -> Agree .....')
            d(resourceId='com.taobao.taobao:id/yes').click()
            logger.info(' -> Done')
            time.sleep(5)
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
            logger.info(' -> Close 618  Windows  .....')
            d(resourceId="com.taobao.taobao:id/tv_member_code_text").click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> 立即抢 .....')
            d(text='立即抢').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Login .....')
            d(resourceId='com.taobao.taobao:id/aliuser_login_switch_pwdlogin').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Username .....')
            d(resourceId='com.taobao.taobao:id/aliuser_login_account_et').send_keys(USERNAME)
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Password .....')
            d(resourceId='com.taobao.taobao:id/aliuser_login_password_et').send_keys(PASSWORD)
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Login  .....')
            d(resourceId='com.taobao.taobao:id/aliuser_login_login_btn').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
        try:
            logger.info(' -> Agree .....')
            d(resourceId='com.taobao.taobao:id/uik_mdButtonDefaultPositive').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')
