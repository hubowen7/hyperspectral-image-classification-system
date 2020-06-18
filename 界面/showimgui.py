# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showimg.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_showImageDialog(object):
    def setupUi(self, showImageDialog):
        showImageDialog.setObjectName("showImageDialog")
        showImageDialog.resize(1431, 538)
        self.horizontalLayout = QtWidgets.QHBoxLayout(showImageDialog)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(showImageDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = ShowImgWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(showImageDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = ShowImgWidget(self.groupBox_2)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(showImageDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = ShowImgWidget(self.groupBox_3)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(showImageDialog)
        QtCore.QMetaObject.connectSlotsByName(showImageDialog)

    def retranslateUi(self, showImageDialog):
        _translate = QtCore.QCoreApplication.translate
        showImageDialog.setWindowTitle(_translate("showImageDialog", "不同深度学习模型的分类结果图像对比"))
        self.groupBox.setTitle(_translate("showImageDialog", "SSRN"))
        self.groupBox_2.setTitle(_translate("showImageDialog", "FDSSC"))
        self.groupBox_3.setTitle(_translate("showImageDialog", "DBMA"))
from showimage.showimgwidget import ShowImgWidget
