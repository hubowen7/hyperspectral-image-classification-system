# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showimg1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_showImageDialog1(object):
    def setupUi(self, showImageDialog1):
        showImageDialog1.setObjectName("showImageDialog1")
        showImageDialog1.resize(516, 419)
        self.horizontalLayout = QtWidgets.QHBoxLayout(showImageDialog1)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(showImageDialog1)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = ShowImgWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(showImageDialog1)
        QtCore.QMetaObject.connectSlotsByName(showImageDialog1)

    def retranslateUi(self, showImageDialog1):
        _translate = QtCore.QCoreApplication.translate
        showImageDialog1.setWindowTitle(_translate("showImageDialog1", "不同深度学习模型的分类结果评价指标图像对比"))
from showimage.showimgwidget import ShowImgWidget
