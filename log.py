#!/usr/bin/env python
#coding:utf-8
import logging
import curses

class PrettyFormatter(logging.Formatter):
    DEFAULT_FMT = '%(color)s[%(levelname)s %(asctime)s '\
        '%(module)s:%(lineno)d]%(end_color)s %(message)s'
    DEFAULT_DATEFMT = '%Y%m%d %H:%M:%S'
    DEFAULT_COLORS = {logging.DEBUG:4, logging.INFO:2, 
                      logging.WARNING:3, logging.ERROR:1}

    def __init__(self, fmt=DEFAULT_FMT, datefmt=DEFAULT_DATEFMT, 
                 colors=DEFAULT_COLORS):
        logging.Formatter.__init__(self, datefmt=datefmt)
        self._fmt = fmt
        self._colors = {}
        curses.setupterm()
        fg_color = curses.tigetstr('setaf')
        for levelno,code in colors.items():
            self._colors[levelno] = curses.tparm(fg_color, code)
        self._normal = curses.tigetstr('sgr0')

    def format(self, record):
        record.message = record.getMessage()
        record.asctime = self.formatTime(record, self.datefmt)
        record.color = self._colors[record.levelno]
        record.end_color = self._normal
        formatted = self._fmt % record.__dict__
        return formatted


def get_logger(name='default.log', level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    hdlr = logging.StreamHandler()
    hdlr.setLevel(level)
    fmt = PrettyFormatter()
    hdlr.setFormatter(fmt)
    logger.addHandler(hdlr)
    return logger

def test():
    logger = get_logger()
    logger.debug('message')
    logger.info('message')
    logger.warning('message')
    logger.error('message')

if __name__ == '__main__':
    test()
'''
log = logging.getLogger()
dic = {}
colors = {'debug':4,
          'info':2,
          'warning':3,
          'error':1}
form = '%(color)s[%(time)s]'\
    '%(end_color)s %(message)s'
curses.setupterm()
dic['color'] = curses.tparm(curses.tigetstr('setaf'),1)
dic['end_color'] = curses.tigetstr('sgr0')
dic['time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
dic['message'] = 'hello world'
formatted = form % dic
print formatted
'''
