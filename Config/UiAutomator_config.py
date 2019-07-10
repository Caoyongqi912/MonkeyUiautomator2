import os
import time

import uiautomator2 as u2

from Apps.Pinduoduo import pinduoduo
from Apps.SuNing import suning
from Apps.TouTiao import toutiao
from Apps.TouTiaoSpeed import tt_speed
from Apps.BaiDu import baidu
from Apps.JingDong import jingdong
from Config.DeviceInfo import DeviceInfo
from Config.Setting import get_logger
from Apps.TaoBao import taobao


class Ui:
    def __init__(self, name, device_id, package_name, sleep_time=3):


        self.logger = get_logger(__name__)
        self.device_id = device_id
        self.sleep_time = sleep_time
        self.d = u2.connect_usb(self.device_id)
        self.package_name = package_name
        if name == 'baidu':
            baidu(self.package_name, self.get_version_id(self.package_name), self.d)
        elif name == 'jingdong':
            jingdong(self.package_name, self.get_version_id(self.package_name), self.d)
        elif name == 'taobao':
            taobao(self.package_name, self.get_version_id(self.package_name), self.d)
        elif name == 'pinduoduo':
            pinduoduo(self.package_name, self.get_version_id(self.package_name), self.d)
        elif name == 'suning':
            suning(self.package_name, self.get_version_id(self.package_name), self.d)
        elif name == 'toutiao':
            toutiao(self.package_name, self.get_version_id(self.package_name), self.d)
        elif name == 'toutiaospeed':
            tt_speed(self.package_name, self.get_version_id(self.package_name), self.d)
        else:
            self.logger.info('Not Found App ...')

    def get_version_id(self, package_name):
        version_id = DeviceInfo().get_app_versionName(self.device_id, package_name)
        return version_id


if __name__ == '__main__':
    Ui('suning', '306c9b91', 'com.suning.mobile.ebuy')
