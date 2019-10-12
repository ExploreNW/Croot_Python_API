#coding=utf-8
from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *
from config import *
from CTSlib.ExtendAPI import *
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
    
    # 查询行情
    stkInfo = tradeServer.queryStkInfo(exchId, stkId)

    # 报单(同步)
    orderInfo = OrderNewInfo()
    orderInfo.acctId = acctId
    orderInfo.exchId = exchId
    orderInfo.stkId = stkId
    orderInfo.orderType = 'B'
    orderInfo.orderPrice = stkInfo.newPrice
    orderInfo.orderQty = 200
    newOrderResponse = tradeServer.orderNew(orderInfo)
    printObject(newOrderResponse, '报单结果：')
    orderNewContractNum_sync = newOrderResponse.contractNum

    # 报单(异步)
    orderInfo = OrderNewInfo()
    orderInfo.acctId = acctId
    orderInfo.exchId = exchId
    orderInfo.stkId = stkId
    orderInfo.orderType = 'B'
    orderInfo.orderPrice = stkInfo.newPrice
    orderInfo.orderQty = 200
    global orderNewContractNum_noSync
    orderNewContractNum_noSync = ''
    def onOrderNew(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('报单结果：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            global orderNewContractNum_noSync
            orderNewContractNum_noSync = returnData.contractNum
            printObject(returnData, '报单结果：')
            printObject(msgHead)
    tradeServer.onOrderNew = onOrderNew
    msgHead = tradeServer.orderNew(orderInfo, False) #异步请求方法返回包头
    printObject(msgHead, '报单发送：')

    # 撤单(同步)
    time.sleep(2)
    orderCancelInfo = OrderCancelInfo()
    orderCancelInfo.acctId = acctId
    orderCancelInfo.exchId = exchId
    orderCancelInfo.contractNum = orderNewContractNum_sync
    cancellOrderResponse = tradeServer.orderCancel(orderCancelInfo)
    printObject(cancellOrderResponse, '撤单结果：')

    # 撤单(异步)
    orderCancelInfo = OrderCancelInfo()
    orderCancelInfo.acctId = acctId
    orderCancelInfo.exchId = exchId
    orderCancelInfo.contractNum = orderNewContractNum_noSync
    def onOrderCancel(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('撤单结果：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '撤单结果：')
            printObject(msgHead)
    tradeServer.onOrderCancel = onOrderCancel
    msgHead = tradeServer.orderCancel(orderCancelInfo, False) #异步请求方法返回包头
    printObject(msgHead, '撤单发送：')


    # 报单查询(同步)
    queryCond = QueryOrderCond()
    queryCond.acctId = acctId
    orderList = tradeServer.queryOrderList(queryCond, maxRowNum = 100, pageNum = 1,syncFlag = True)
    printObject(orderList,'报单查询：')

    # 报单查询(异步)
    queryCond = QueryOrderCond()
    queryCond.acctId = acctId
    def onQueryOrderList(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('报单查询：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '报单查询：')
            if (msgRespond.lastFlag):
                printString('查询数据全部返回')
    tradeServer.onQueryOrderList = onQueryOrderList
    msgHead = tradeServer.queryOrderList(queryCond, maxRowNum = 100, pageNum = 1,syncFlag = False) #异步请求方法返回包头
    printObject(msgHead,'报单查询发送：')

    # 成交查询(同步)
    queryCond = QueryKnockCond()
    queryCond.acctId = acctId
    knockList = tradeServer.queryKnockList(queryCond, maxRowNum = 100, pageNum = 1, syncFlag = True)
    printObject(knockList, '成交查询：')

    # 成交查询(异步)
    queryCond = QueryKnockCond()
    queryCond.acctId = acctId
    def onQueryKnockList(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('成交查询：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '成交查询：')
            if (msgRespond.lastFlag):
                printString('查询数据全部返回')
    tradeServer.onQueryKnockList = onQueryKnockList
    msgHead = tradeServer.queryKnockList(queryCond, maxRowNum = 100, pageNum = 1,syncFlag = False) #异步请求方法返回包头
    printObject(msgHead,'成交发送：')


except Exception as ex:
    Logger.error('Exception... %s' % ex)
