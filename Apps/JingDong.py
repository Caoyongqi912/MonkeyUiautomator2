import time

from selenium.common.exceptions import NoSuchElementException
from Config.Setting import get_logger, USERNAME, PASSWORD



def jingdong(package_name, version_id, d):
    logger = get_logger(__name__)
    logger.info(package_name)
    if version_id == '8.1.0':
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except Exception as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(" -> I Know ....")
            d(resourceId='com.jingdong.app.mall:id/bqp').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)
        try:
            logger.info(' -> Start ..')
            d(resourceId='com.jingdong.app.mall:id/c6i').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Keep ...")
            d(resourceId='com.jingdong.app.mall:id/ar2').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)
        try:
            logger.info(' -> Agree ....')
            d(resourceId='android:id/button1').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)
        try:
            logger.info(' -> Agree ....')
            d(resourceId='android:id/button1').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3 * 2)

        try:
            logger.info(" -> Close Windows")
            d(resourceId="com.jingdong.app.mall:id/bjj").click()
        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Mine ")
            d(description=u"我的", className="android.view.View").click()
        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Login ...  ")
            d(resourceId="com.jd.lib.personal:id/ss").click()
        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Username ...  ")
            d(resourceId="com.jd.lib.login:id/q5").send_keys(USERNAME)

        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Password ...  ")
            d(resourceId="com.jd.lib.login:id/q7").send_keys(PASSWORD)

        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> login  ...  ")
            d(resourceId="com.jd.lib.login:id/qb").click()

        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Close Windows")
            d(resourceId='com.jingdong.app.mall:id/mu').click()
        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> index  ...  ")
            d(description=u"首页", className="android.view.View").click()

        except Exception as e:
            logger.info(' -> Not Found ....')

    if version_id == '8.1.2':
        try:
            logger.info(' -> Start APP :%s  Version : %s ' % (package_name, version_id))
            d.app_start(package_name)
            logger.info(' -> Done')
            time.sleep(3)
        except Exception as e:
            logger.info(' -> Not Found ....')

        try:
            logger.info(" -> I Know ....")
            d(resourceId='com.jingdong.app.mall:id/bqz').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)
        try:
            logger.info(' -> Start ..')
            d(resourceId='com.jingdong.app.mall:id/c74').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Keep ...")
            d(resourceId='com.jingdong.app.mall:id/ar9').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)
        try:
            logger.info(' -> Agree ....')
            d(resourceId='android:id/button1').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)
        try:
            logger.info(' -> Agree ....')
            d(resourceId='android:id/button1').click()
        except NoSuchElementException as e:
            logger.info(' -> Not Found ....')
        time.sleep(3 * 2)

        try:
            logger.info(" -> Close Windows")
            d(resourceId="com.jingdong.app.mall:id/mw").click()
        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Mine ")
            d(description=u"我的", className="android.view.View").click()
        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Login ...  ")
            d(resourceId="com.jd.lib.personal:id/t3").click()
        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Username ...  ")
            d(resourceId="com.jd.lib.login:id/qj").send_keys(USERNAME)

        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Password ...  ")
            d(resourceId="com.jd.lib.login:id/ql").send_keys(PASSWORD)

        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> login  ...  ")
            d(resourceId="com.jd.lib.login:id/qq").click()

        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> Close Windows")
            d(resourceId='com.jingdong.app.mall:id/mw').click()
        except Exception as e:
            logger.info(' -> Not Found ....')
        time.sleep(3)

        try:
            logger.info(" -> index  ...  ")
            d(description=u"首页", className="android.view.View").click()

        except Exception as e:
            logger.info(' -> Not Found ....')
