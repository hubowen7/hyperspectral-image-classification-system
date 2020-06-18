# -*- coding: utf-8 -*-

from showimgui import Ui_showImageDialog
from PyQt5.QtWidgets import QDialog
import os
from showimgui1 import Ui_showImageDialog1


class ShowImage(QDialog, Ui_showImageDialog):
    def __init__(self, name,parent=None):
        super(ShowImage, self).__init__(parent)
        self.setupUi(self)
        self.show()
        path = "..//all_classification_maps"
        ssrn_path = os.path.join(path, name+"_SSRN.png")
        self.widget.showImage(ssrn_path)

        fdssc_path = os.path.join(path, name+"_FDSSC.png")
        self.widget_2.showImage(fdssc_path)

        dbma_path = os.path.join(path, name+"_DBMA.png")
        self.widget_3.showImage(dbma_path)


class ShowImage1(QDialog, Ui_showImageDialog1):
    def __init__(self, name,parent=None):
        super(ShowImage1, self).__init__(parent)
        self.setupUi(self)
        self.resize(700,600)
        self.show()
        path = "..//all_classification_maps"
        img_path = os.path.join(path, name +"_class.jpg")
        self.widget.showImage(img_path)
        self.widget.zoom_slider.setValue(130)
