#coding=utf-8
from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *
from config import *
from CTSlib.MultiProcessHandle import *
import time

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
    
    # 账户登录
    acctInfo = tradeServer.accountLogin(acctId, pwd)
    printObject(acctInfo, '账户登录：')
    
    # 服务器连接异常断开重连
    def onSocketError(status):
        print('服务器连接断开')
        print('开始重连...')
        while True:
            try:
                connInfo = tradeServer.connect(serverHost, serverPort)
                printObject(connInfo, '系统连接：')
                break
            except Exception as ex:
                Logger.error('connect retry exception... %s' % ex)
                time.sleep(2)
                
        # 柜员登录
        optLoign = tradeServer.optLogin(optId, optPw)
        printObject(optLoign, '柜员登录：')
        # 账户登录
        acctInfo = tradeServer.accountLogin(acctId, pwd)
        printObject(acctInfo, '账户登录：')
        
        stkInfo = tradeServer.queryStkInfo(exchId, stkId)
     
        # 报单(同步)
        orderInfo = OrderNewInfo()    
        orderInfo.acctId = acctId
        orderInfo.currencyId = acctInfo.currencyId
        orderInfo.exchId = exchId
        orderInfo.stkId = stkId
        orderInfo.orderType = 'B'
        orderInfo.orderQty = 2
        orderInfo.orderPrice = stkInfo.newPrice
        orderInfo.f_offSetFlag = 'OPEN'
        orderInfo.bsFlag = 'B'
        orderInfo.businessMark = 'OTO'
        orderInfo.f_orderPriceType = 'ANY'
        newOrderResponse = tradeServer.orderNew(orderInfo)
        printObject(newOrderResponse, '期权报单结果：')
        
        # 成交订阅
        def onTradeEvent(returnData, msgRespond):
            if(msgRespond.successFlg != 0):
                printString('成交数据：')
                printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
            else:
                printObject(returnData, '成交数据：')
        tradeServer.onTradeEvent = onTradeEvent #订阅数据推送方法
        tradeServer.subscriptTrade(acctId, pwd)
        
    tradeServer.onSocketError = onSocketError
    
    
    # 设置报单参数
    orderInfo = OrderNewInfo()
    orderInfo.acctId = acctId
    orderInfo.currencyId = acctInfo.currencyId
    orderInfo.exchId = exchId
    orderInfo.stkId = stkId
    orderInfo.orderType = 'B'
    orderInfo.orderQty = 2
    orderInfo.orderPrice = 0.01
    orderInfo.f_offSetFlag = 'OPEN'
    orderInfo.bsFlag = 'B'
    orderInfo.businessMark = 'OTO'
    orderInfo.f_orderPriceType = 'LIMIT'
    # 重写报单回调方法
    def onOrderNew(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('报单结果：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '报单结果：')
            printObject(msgHead)
    tradeServer.onOrderNew = onOrderNew
    # 实例化多进程报单类，全局只初始化一次
    orderNewHandle = OrderNewHandle(multiProcessCnt)
    for i in range(10):
        orderNewHandle.order(tradeServer.orderNew, orderInfo)
        
        
except Exception as ex:
    Logger.error('Exception... %s' % ex)
