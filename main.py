import os
import threading
import time
import matplotlib.pyplot as plt
from Config.DeviceInfo import DeviceInfo
from Config.File_config import OperateFile
from Config.Monkey_config import Monkey
from Config.Setting import DICT, CONTENT_CATCHER, SYSTEM_AD_SOLUTION
from Config.UiAutomator_config import Ui
import logging.config
from Config.log_config import LOGGING_DIC

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Main(object):
    def __init__(self, num):

        _cmd = 'python -m uiautomator2 init'
        os.popen(_cmd)
        time.sleep(5)

        logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的配置
        self.logger = logging.getLogger(__name__)  # 生成一个log实例

        self.contentcatcher_mem = []
        self.systemAdSolution_mem = []
        self.catcher_cpu = []
        self.systemAdSolution_cpu = []

        self.num = num
        self.flag = True
        os.popen("adb kill-server")
        os.popen("adb start-server")
        time.sleep(2)
        devices = DeviceInfo().get_devices()

        if devices:
            t1 = threading.Thread(target=self.get_info, name='get_info_Thread', args=devices)
            t2 = threading.Thread(target=self.apps_monkey, name='apps_monkey_Thread', args=devices)
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        else:
            print('No devices!')

    def get_info(self, devices):
        s = 0
        while True:
            cpu_kel = DeviceInfo().get_cupinfo(devices, CONTENT_CATCHER)
            self.catcher_cpu.append(cpu_kel)
            OperateFile(PATH("./info_log/" + devices + '_' + CONTENT_CATCHER + "_cpu.log")).write_txt(str(cpu_kel))
            _cpu_kel = DeviceInfo().get_cupinfo(devices, SYSTEM_AD_SOLUTION)
            self.systemAdSolution_cpu.append(_cpu_kel)
            OperateFile(PATH("./info_log/" + devices + '_' + SYSTEM_AD_SOLUTION + "_cpu.log")).write_txt(str(_cpu_kel))

            mem = DeviceInfo().get_meminfo(devices, CONTENT_CATCHER)
            self.contentcatcher_mem.append(mem)
            OperateFile(PATH("./info_log/" + devices + '_' + CONTENT_CATCHER + "_mem.log")).write_txt(str(mem))
            _mem = DeviceInfo().get_meminfo(devices, SYSTEM_AD_SOLUTION)
            self.systemAdSolution_mem.append(_mem)

            OperateFile(PATH("./info_log/" + devices + '_' + SYSTEM_AD_SOLUTION + "_mem.log")).write_txt(str(_mem))
            time.sleep(5)
            s += 1
            self.logger.info('---------------get info %s 次------------------' % s)
            if self.flag == False:
                self.logger.info('测试结束~')
                break
        time.sleep(5)
        self.plt_write()

    def apps_monkey(self, devices):
        self.adb_push_script(devices)
        time.sleep(2)
        for name, value in DICT.items():
            Ui(name, devices, value[0])
            time.sleep(2)
            # devices, package_name,num  path
            Monkey(devices, name, value[0], self.num, PATH("./monkey_log/" + devices + '_' + value[0] + ".log"))
        self.flag = False

    def adb_push_script(self, devices):
        try:
            _cmd = f' adb -s %s push {PATH("MonkeyScript/Ms")}   /sdcard/script' % devices
            os.popen(_cmd)
            self.logger.info(f'{_cmd} Done!')

        except Exception as e:
            print(' MonkeyScript push ERROR  ')
        time.sleep(1)
        try:
            _cmd = f' adb -s %s push {PATH("MonkeyScript/baidu")}   /sdcard/script' % devices
            os.popen(_cmd)
            self.logger.info(f'{_cmd} Done!')

        except Exception as e:
            print(' MonkeyScript push ERROR  ')

    def plt_write(self):

        plt.figure(figsize=(30, 16))
        plt.title("ContentCatcher_mem")
        plt.ylabel("mem(mb)")
        plt.plot(self.contentcatcher_mem)
        plt.savefig(PATH('img/contentcatcher_mem.jpg'))
        plt.show()

        plt.figure(figsize=(30, 16))
        plt.title("Meminfo")
        plt.ylabel("mem(mb)")
        plt.plot(self.systemAdSolution_mem)
        plt.savefig(PATH('img/systemAdSolution_mem.jpg'))
        plt.show()

        plt.figure(figsize=(30, 16))
        plt.title("catcher_cpu")
        plt.ylabel("Cpu(%)")
        plt.plot(self.catcher_cpu)
        plt.savefig(PATH('img/catcher_cpu.jpg'))
        plt.show()

        plt.figure(figsize=(30, 16))
        plt.title("systemAdSolution_cpu")
        plt.ylabel("Cpu(%)")
        plt.plot(self.catcher_cpu)
        plt.savefig(PATH('img/systemAdSolution_cpu.jpg'))
        plt.show()


if __name__ == '__main__':
    Main(10000)
