#coding=utf-8

import sys

class MyTushare(object):

    __version = '0.1.0'

    def run(self):
        method = sys.argv[1]

        if hasattr(self, method):
            method = getattr(self, method)
            method()
        else:
            self.help()

    def version(self):
        print(self.__version)

    def help(self):
        print('help')
        # print(dir(self))
        print(self.__list_all_member())

    def stock_basic(self):
        print('stock_basic')
        import lib.my_tushare.tushare.stock_basic

    def __list_all_member(self):
        for name in dir(self):
            print(name)





