# -*- coding: utf-8 -*-
import os, re
import sys
sys.path.append('../CDCNN/')
sys.path.append('../DBDA/')
sys.path.append('../DBMA/')
sys.path.append('../FDSSC/')
sys.path.append('../SSRN/')
import time
from timeit import default_timer as timer


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CDCNN_main import *
from DBMA_main import *
from DBDA_main import *
from FDSSC_main import *
from SSRN_main import *
from showimg import ShowImage
from showimg import ShowImage1
a = "gui"  #ui文件名,没有后缀a =?
# ui自动改成py,
os.system(r"C:\Python37\python.exe -m PyQt5.uic.pyuic {0}.ui -o {0}.py".format(a))
from gui import *
from settingdialog import Dialog
#线程1:图片
class Thread_1(QThread):  # 线程1,不用这个界面会卡死.结果用信号传给主界面
    _signal = pyqtSignal()#结束后输出的结果类型,不能错._signal = pyqtSignal(?).不返回不写

    def run(self):
        t1 = time.time()
        mainWindow.statusbar.showMessage("---运行中---")
        choose = mainWindow.comboBox_2.currentText()
        if choose=="CDCNN":
            mainWindow.cdcnn_run()
        elif choose=="DBDA":
            mainWindow.dbda_run()
        elif choose=="DBMA":
            mainWindow.dbma_run()
        elif choose=="FDSSC":
            mainWindow.fdssc_run()
        elif choose=="SSRN":
            mainWindow.ssrn_run()
        t2 = time.time()
        mainWindow.statusbar.showMessage("---分析结束,用时{}s---".format(t2 - t1))
        self._signal.emit()
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow,Cdcnn,Dbda,Fdssc,Ssrn,Dbma):  # 参数1对应ui窗口类型.参数2对应QtDesigner生成的文件第一个class名字.默认是Ui_Form或Ui_MainWindow
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('高光谱图像处理系统')
        self.setStyleSheet("#MainWindow{border-image:url(./子窗口背景图.jpg);}")
        #图标
        self.setWindowIcon(QIcon("下载.jpg"))
        # 写信号槽
        self.pushButton.clicked.connect(self.save)  # 选择保存地址
        self.pushButton_start.clicked.connect(self.thread_1fun)  # 开始运行
        self.setting_btn.clicked.connect(self.onSetting)


    def onSetting(self):
        dialog = Dialog(self.comboBox_1.currentText())
        dialog.exec_()


    # 以下是信号槽连接的函数们
    # 1图片识别
    def thread_1fun(self):
        #1.1进入线程
        self.sender1 = self.sender()
        self.sender1.setEnabled(False)
        self.thread_1 = Thread_1()
        self.thread_1.start()
        self.thread_1._signal.connect(self.thread_1result)
        self.input = "{0}/{1}_gt.png".format('../all_classification_maps/',self.comboBox_1.currentText())
        self.img = QImage(self.input)
        # self.choose_2 = self.comboBox_1.currentText()

       # self.label_6.setPixmap(QPixmap(self.input))
        self.widget.showImage(self.img)

        # if self.choose_2 == 'IN':
        #     self.result = self.img.scaled(300, 300, Qt.IgnoreAspectRatio,
        #                                   Qt.SmoothTransformation)
        #     #self.label_6.setPixmap(QPixmap(self.result))
        #     self.widget.showImage(self.result)
        #
        # # if self.choose_2 == 'SV':
        # #     self.result = self.img.scaled(100, 300, Qt.IgnoreAspectRatio,
        # #                                   Qt.SmoothTransformation)
        # #     self.label_6.setPixmap(QPixmap(self.result))
        # # if self.choose_2 == 'KSC':
        #     self.result = self.img.scaled(300, 300, Qt.IgnoreAspectRatio,
        #                                       Qt.SmoothTransformation)
        #     #self.label_6.setPixmap(QPixmap(self.result))
        #     self.widget.showImage(self.result)
        #
        # if self.choose_2 == 'BS':
        #     self.result = self.img.scaled(50, 300, Qt.IgnoreAspectRatio,
        #                                       Qt.SmoothTransformation)
        #    # self.label_6.setPixmap(QPixmap(self.result))
        #     self.widget.showImage(self.result)
        #
        #     self.widget.showImage(self.input)
        # if self.choose_2 == 'UP':
        #     self.result = self.img.scaled(130, 300, Qt.IgnoreAspectRatio,
        #                                       Qt.SmoothTransformation)
        #     #self.label_6.setPixmap(QPixmap(self.result))
        #     self.widget.showImage(self.result)


        # 拉伸
        # self.label_6.setScaledContents(True)
    def thread_1result(self):
        #1.2线程结果
        self.sender1.setEnabled(True)
        # 显示结果图片
        if self.comboBox_2.currentText()=="DBDA":
            name="DBDA_MISH"
        else:
            name =self.comboBox_2.currentText()
        self.out = "{0}/{1}_{2}.png".format(self.lineEdit.text(), self.comboBox_1.currentText(),name)
        self.img = QImage(self.out)
        # self.choose_3 = self.comboBox_1.currentText()
        #self.label_7.setPixmap(QPixmap(self.out))
        self.widget_2.showImage(self.out)

        # if self.choose_3 == 'IN':
        #     self.result = self.img.scaled(300, 300, Qt.IgnoreAspectRatio,
        #                                   Qt.SmoothTransformation)
        #     #self.label_7.setPixmap(QPixmap(self.result))
        #     self.widget_2.showImage(self.result)
        # if self.choose_3 == 'KSC':
        #     self.result = self.img.scaled(300, 300, Qt.IgnoreAspectRatio,
        #                                       Qt.SmoothTransformation)
        #     #self.label_7.setPixmap(QPixmap(self.result))
        #     self.widget_2.showImage(self.result)
        # if self.choose_3 == 'BS':
        #     self.result = self.img.scaled(50, 300, Qt.IgnoreAspectRatio,
        #                                       Qt.SmoothTransformation)
        #     #self.label_7.setPixmap(QPixmap(self.result))
        #     self.widget_2.showImage(self.result)
        # if self.choose_3 == 'UP':
        #     self.result = self.img.scaled(130, 300, Qt.IgnoreAspectRatio,
        #                                       Qt.SmoothTransformation)
        #     #self.label_7.setPixmap(QPixmap(self.result))
        #     self.widget_2.showImage(self.result)
        # 拉伸
        # self.label_7.setScaledContents(True)


        value = self.comboBox_1.currentText()
        dialog = ShowImage(value)
        dialog.show()
        dialog1 = ShowImage1(value)
        dialog1.exec()
        self.thread_1.wait()
        self.thread_1.quit()

    def save(self):
        self.directory = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "../")

        self.lineEdit.setText(self.directory)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


