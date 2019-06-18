import time

from selenium.common.exceptions import NoSuchElementException

from Config.DeviceInfo import DeviceInfo
from appium import webdriver
import os
import subprocess


class AppiumOperation():
    def __init__(self):
        pass

    def start_appium(self):
        try:
            cmd = 'nohup /home/mi/Appium/Appium-linux-1.13.0.AppImage > a.info_log 2>&1&'
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        except Exception as msg:
            errormsg = str(msg)
            return errormsg

    def stop_appium(self):
        end_appium_cmd = "ps -ef |grep appium |grep -v grep |awk '{print $2}' |xargs kill -9"
        os.popen(end_appium_cmd)


class Appium_config:
    def __init__(self, name, device_id, appPackage, appActivity, sleep_time=3):
        # AppiumOperation().start_appium()
        # time.sleep(3)
        # print(' -> Appium Server Start ....')

        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = DeviceInfo().getAndroidVersion(device_id)
        self.desired_caps['deviceName'] = 'Android Emulator'
        self.desired_caps['appPackage'] = appPackage
        self.desired_caps['noReset'] = True
        self.desired_caps['appActivity'] = appActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.sleep_time = sleep_time
        print(self.desired_caps)
        print(' -> appName     :%s is running .....' % self.desired_caps['appPackage'])
        print(' -> appActivity :%s  ' % self.desired_caps['appActivity'])
        time.sleep(self.sleep_time)

        if name == 'Ms':
            self.baidu()
        elif name == 'jingdong':
            self.jingdong()
        elif name == 'taobao':
            self.taobao()
        elif name == 'pinduoduo':
            self.piin_dd()
        elif name == 'suning':
            self.suning()
        elif name == 'toutiao':
            self.toutiao()
        elif name == 'toutiaospeed':
            self.tt_speed()
        else:
            print('Not Found App ...')

    def baidu(self):
        try:
            print(' -> Agree and continue ..... ')
            self.driver.find_element_by_id('com.Ms.searchbox:id/positive_button').click()
            print(' -> Done .....')
            time.sleep(3)
        except NoSuchElementException as e:
            print(' -> ', e)
        try:
            print(' -> Agree One ...')
            self.driver.find_element_by_id('android:id/button1').click()
            print(' -> Done')
            time.sleep(3)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Agree Permission ...')
            self.driver.find_element_by_id('android:id/button1').click()
            print(' -> Done')
            time.sleep(3)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Agree Local ...')
            self.driver.find_element_by_id('android:id/button1').click()
            print(' -> Done')
            time.sleep(3)
        except NoSuchElementException as e:
            print(' -> ', e)

        print(" -> Done ...")

    def tt_speed(self):
        try:
            print(' -> Agree ....')
            self.driver.find_element_by_id('android:id/button1').click()
            time.sleep(self.sleep_time)
            print(' -> Done')
        except  NoSuchElementException as e:
            print(' -> Not Found ....')

        try:
            print(' -> Close window ....')
            self.driver.find_element_by_id('com.ss.android.article.lite:id/z0').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> Not Found ....')

    def toutiao(self):

        try:
            print(' -> I Know ....')
            self.driver.find_element_by_id('com.ss.android.article.news:id/a4j').click()
            time.sleep(5)
            print(' -> Done')
        except NoSuchElementException as  e:
            print(e)

    def taobao(self):
        try:
            print(' -> Agree .....')
            self.driver.find_element_by_id('android:id/button1').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Agree .....')
            self.driver.find_element_by_id('com.taobao.taobao:id/yes').click()
            print(' -> Done')
            time.sleep(5)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Agree .....')
            self.driver.find_element_by_id('android:id/button1').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

    def suning(self):

        try:
            print(' -> Agree .....')
            self.driver.find_element_by_id('com.suning.mobile.ebuy:id/positive').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Agree .....')
            self.driver.find_element_by_id('android:id/button1').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Agree .....')
            self.driver.find_element_by_id('android:id/button1').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

    def piin_dd(self):

        try:
            print(' -> Ok .....')
            self.driver.find_element_by_id('com.xunmeng.pinduoduo:id/b5j').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Agree .....')
            self.driver.find_element_by_id('android:id/button1').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Jump .....')
            self.driver.find_element_by_id('com.xunmeng.pinduoduo:id/b80').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

        try:
            print(' -> Close Windows .....')
            self.driver.find_element_by_id('com.xunmeng.pinduoduo:id/m_').click()
            print(' -> Done')
            time.sleep(self.sleep_time)
        except NoSuchElementException as e:
            print(' -> ', e)

    def jingdong(self):

        try:
            print(" -> I Know ....")
            self.driver.find_element_by_id("com.jingdong.app.mall:id/bqi").click()
        except NoSuchElementException as msg:
            print("Error: %s" % msg)
        time.sleep(self.sleep_time)
        try:
            print(' -> Start ..')
            self.driver.find_element_by_id("com.jingdong.app.mall:id/c61").click()
        except NoSuchElementException as msg:
            print("Error: %s" % msg)
        time.sleep(self.sleep_time)

        try:
            print(" -> Keep ...")
            self.driver.find_element_by_id("com.jingdong.app.mall:id/aqu").click()
        except NoSuchElementException as msg:
            print("Error: %s" % msg)
        time.sleep(self.sleep_time)
        try:
            print(' -> Agree ....')
            self.driver.find_element_by_id("android:id/button1").click()
        except NoSuchElementException as msg:
            print("Error: %s" % msg)
        time.sleep(self.sleep_time)
        try:
            print(' -> Agree ....')
            self.driver.find_element_by_id("android:id/button1").click()
        except NoSuchElementException as msg:
            print("Error: %s" % msg)
        time.sleep(self.sleep_time * 2)
        try:
            print(" -> Close Windows")
            self.driver.find_element_by_id("com.jingdong.app.mall:id/mn").click()
        except Exception as msg:
            print("msg: %s" % msg)
