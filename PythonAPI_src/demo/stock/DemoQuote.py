#coding=utf-8
import time
import pydoc

from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *
from config import *

try:
    
    # 设置日志级别
    Logger.setLogOutputFlag(True)
    Logger.setLogLevel(Logger.logLevelDebug)
    
    # 连接服务器
    tradeServer = CtsServer()
    connInfo = tradeServer.connect(serverHost, serverPort)
    printObject(connInfo, '系统连接：')
    
    # 柜员登录
    optLoign = tradeServer.optLogin(optId, optPw)
    printObject(optLoign, '柜员登录：')
    
    # 查证券信息1
    stkInfo1 = tradeServer.queryStkInfo('0', '600050')
    printObject(stkInfo1, '证券信息：')
    
    # 查证券信息2
    stkInfo2 = tradeServer.queryStkInfo('1', '000858')
    printObject(stkInfo2, '证券信息：')

    # 逐笔成交查询
    transInfo = tradeServer.queryTransInfo('0', '600030')
    printObject(transInfo, '逐笔成交信息：')

    # 查询证券信息（异步）
    def onQueryStkInfo(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('证券信息：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '证券信息：')
    tradeServer.onQueryStkInfo = onQueryStkInfo
    tradeServer.queryStkInfo('1', '000858' , False)
        
    # 行情订阅
    subQuotaRequestContent1 = SubQuotaContent('0', '600000')
    subQuotaRequestContent2 = SubQuotaContent('0', '600000')
    def onQuoteEvent(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('行情数据：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '行情数据：')
    tradeServer.onQuoteEvent = onQuoteEvent #订阅数据推送方法
    tradeServer.subscriptQuota([subQuotaRequestContent1, subQuotaRequestContent2])

    # 逐笔成交订阅
    subTransQuotaRequestContent1 = SubQuotaContent('0', '600030')
    subTransQuotaRequestContent2 = SubQuotaContent('0', '600000')
    def onTransQuoteEvent(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('逐笔成交行情数据：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '逐笔成交行情数据：')
    tradeServer.onTransQuoteEvent = onTransQuoteEvent #订阅数据推送方法
    tradeServer.subscriptTransQuota([subTransQuotaRequestContent1, subTransQuotaRequestContent2])

except Exception as ex:
    Logger.error('Exception... %s' % ex)
