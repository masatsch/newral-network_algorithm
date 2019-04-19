import numpy as np


class Dropout:
    def __init__(self, dropout_raito=0.5):
        self.dropout_ratio = dropout_raito
        self.mask = None

    def forward(self, x, train_flg=True):
        if train_flg:
            self.mask = np.random.rand(*x.shape) > self.dropout_ratio
            return x * self.mask

    def backward(self, dout):
        return dout * self.mask
