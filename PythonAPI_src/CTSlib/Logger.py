# coding=utf-8

"""
提供 API 日志服务功能
日志默认输出到程序运行当前目录下的 log 目录，系统自动创建目录结构
日志分为四个级别进行记录，分别是 info, error, warn, debug

"""

__author__ = "GuiPei <guipei@croot.com>"
__status__ = "production"
__version__ = "1.01"
__date__ = "2017-03-10"


import sys, os, datetime
import logging
import types
import traceback
from CTSlib.SysUtils import *
from logging.handlers import RotatingFileHandler

logLevelInfo = logging.INFO
logLevelError = logging.ERROR
logLevelDebug = logging.DEBUG
logLevelWarn = logging.WARN

logDate = datetime.datetime.now().strftime('%Y%m%d')

logPath = ''

logInfo = logging.Logger(logging.INFO)
logDebug = logging.Logger(logging.DEBUG)
logError = logging.Logger(logging.ERROR)
logWarn = logging.Logger(logging.WARN)

# log format
FORMAT = '%(asctime)-15s %(levelname)s -- %(message)s'
defaultFormat = logging.Formatter(FORMAT)
# logging.basicConfig(format=FORMAT, stream=sys.stdout, level=logging.DEBUG)

# log stream
logStream = logging.StreamHandler(stream = sys.stdout)
logStream.setFormatter(defaultFormat)


def setLogPath(path):
    """
    设置日志路径
    """
    logPath = path
    # log path
    if(not os.path.exists(logPath)):
        os.makedirs(logPath)
    
    # log info
    fileHandlerInfo = logging.handlers.RotatingFileHandler('%s/log_%s_info.log' % (logPath, logDate),mode='a',maxBytes=1024 * 1024 * 50,backupCount=100,encoding=encode,delay=0)
    fileHandlerInfo.setFormatter(defaultFormat)
    logInfo.addHandler(fileHandlerInfo)
    
    # log debug
    fileHandlerDebug = logging.handlers.RotatingFileHandler('%s/log_%s_debug.log' % (logPath, logDate),mode='a',maxBytes=1024 * 1024 * 50,backupCount=100,encoding=encode,delay=0)
    fileHandlerDebug.setFormatter(defaultFormat)
    logDebug.addHandler(fileHandlerDebug)
    
    # log error
    fileHandlerError = logging.handlers.RotatingFileHandler('%s/log_%s_error.log' % (logPath, logDate),mode='a',maxBytes=1024 * 1024 * 50,backupCount=100,encoding=encode,delay=0)
    fileHandlerError.setFormatter(defaultFormat)
    logError.addHandler(fileHandlerError)
    
    # log warn
    fileHandlerWarn = logging.handlers.RotatingFileHandler('%s/log_%s_warn.log' % (logPath, logDate),mode='a',maxBytes=1024 * 1024 * 50,backupCount=100,encoding=encode,delay=0)
    fileHandlerWarn.setFormatter(defaultFormat)
    logWarn.addHandler(fileHandlerWarn)

def setLogLevel(level):
    """
    设置日志记录级别

    :parameters: * level : Numeric value
                    * CRITICAL : 50
                    * ERROR : 40
                    * WARNING : 30
                    * INFO : 20
                    * DEBUG : 10
                    * NOTSET : 0

    """
    logInfo.setLevel(level)
    logDebug.setLevel(level)
    logError.setLevel(level)
    logWarn.setLevel(level)

def setLogOutputFlag(flag):
    """
    设置打开或者关闭控制台输出日志功能
    """
    
    if(flag == True):
        logInfo.addHandler(logStream)
        logDebug.addHandler(logStream)
        logError.addHandler(logStream)
        logWarn.addHandler(logStream)
    else:
        logInfo.removeHandler(logStream)
        logDebug.removeHandler(logStream)
        logError.removeHandler(logStream)
        logWarn.removeHandler(logStream)

def error(msg):
    """
    记录错误级别日志
    """
    msg = strEncodeConvert(msg)  
#     exstr = traceback.format_stack()
#     print exstr
#     msg = msg + exstr
    logError.error(msg)

def warn(msg):
    """
    记录警告级别日志
    """
    
    msg = strEncodeConvert(msg)
    logWarn.warn(msg)

def info(msg):
    """
    记录信息级别日志
    """
    
    msg = strEncodeConvert(msg)
    logInfo.info(msg)

def debug(msg):
    """
    记录调试级别日志
    """
    
    msg = strEncodeConvert(msg)
    logDebug.debug(msg)
