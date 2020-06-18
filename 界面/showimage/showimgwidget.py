#! /usr/bin/env python3.6
# -*- coding:utf-8 -*-

import math
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QTransform, QPixmapCache, QPixmap, QImage
from showimage.ui.showimgwidget import Ui_ShowImgWidget


class ShowImgWidget(Ui_ShowImgWidget, QWidget):
    def __init__(self, parent=None):
        super(ShowImgWidget, self).__init__(parent)
        self.setupUi(self)
        self.init()

    def init(self):
        self.is_first = True
        self.resetView()
        self.zoom_slider.valueChanged.connect(self.setupMatrix)
        self.graphics_view.zoomInSignal.connect(self.zoomIn)
        self.graphics_view.zoomOutSignal.connect(self.zoomOut)

    def zoomIn(self):
        self.zoom_slider.setValue(self.zoom_slider.value() + 4)

    def zoomOut(self):
        self.zoom_slider.setValue(self.zoom_slider.value() - 4)

    def setupMatrix(self):
        scale = pow(2, (self.zoom_slider.value() - 250) / 50)
        transform = QTransform()
        transform.scale(scale, scale)
        self.graphics_view.setTransform(transform)

    def resetView(self):
        self.zoom_slider.setValue(250)
        self.setupMatrix()
        self.graphics_view.ensureVisible(QRectF(0, 0, 0, 0))

    def showImage(self, path):
        if isinstance(path, str):
            img = QPixmap(path)
        elif isinstance(path, QImage):
            img = QPixmap.fromImage(path, Qt.AutoColor)
        else:
            img = path
        self.graphics_view.img_item.setPixmap(img.scaled(img.width(), img.height()))
        self.compareWithViewAndImage(img.width(), img.height())
        self.setImageCenterOn()
        QPixmapCache.clear()
        self.graphics_view.scene.update()

    def compareWithViewAndImage(self, imgWidth, imageHeight):
        try:
            self.show()
            if self.is_first is True:
                w_scale = float((self.graphics_view.width()-90)/(imgWidth-60))
                h_scale = float((self.graphics_view.height())/(imageHeight-60))
            else:
                w_scale = float((self.graphics_view.width()-90)/(imgWidth))
                h_scale = float((self.graphics_view.height())/(imageHeight))
            if w_scale > 1 and h_scale > 1:
                self.zoom_slider.setValue(250)
            else:
                min_scale = min(w_scale, h_scale)
                self.zoom_slider.setValue(math.log(min_scale, 2)*50+250)
        except:
            pass

    def setImageCenterOn(self):
        max_number_v = self.graphics_view.verticalScrollBar().maximum()
        min_number_v = self.graphics_view.verticalScrollBar().minimum()
        self.graphics_view.verticalScrollBar().setValue((max_number_v + min_number_v) / 2)
        max_number_h = self.graphics_view.horizontalScrollBar().maximum()
        min_number_h = self.graphics_view.horizontalScrollBar().minimum()
        self.graphics_view.horizontalScrollBar().setValue((max_number_h + min_number_h) / 2)

    def resizeEvent(self, QResizeEvent):
        QWidget.resizeEvent(self, QResizeEvent)
        if self.is_first is True:
            self.compareWithViewAndImage(self.graphics_view.width(), self.graphics_view.height())
            self.is_first = False

