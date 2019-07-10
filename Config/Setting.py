import os
import logging.config





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

USERNAME = '17157428206'
PASSWORD = 'qwertyuiop12345@'




"""
logging配置
"""


# 定义三种日志输出格式 开始

standard_format = '[%(asctime) -s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = PATH('../monkey_log') # log文件的目录

logfile_name = 'SmartTest.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}

logging.config.dictConfig(LOGGING_DIC)


def get_logger(name):
    logger = logging.getLogger(name)
    return logger