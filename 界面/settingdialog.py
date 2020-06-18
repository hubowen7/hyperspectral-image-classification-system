#! /usr/bin/env python3.6
# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QDialog, QMessageBox
from dialog import Ui_Dialog
from value import Value


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, alg, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.in_label.setVisible(False)
        self.in_lineedit.setVisible(False)
        self.up_label.setVisible(False)
        self.up_lineedit.setVisible(False)
        self.ksn_label.setVisible(False)
        self.ksn_linedit.setVisible(False)
        self.lr_lineedit.setText(str(Value.lr_all))
        self.epochs_lineedit.setText(str(Value.num_epochs_all))
        self.batch_size_linedit.setText(str(Value.batch_size_all))
        self.alg = alg
        if self.alg == "IN":
            self.in_label.setVisible(True)
            self.in_lineedit.setVisible(True)
            self.in_lineedit.setText(str(Value.VALIDATION_SPLIT_IN))
        elif self.alg == "UP":
            self.up_label.setVisible(True)
            self.up_lineedit.setVisible(True)
            self.up_lineedit.setText(str(Value.VALIDATION_SPLIT_UP))
        elif self.alg == "KSC":
            self.ksn_label.setVisible(True)
            self.ksn_linedit.setVisible(True)
            self.ksn_linedit.setText(str(Value.VALIDATION_SPLIT_KSN))
        self.ok_btn.clicked.connect(self.onOk)


    def onOk(self):
        try:
            Value.lr_all = float(self.lr_lineedit.text())
            Value.num_epochs_all = int(float(self.epochs_lineedit.text()))
            Value.batch_size_all = int(float(self.batch_size_linedit.text()))
            if self.alg == "IN":
                Value.VALIDATION_SPLIT_IN = float(self.in_lineedit.text())
            elif self.alg == "UP":
                Value.VALIDATION_SPLIT_UP = float(self.up_lineedit.text())
            elif self.alg == "KSC":
                Value.VALIDATION_SPLIT_KSN = float(self.ksn_linedit.text())
            QMessageBox.information(self, "提示", "设置成功", QMessageBox.Yes, QMessageBox.Yes)
        except:
            QMessageBox.critical(self, "错误", "有输入不是数值类型")