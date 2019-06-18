import threading
import time
import uiautomator2 as u2
import os
import matplotlib.pyplot as plt
from Config.DeviceInfo import DeviceInfo
from Config.Setting import CONTENT_CATCHER, PATH, SYSTEM_AD_SOLUTION

flag = True
#
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
#

def ui2():
    _cmd = 'adb  push ' + PATH('../MonkeyScript/jingdong') + '  /sdcard/script'
    print(_cmd)
    os.popen(_cmd)
    time.sleep(2)
    d = u2.connect('306c9b91')
    d.app_start('com.taobao.taobao')
    time.sleep(3)
    # d(resourceId='com.jingdong.app.mall:id/bqp').click()
    # time.sleep(3)
    # d(resourceId='com.jingdong.app.mall:id/c6i').click()
    # time.sleep(3)
    # d(resourceId='com.jingdong.app.mall:id/ar2').click()
    # time.sleep(3)
    # d(resourceId='com.xunmeng.pinduoduo:id/b8n').click()
    # time.sleep(3)
    d(resourceId='android:id/button1').click()
    time.sleep(3)
    # d(resourceId='android:id/button1').click()
    # time.sleep(3)
    d(resourceId='com.taobao.taobao:id/yes').click()
    time.sleep(3)
    d(resourceId='android:id/button1').click()
    time.sleep(3)


    cmd = 'adb shell monkey -p com.taobao.taobao   -f /sdcard/script/jingdong  -v -v 100'
    os.popen(cmd)
    time.sleep(500)
    global flag
    flag = False


mem_list = []
mem_list_ADS = []
cpu_list = []


def get_info():
    a = 0
    while True:
        # cpu = DeviceInfo().get_cupinfo('306c9b91', CONTENT_CATCHER)
        mem = DeviceInfo().get_meminfo('306c9b91', CONTENT_CATCHER)
        _cpu = DeviceInfo().get_cupinfo('306c9b91', CONTENT_CATCHER)
        cpu_list.append(_cpu)
        mem_list.append(mem)

        ads = DeviceInfo().get_meminfo('306c9b91', SYSTEM_AD_SOLUTION)
        mem_list_ADS.append(ads)

        # cpu_list.append(cpu)
        time.sleep(2)
        a += 1
        print('----------%d-----------' % a)
        global flag
        if flag == False:
            break

    if flag == False:
        # plt.figure(figsize=(50, 20))
        plt.title(CONTENT_CATCHER)
        plt.ylabel("mem")
        plt.plot(mem_list)
        plt.savefig(PATH('../img/' + CONTENT_CATCHER + '_mem.jpg'))
        plt.show()

        # plt.figure(figsize=(50, 20))
        plt.title("CONTENT_CATCHER")
        plt.ylabel("cpu")
        plt.plot(cpu_list)
        plt.savefig(PATH('../img/' + CONTENT_CATCHER + '_cpu.jpg'))
        plt.show()

        plt.title(SYSTEM_AD_SOLUTION)
        plt.ylabel("mem")
        plt.plot(mem_list_ADS)
        plt.savefig(PATH('../img/' + SYSTEM_AD_SOLUTION + '_mem.jpg'))
        plt.show()


if __name__ == '__main__':
    os.popen('adb kill-server')
    time.sleep(1)
    os.popen('adb start-server')
    time.sleep(5)

    t1 = threading.Thread(target=ui2)
    t2 = threading.Thread(target=get_info)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
