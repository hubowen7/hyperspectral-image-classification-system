# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showimgwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowImgWidget(object):
    def setupUi(self, ShowImgWidget):
        ShowImgWidget.setObjectName("ShowImgWidget")
        ShowImgWidget.resize(827, 739)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShowImgWidget)
        self.verticalLayout.setContentsMargins(11, 5, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphics_view = ShowImgView(ShowImgWidget)
        self.graphics_view.setObjectName("graphics_view")
        self.horizontalLayout_2.addWidget(self.graphics_view)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.zoom_slider = QtWidgets.QSlider(ShowImgWidget)
        self.zoom_slider.setMaximum(500)
        self.zoom_slider.setSingleStep(10)
        self.zoom_slider.setProperty("value", 250)
        self.zoom_slider.setOrientation(QtCore.Qt.Vertical)
        self.zoom_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.zoom_slider.setObjectName("zoom_slider")
        self.verticalLayout_2.addWidget(self.zoom_slider)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ShowImgWidget)
        QtCore.QMetaObject.connectSlotsByName(ShowImgWidget)

    def retranslateUi(self, ShowImgWidget):
        _translate = QtCore.QCoreApplication.translate
        ShowImgWidget.setWindowTitle(_translate("ShowImgWidget", "ShowImgWidget"))
from ..showimgview import ShowImgView
