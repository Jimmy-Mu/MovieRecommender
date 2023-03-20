# load：         加载数据集并进行预处理
# function:      训练和推荐需要用到的函数
# train:         训练网络
# recommender:   电影推荐
# show：         pyqt做的UI界面
# main：         主函数


import sys
from show import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = show_window()
    sys.exit(app.exec_()) 