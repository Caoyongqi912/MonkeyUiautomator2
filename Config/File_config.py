import logging.config
import os

from Config.DeviceInfo import DeviceInfo
from Config.Setting import PATH
from Config.log_config import LOGGING_DIC

'''
操作文件
'''


class OperateFile:
    # method(r,w,a)

    def __init__(self, file, method='a'):
        logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的配置
        self.logger = logging.getLogger(__name__)  # 生成一个log实例
        self.file = file
        self.method = method
        self.fileHandle = None

    def write_txt(self, line):
        OperateFile(self.file).check_file()
        self.fileHandle = open(self.file, self.method)
        self.fileHandle.write(line + "\n")
        self.fileHandle.close()

    def read_txt_row(self):
        resutl = ""
        if OperateFile(self.file).check_file():
            self.fileHandle = open(self.file, self.method)
            resutl = self.fileHandle.readline()
            self.fileHandle.close()
        return resutl

    def read_txt_rows(self):
        if OperateFile(self.file).check_file():
            self.fileHandle = open(self.file, self.method)
            file_list = self.fileHandle.readlines()
            for i in file_list:
                self.logger.info(i.strip("\n"))
            self.fileHandle.close()

    def check_file(self):
        if not os.path.isfile(self.file):
            # self.mkdir_file()
            # self.logger.info('文件不存在' + self.file)
            # sys.exit()
            return False
        else:
            return True
        # self.logger.info("文件存在！")

    def mkdir_file(self):
        if not os.path.isfile(self.file):
            f = open(self.file, self.method)
            f.close()
            self.logger.info("创建文件成功")
        else:
            self.logger.info("文件已经存在")

    def remove_file(self):
        if os.path.isfile(self.file):
            os.remove(self.file)
            self.logger.info("删除文件成功")
        else:
            self.logger.info("文件不存在")

#
# if __name__ == '__main__':
#     OperateFile(PATH('test.txt')).write_txt(123)