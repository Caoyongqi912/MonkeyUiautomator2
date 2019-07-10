import time
from Config.Setting import get_logger, USERNAME, PASSWORD

from uiautomator2 import UiObjectNotFoundError


def suning(package_name, version_id, d):
    logger = get_logger(__name__)
    logger.info(package_name)

    if version_id == '7.7.3':
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except Exception as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Agree .....')
            d(resourceId='com.suning.mobile.ebuy:id/positive').click()
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
            d(resourceId='android:id/button1').click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Car .....')
            d(resourceId="com.suning.mobile.ebuy:id/iv_tab_icon", description=u"苏宁易购",
                   className="android.widget.ImageView",
                   instance=1).click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Go login  .....')
            d(resourceId="com.suning.mobile.ebuy:id/tv_cart1_emtpy_btn").click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Swich_login_type .....')
            d(resourceId="com.suning.mobile.ebuy:id/tv_swich_login_type").click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> username  .....')
            d(resourceId="com.suning.mobile.ebuy:id/account").send_keys(USERNAME)
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> password  .....')
            d(resourceId="com.suning.mobile.ebuy:id/password").send_keys(PASSWORD)
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Login  .....')
            d(resourceId="com.suning.mobile.ebuy:id/btn_logon_first").click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> go Index   .....')
            d.press("back")
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(' -> Close Window   .....')
            d(resourceId="com.suning.mobile.ebuy:id/home_new_person_delete_iv").click()
            logger.info(' -> Done')
            time.sleep(3)
        except UiObjectNotFoundError as e:
            logger.info(' -> Not Found ....')

        logger.info('%s uiautomator  Done ...' % package_name)
