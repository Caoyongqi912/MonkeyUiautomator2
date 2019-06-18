import os
import time

import uiautomator2 as u2
from selenium.common.exceptions import NoSuchElementException
from uiautomator2 import UiObjectNotFoundError

from Config.DeviceInfo import DeviceInfo

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

DICT = {
    'baidu': ['com.baidu.searchbox', 'com.baidu.searchbox.MainActivity'],
    'toutiao': ['com.ss.android.article.news', 'com.ss.android.article.news.activity.MainActivity'],
    'toutiaospeed': ['com.ss.android.article.lite', 'com.ss.android.article.lite.activity.MainActivity'],
    'jingdong': ['com.jingdong.app.mall', '.main.MainActivity'],
    'taobao': ['com.taobao.taobao', 'com.taobao.tao.welcome.Welcome'],
    'pinduoduo': ['com.xunmeng.pinduoduo', 'com.xunmeng.pinduoduo.ui.activity.MainFrameActivity'],
    'suning': ['com.suning.mobile.ebuy', 'com.suning.mobile.ebuy.host.MainActivity'],

}

CONTENT_CATCHER = 'com.miui.contentcatcher'
SYSTEM_AD_SOLUTION = 'com.miui.systemAdSolution'

