import logging.config
import time

import uiautomator2 as u2
from selenium.common.exceptions import NoSuchElementException
from uiautomator2 import UiObjectNotFoundError

from Config.DeviceInfo import DeviceInfo
from Config.log_config import LOGGING_DIC


class Ui:
    def __init__(self, name, device_id, package_name, sleep_time=3):
        logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的配置
        self.logger = logging.getLogger(__name__)  # 生成一个log实例
        self.device_id = device_id
        self.sleep_time = sleep_time
        self.d = u2.connect_usb(self.device_id)
        self.package_name = package_name
        if name == 'baidu':
            self.baidu()
        elif name == 'jingdong':
            self.jingdong()
        elif name == 'taobao':
            self.taobao()
        elif name == 'pinduoduo':
            self.pin_dd()
        elif name == 'suning':
            self.suning()
        elif name == 'toutiao':
            self.toutiao()
        elif name == 'toutiaospeed':
            self.tt_speed()
        else:
            self.logger.info('Not Found App ...')

    def tt_speed(self):
        version_id = self.get_version_id('com.ss.android.article.lite')
        if version_id == '6.9.5' or version_id == '6.9.2' or version_id == '6.9.6':
            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                pass
            try:
                self.logger.info(' -> Agree ....')
                self.d(resourceId='android:id/button1').click()
                time.sleep(self.sleep_time)
                self.logger.info(' -> Done')
            except  NoSuchElementException as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Close window ....')
                self.d(resourceId='com.ss.android.article.lite:id/z0').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except NoSuchElementException as e:
                self.logger.info(' -> Not Found ....')

    def toutiao(self):
        version_id = self.get_version_id('com.ss.android.article.news')
        if version_id == '7.2.9':
            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> I Know ....')
                self.d(resourceId='com.ss.android.article.news:id/a4u').click()
                time.sleep(self.sleep_time)
                self.logger.info(' -> Done')
            except NoSuchElementException as  e:
                self.logger.info(' -> Not Found ....')


        elif version_id == '7.2.7':
            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> I Know ....')
                self.d(resourceId='com.ss.android.article.news:id/a4r').click()
                time.sleep(self.sleep_time)
                self.logger.info(' -> Done')
            except NoSuchElementException as  e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> I Agree ....')
                self.d(resourceId='android:id/button1').click()
                time.sleep(6)
                self.logger.info(' -> Done')
            except NoSuchElementException as  e:
                self.logger.info(' -> Not Found ....')
        elif version_id == '7.4.2':
            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> I Know ....')
                self.d(resourceId='com.ss.android.article.news:id/a4j').click()
                time.sleep(self.sleep_time)
                self.logger.info(' -> Done')
            except NoSuchElementException as  e:
                self.logger.info(' -> Not Found ....')

    def suning(self):
        version_id = self.get_version_id('com.suning.mobile.ebuy')
        if version_id == '7.7.3':
            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='com.suning.mobile.ebuy:id/positive').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except NoSuchElementException as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except NoSuchElementException as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except NoSuchElementException as e:
                self.logger.info(' -> Not Found ....')

    def pin_dd(self):
        version_id = self.get_version_id('com.xunmeng.pinduoduo')
        if version_id == '4.59.0':

            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Ok .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/b7k').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')
            try:
                self.logger.info(' -> Wechat .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/ac0').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Close Windows .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/m_').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

        elif version_id == '4.58.0':
            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Ok .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/b5j').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Jump .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/b80').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except NoSuchElementException as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Close Windows .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/m_').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')
        elif version_id == '4.60.0':
            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Ok .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/b8n').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')
            try:
                self.logger.info(' -> Wechat .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/acw').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Close Windows .....')
                self.d(resourceId='com.xunmeng.pinduoduo:id/mg').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

    def baidu(self):
        version_id = self.get_version_id('com.baidu.searchbox')
        self.logger.info(self.package_name)
        if version_id == '11.9.0.11' or version_id == '11.8.0.10' or version_id == '11.10.0.12':

            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Agree and continue ..... ')
                self.d(resourceId='com.baidu.searchbox:id/positive_button').click()
                self.logger.info(' -> Done .....')
                time.sleep(3)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(' -> Agree One ...')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(3)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')
            try:
                self.logger.info(' -> Agree Permission ...')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(3)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')
            try:
                self.logger.info(' -> Agree Local ...')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(3)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')
            try:
                self.logger.info(' -> Not Update ...')
                self.d(resourceId='com.baidu.searchbox:id/update_close').click()
                self.logger.info(' -> Done')
                time.sleep(3)
            except UiObjectNotFoundError as e:
                self.logger.info(' -> Not Found ....')
            self.logger.info(" -> Done ...")

    def taobao(self):
        version_id = self.get_version_id('com.taobao.taobao')
        if version_id == '8.8.0':

            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')
            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')
            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='com.taobao.taobao:id/yes').click()
                self.logger.info(' -> Done')
                time.sleep(5)
            except Exception as e:
                self.logger.info(' -> Not Found ....')
            try:
                self.logger.info(' -> Agree .....')
                self.d(resourceId='android:id/button1').click()
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')
            self.d.app_stop(self.package_name)

    def jingdong(self):
        version_id = self.get_version_id('com.jingdong.app.mall')
        if version_id == '8.1.0':
            try:
                self.logger.info(' -> Start APP :%s  Version : %s ' % (self.package_name, version_id))
                self.d.app_start(self.package_name)
                self.logger.info(' -> Done')
                time.sleep(self.sleep_time)
            except Exception as e:
                self.logger.info(' -> Not Found ....')

            try:
                self.logger.info(" -> I Know ....")
                self.d(resourceId='com.jingdong.app.mall:id/bqp').click()
            except NoSuchElementException as baidug:
                self.logger.info("Error: %s" % baidug)
            time.sleep(self.sleep_time)
            try:
                self.logger.info(' -> Start ..')
                self.d(resourceId='com.jingdong.app.mall:id/c6i').click()
            except NoSuchElementException as baidug:
                self.logger.info(' -> Not Found ....')
            time.sleep(self.sleep_time)

            try:
                self.logger.info(" -> Keep ...")
                self.d(resourceId='com.jingdong.app.mall:id/ar2').click()
            except NoSuchElementException as baidug:
                self.logger.info(' -> Not Found ....')
            time.sleep(self.sleep_time)
            try:
                self.logger.info(' -> Agree ....')
                self.d(resourceId='android:id/button1').click()
            except NoSuchElementException as baidug:
                self.logger.info(' -> Not Found ....')
            time.sleep(self.sleep_time)
            try:
                self.logger.info(' -> Agree ....')
                self.d(resourceId='android:id/button1').click()
            except NoSuchElementException as baidug:
                self.logger.info(' -> Not Found ....')
            time.sleep(self.sleep_time * 2)
            try:
                self.logger.info(" -> Close Windows")
                self.d(resourceId='com.jingdong.app.mall:id/mu').click()
            except Exception as baidug:
                self.logger.info(' -> Not Found ....')

    def get_version_id(self, package_name):
        version_id = DeviceInfo().get_app_versionName(self.device_id, package_name)
        return version_id
