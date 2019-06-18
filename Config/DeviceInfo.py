import os
import re
import subprocess
from wsgiref.validate import validator


class DeviceInfo:
    '''
    获取手机信息
    '''

    def __init__(self):
        pass

    def getDeviceId(self):
        '''
          获取ID
        :return: 字符串
        '''
        cmd = "adb devices | grep device | sed '1d' | awk '{print $1}'"
        device_id = os.popen(cmd).read()
        # print("device_id: %s" % device_id)
        return device_id

    def get_devices(self):
        """
        获取ID
        :return:  ID 列表
        """
        _cmd = 'adb devices'
        devices = os.popen(_cmd).read()
        devices = devices.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]

    def getAndroidVersion(self, device_id):
        cmd = "adb -s %s shell getprop ro.build.version.release" % device_id
        android_version = os.popen(cmd).read().strip()
        # print("android_version: %s" % android_version)
        return android_version

    def get_Mobile_Type(self, device_id):
        """

        :param device_id: device_id
        :return:   mobile_type like: MI 8
        """
        cmd = "adb -s %s shell getprop ro.product.model" % device_id
        mobile_type = os.popen(cmd).read().strip()
        # print("mobile_type: %s" % mobile_type)
        return mobile_type

    def get_Miui_Version(self, device_id):
        """

        :param device_id: device_id
        :return: miui_version  like:9.5.27
        """
        cmd = "adb -s %s shell getprop ro.build.version.incremental" % device_id
        miui_version = os.popen(cmd).read().strip()

        # print("miui_version: %s" % miui_version)
        return miui_version

    def get_current_package_name(self, device_id):
        """

        :param device_id: device_id
        :return: 返回正在运行的程序 list[name activity]
        """
        _cmd = "adb -s %s shell dumpsys window w | grep \/ | grep name=" % device_id
        pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
        out = os.popen(_cmd).read()
        package_name = pattern.findall(out)[0].split("/")[0]
        package_name_activity = pattern.findall(out)[0].split("/")[1]
        current_app = []
        current_app.append(package_name)
        current_app.append(package_name_activity)
        print(current_app)
        return current_app

    def get_meminfo(self, devices_id, package_name):
        """

        :param devices_id: devices_id
        :param package_name: package_name
        :return: mem_size   like:364.91mb
        """
        cmd = 'adb -s %s shell dumpsys meminfo %s' % (devices_id, package_name)
        me = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        mem = ''.join([x.decode() for x in me])
        pattern = re.compile(r'TOTAL\s+\d+')
        mem_size = float(pattern.findall(mem)[0].split(' ')[-1]) / 1024
        # mem_size =float('%.2f'%mem_size)
        # print('进程名称：%s' % package_name)
        # print("内存占用：%s " % mem_size)
        return mem_size

    def get_battery(self, device_id):
        """

        :param device_id: device_id
        :return: battery_status   like:100
        """
        try:
            cmd = "adb -s %s shell dumpsys battery" % device_id
            output = os.popen(cmd).read()
            battery = float(re.findall("level:.(\d+)*", output, re.S)[0])
            print(battery)
        except:
            battery = 90
            print(battery)
        # writeInfo(battery2, PATH("../info/" + devices + "_battery.pickle"))

        return battery

    def get_cupinfo(self, device_id, package_name):
        """

        :param device_id: device_id
        :param package_name: package_name
        :return: CPU佔用：16%
        """
        cmd = 'adb -s %s shell dumpsys cpuinfo | grep %s' % (device_id, package_name)
        cpu_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        try:
            cpu_info = float(cpu_info[0].decode().split(' ')[2].replace('%', ''))
            # print('进程名称:%s' % package_name)
            # print('CPU佔用：%s' % cpu_info)
            return cpu_info
        except IndexError as e:
            cpu_info = 0
            return cpu_info

    def get_fps(self, device_id, package_name):
        """

        :param device_id:
        :param package_name:
        :return: 60
        """
        _adb = "adb -s %s shell dumpsys gfxinfo %s" % (device_id, package_name)
        results = os.popen(_adb).read().strip()
        frames = [x for x in results.split('\n') if validator(x)]
        frame_count = len(frames)
        jank_count = 0
        vsync_overtime = 0
        render_time = 0
        for frame in frames:
            time_block = re.split(r'\s+', frame.strip())
            if len(time_block) == 3:
                try:
                    render_time = float(time_block[0]) + float(time_block[1]) + float(time_block[2])
                except Exception as e:
                    render_time = 0
            '''
            当渲染时间大于16.67，按照垂直同步机制，该帧就已经渲染超时
            那么，如果它正好是16.67的整数倍，比如66.68，则它花费了4个垂直同步脉冲，减去本身需要一个，则超时3个
            如果它不是16.67的整数倍，比如67，那么它花费的垂直同步脉冲应向上取整，即5个，减去本身需要一个，即超时4个，可直接算向下取整

            最后的计算方法思路：
            执行一次命令，总共收集到了m帧（理想情况下m=128），但是这m帧里面有些帧渲染超过了16.67毫秒，算一次jank，一旦jank，
            需要用掉额外的垂直同步脉冲。其他的就算没有超过16.67，也按一个脉冲时间来算（理想情况下，一个脉冲就可以渲染完一帧）

            所以FPS的算法可以变为：
            m / （m + 额外的垂直同步脉冲） * 60
            '''
            if render_time > 16.67:
                jank_count += 1
                if render_time % 16.67 == 0:
                    vsync_overtime += int(render_time / 16.67) - 1
                else:
                    vsync_overtime += int(render_time / 16.67)

        _fps = int(frame_count * 60 / (frame_count + vsync_overtime))
        # writeInfo(_fps, PATH("../info/" + devices + "_fps.pickle"))

        # return (frame_count, jank_count, fps)
        return _fps

    def get_pid(self, device_id, package_name):
        """

        :param device_id: device_id
        :param package_name: package_name
        :return: 进程PID like:6974
        """
        cmd = "adb -s %s  shell ps | grep %s" % (device_id, package_name)
        pid = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE).stdout.readlines()
        for item in pid:
            if item.split()[8].decode() == package_name:
                # print(item.split()[1].decode())
                return item.split()[1].decode()

    def reboot(self, device_id):
        """

        :param device_id: device_id
        :return:
        """
        cmd = 'adb -s {} reboot'.format(device_id)
        os.popen(cmd)

    def get_app_pix(self, device_id):
        """
        手机分辨率
        Physical size ：物理尺寸
        Override size : 覆盖尺寸
        :param device_id: device_id
        :return: dict    {'Physical size': '1080x2158', 'Override size': '1080x2248'}
        """
        cmd = "adb -s {} shell wm size".format(device_id)
        info = os.popen(cmd).read()
        size = info.split()[-1]
        return size

    def get_CPU_kel(self, device_id):
        """
        手机核数
        :param device_id: device_id
        :return: 8核
        """
        cmd = "adb -s {} shell cat /proc/cpuinfo".format(device_id)
        output = os.popen(cmd).read()
        # print(str(len(re.findall("processor", output))) + "核")
        return str(len(re.findall("processor", output))) + "核"

    def get_men_total(self, device_id):
        """
        总内存
        :param device_id: device_id
        :return:  str 5632.09mb

        """
        cmd = "adb -s {}  shell cat /proc/meminfo".format(device_id)
        output = os.popen(cmd).read()
        MemTotal = str('%.2f' % (float(re.findall('MemTotal:(\s+)(\d+)', output, re.S)[0][-1]) / 1024)) + 'mb'
        # print(MemTotal)
        return MemTotal

    def get_app_versionName(self, device_id, package_name):
        """
        获取APP版本号
        :param device_id: device_id
        :param package_name: package_name
        :return:  like:  7.2.6
        """
        cmd = 'adb -s {} shell pm dump {} | grep versionName'.format(device_id, package_name)
        vname = os.popen(cmd).read().split(' ')[-1].strip().split('=')[-1]
        # print(vname,type(vname))
        return vname

    def kill_app(self, pid):

        cmd = 'adb shell kill -9 {}'.format(pid)
        os.popen(cmd)


