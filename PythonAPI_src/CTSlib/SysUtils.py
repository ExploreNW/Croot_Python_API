# coding=utf-8

"""
    提供系统工具类   

"""
from _ast import Str

__author__ = "GuiPei <guipei@croot.com>"
__status__ = "production"
__version__ = "1.01"
__date__ = "2017-03-10"


import threading
import types
import time

#日志字符集
encode = 'utf-8'

#单例类
class Borg(object):
    _state = {}  
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

lock = threading.Lock()

#序号管理器
class SequenceManager (Borg):
    
    num = 10000000 
    def getNextId(self):
        if lock.acquire():
            self.num = self.num + 1
            lock.release()
            return self.num;

def checkValid(obj):
    """
    判断变量是否为空
    """
    if(obj != None and obj != ""):
        return True
    else:
        return False

def strEncodeConvert(msg):
    
    t = type(msg)
    if(t == bytes):
        msg = msg.decode(encode)
    return msg

def printObject(theObject, msg = None):
    """
    打印输出对象
    """
    
    if not checkValid(theObject):
        return
    
    if msg != None:
        printString(msg)
        
    if type(theObject) == str:
        printString (theObject)
        
    elif type(theObject) == list:
        for item in theObject:
            printObject(item)
            print("\n")
    else:
        for key, value in vars(theObject).items():
            printString ("   .%s=%s " , (key, value))
            
def printMutiObject(theObject, msg = None):
    """
    打印输出对象
    """
    
    if not checkValid(theObject):
        return
    
    if msg != None:
        printString(msg)
        
    for key, value in vars(theObject).items():
        
        printString (" .%s= " , key)
        if type(value) == list:
            for item in value:
#                 printString("     %s ",str(item.__dict__))
                printObject(item)
                printObject("\n")
            
        else:
#             printString("  %s ",value.__dict__)
            printObject(value)
            printObject("\n")

def printString(key, value = None):
    """
    字符串打印，将字符进行编码后打印。
    """
    if not checkValid(value):
        #value=None时，直接打印key。
        print((strEncodeConvert(key)))
    else:
        #value！=None时，按key格式化value，并输出
        print((strEncodeConvert(key) % strEncodeConvert(value)))

def getTerminalInfo():
    '''
    获取简单终端信息
    '''
    import socket
    import uuid
    # 获取主机名
    hostname = socket.gethostname()
    #获取IP
    ip = socket.gethostbyname(hostname)
    # 获取Mac地址
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    
    return ('LIP:%s;MAC:%s;PCN:%s' %(ip,mac,hostname)).upper()

def getMac():
    '''
    获取终端MAC信息
    '''
    import uuid

    # 获取Mac地址
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]

    return mac.upper()

def getSecond(time1,time2):
    '''
    计算两个时间点的时间间隔（s）
    时间格式 : %Y%m%d%H%M%S
    '''
    num1 = int(time.mktime(time.strptime(time1, "%Y%m%d%H%M%S")))
    num2 = int(time.mktime(time.strptime(time2, "%Y%m%d%H%M%S")))
    return num2-num1