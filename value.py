#! /usr/bin/env python3.6
# -*- coding:utf-8 -*-



class Value(object):
    lr_all = 0.00050
    num_epochs_all = 200
    batch_size_all = 16
    VALIDATION_SPLIT_IN = 0.97
    VALIDATION_SPLIT_UP = 0.995
    VALIDATION_SPLIT_KSN = 0.95
    def setlr(self, lr):
        self.lr_all = lr

    def getlr(self):
        return self.lr_all

    def setepochs(self, num_epochs):
        self.num_epochs_all = num_epochs

    def getepochs(self):
        return self.num_epochs_all

    def setbatchsize(self, batch_size):
        self.batch_size_all = batch_size

    def getbatchsize(self):
        return self.batch_size_all

    def setIN(self, IN):
        self.VALIDATION_SPLIT_IN = IN

    def getIN(self):
        return self.VALIDATION_SPLIT_IN


    def setup(self, up):
        self.VALIDATION_SPLIT_UP = up

    def getup(self):
        return self.VALIDATION_SPLIT_UP

    def setksn(self, ksn):
        self.VALIDATION_SPLIT_KSN = ksn

    def getlr(self):
        return self.VALIDATION_SPLIT_KSN