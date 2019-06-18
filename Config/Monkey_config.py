import logging.config

import subprocess
import time

from Config.File_config import OperateFile
from Config.log_config import LOGGING_DIC


class Monkey:
    def __init__(self, devices, app_name, package_name, num, path):
        logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的配置
        self.logger = logging.getLogger(__name__)  # 生成一个log实例
        self.devices = devices
        self.app_name = app_name
        self.package_name = package_name
        self.path = path
        self.num = num
        OperateFile(self.path).mkdir_file()
        if self.app_name == 'toutiaospeed' or self.app_name == 'toutiao':

            cmd = 'adb -s {} shell monkey -p {}  -f /sdcard/script/Ms   --throttle 500 --ignore-timeouts --ignore-crashes   --monitor-native-crashes -v -v -v 30 > {}'.format(
                self.devices, self.package_name, self.path)
        else:
            cmd = 'adb -s {} shell monkey -p {}  --throttle 500  --ignore-timeouts --ignore-crashes   --monitor-native-crashes -v -v -v {} > {}'.format(
                self.devices, self.package_name, self.num, self.path
            )
        self.logger.info(f'Running Monkey On {self.package_name} ....')
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def __del__(self):
        while True:
            with open(self.path, encoding='utf-8') as ml:
                time.sleep(5)
                if ml.read().count('Monkey finished') > 0:
                    self.logger.info(f'{self.app_name} Monkey Test Done ..')
                    break
