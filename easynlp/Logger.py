# -*- coding: utf-8 -*-
import os
import logging


class Logger(object):
    '''
    @summary:日志处理对象,对logging的封装
    '''

    def __init__(self, name='Logger'):

        self.logger = logging.getLogger(name)

        self.init_logger()

    def init_logger(self):

        self.logger.setLevel(logging.DEBUG)

        # 屏幕输出日志
        stream = logging.StreamHandler()
        stream.setLevel(logging.INFO)
        # 日志样式
        fm_stream = logging.Formatter(
            "[\033[1;%(colorcode)sm%(levelname)s\033[0m   %(asctime)s   %(myfn)s:%(mylno)d:%(myfunc)s%(mymodule)s]   %(message)s",
            "%m-%d %H:%M:%S")
        stream.setFormatter(fm_stream)

        self.logger.addHandler(stream)

    def update_kwargs(self, kwargs, colorcode):
        try:
            fn, lno, func = self.logger.findCaller()
            fn = os.path.basename(fn)
        except Exception as ddd:
            fn, lno, func = "(unknown file)", 0, "(unknown function)"

        if not "extra" in kwargs:
            kwargs["extra"] = {}

        kwargs["extra"]["myfn"] = fn
        kwargs["extra"]["mylno"] = lno
        kwargs["extra"]["myfunc"] = func
        kwargs["extra"]["colorcode"] = colorcode
        kwargs["extra"]["mymodule"] = ""

    def debug(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "0")  # 原色
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "32")  # 绿色
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "33")  # 黄色
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "31")  # 红色
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.update_kwargs(kwargs, "31")  # 红色
        self.logger.critical(msg, *args, **kwargs)


def get_logger():
    '''
    设置日志配置
    '''
    logger = Logger()
    return logger


logger = get_logger()
