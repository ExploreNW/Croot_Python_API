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
    
    # 查证券信息
    stkInfo1 = tradeServer.queryStkInfo('F', 'IF1704')
    printObject(stkInfo1, "期货证券信息：")

    # 查证券信息2
    stkInfo2 = tradeServer.queryStkInfo('D', 'm1709')
    printObject(stkInfo2, '期货证券信息：')

    # 查询证券信息（异步）
    def onQueryStkInfo(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('期货证券信息：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '期货证券信息：')
    tradeServer.onQueryStkInfo = onQueryStkInfo
    tradeServer.queryStkInfo('F', 'IF1704' , False)

    # 期货合约信息查询
    queryCond = QueryFutureCond()
    queryCond.exchId = 'F'
    queryCond.f_productId = 'IF'
    queryCond.basicExchId = '0'
    queryCond.basicStkId = '000300'
    futureInfo = tradeServer.queryFutureInfo(queryCond, maxRowNum=100, pageNum=1)
    printObject(futureInfo, '期货合约信息查询：')

    # 行情订阅
    subQuotaRequestContent1 = SubQuotaContent('F', 'IF1704')
    subQuotaRequestContent2 = SubQuotaContent('D', 'm1709')
    def onQuoteEvent(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('期货行情数据：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '期货行情数据：')
    tradeServer.onQuoteEvent = onQuoteEvent #订阅数据推送方法
    tradeServer.subscriptQuota([subQuotaRequestContent1, subQuotaRequestContent2])
    
except Exception as ex:
    Logger.error('Exception... %s' % ex)