# if __name__ == '__main__':
    # DeviceInfo().getDeviceId()
    #     # DeviceInfo().get_devices()
    #     # 306c9b91
    #     DeviceInfo().get_Mobile_Type('306c9b91')
    #     # DeviceInfo().getMiuiVersion('306c9b91')
    #     DeviceInfo().get_current_package_name('306c9b91')
    #     # DeviceInfo().get_meminfo('306c9b91','com.ss.android.article.news')
    #     # DeviceInfo().get_battery('306c9b91')
    #     DeviceInfo().get_cupinfo('306c9b91', 'com.miui.contentcatcher')
    #     # DeviceInfo().get_fps('306c9b91', 'com.ss.android.article.news')
    #     # DeviceInfo().get_pid('306c9b91', 'com.ss.android.article.news')
    #     # DeviceInfo().get_app_pix('306c9b91')
    #     # DeviceInfo().get_CPU_kel('306c9b91')
    #     # DeviceInfo().get_men_total('306c9b91')
    #     DeviceInfo().get_app_versionName('306c9b91','com.ss.android.article.news')
    #     DeviceInfo().kill_app('306c9b91','com.Ms.searchbox')
    # if __name__ == '__main__':
    # DeviceInfo().get_cupinfo('306c9b91', 'com.jingdong.app.mall')
    # DeviceInfo().get_meminfo('306c9b91', 'com.jingdong.app.mall')
