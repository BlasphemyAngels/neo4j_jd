#########################################################################
# File Name: prepare_data.py
# Author: caochenglong
# mail: caochenglong@163.com
# Created Time: 2017-07-24 14:50:43
# Last modified:2017-07-24 15:04:51
#########################################################################
# !/usr/bin/python3
# _*_coding: utf-8_*_

import json


class DataProcessor(object):

    def __init__(self, filename):
        self._filepath = "data/%s" % filename
        self._labels = set()
        self._data

    @property
    def _data(self):
        with open(self._filepath, "r") as f:
            data = json.load(f)
        return data

    def process(self):
        for d in self._data:
            self._labels.add(d['label'])
        print(len(self._labels))


if __name__ == "__main__":
    dp = DataProcessor("data")
    dp.process()
