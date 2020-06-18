#! /usr/bin/env python3.6
# -*- coding:utf-8 -*-


from PyQt5.QtWidgets import QGraphicsView, QStylePainter, QApplication, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QBrush


class ShowImgView(QGraphicsView):
    zoomInSignal = pyqtSignal()
    zoomOutSignal = pyqtSignal()
    def __init__(self, parent=None):
        super(ShowImgView, self).__init__(parent)
        self.img_item = QGraphicsPixmapItem()
        self.scene = QGraphicsScene(self)
        self.scene.addItem(self.img_item)
        self.setScene(self.scene)
        self.mouse_wheel_speed = 0.2
        self.setBackgroundBrush(QBrush(Qt.white))
        self.setMouseTracking(True)
        self.setRenderHint(QStylePainter.Antialiasing, False)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setOptimizationFlags(QGraphicsView.DontSavePainterState)
        self.setViewportUpdateMode(QGraphicsView.SmartViewportUpdate)

    def wheelEvent(self, event):
        if QApplication.keyboardModifiers() == Qt.ControlModifier:
            cursor_point = event.pos()
            scene_pos = self.mapToScene(QPoint(cursor_point.x(), cursor_point.y()))
            view_width = self.viewport().width()
            view_height = self.viewport().height()
            h_scale = cursor_point.x() / view_width
            v_scale = cursor_point.y() / view_height
            wheel_delta_value = event.angleDelta()
            if wheel_delta_value.y() > 0:
                self.zoomInSignal.emit()
            else:
                self.zoomOutSignal.emit()
            view_point = self.transform().map(scene_pos)
            self.horizontalScrollBar().setValue(int(view_point.x() - view_width * h_scale))
            self.verticalScrollBar().setValue(int(view_point.y() - view_height * v_scale))
        elif QApplication.keyboardModifiers() == Qt.ShiftModifier:
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - event.angleDelta().y()*self.mouse_wheel_speed)
        else:
             self.verticalScrollBar().setValue(self.verticalScrollBar().value() - event.angleDelta().y()*self.mouse_wheel_speed)
        event.accept()
