import os
import matplotlib.pyplot as plt

from Config.Setting import SYSTEM_AD_SOLUTION, CONTENT_CATCHER, PATH


class Read():
    def __init__(self):
        self.Name_list = os.listdir(PATH('../info_log'))
        for name in self.Name_list:
            with open(name, encoding='utf-8')as f:

                info = [float(x) for x in f.read().split('\n') if x != '']
                self.create_plt(info,name)
                pass

    def create_plt(self, info,name):

        plt.figure(figsize=(30, 16))
        plt.title(name)
        plt.plot(info)
        plt.show()


if __name__ == '__main__':
    Read()
