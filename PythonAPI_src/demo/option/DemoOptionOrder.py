#coding=utf-8
from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *
from CTSlib.ExtendAPI import *
from config import *
import time

try:
    
    # 设置日志级别
    Logger.setLogOutputFlag(True)
    Logger.setLogLevel(Logger.logLevelDebug)
    
    # 测试连接服务器
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
    orderNewContractNum_sync = newOrderResponse.contractNum

    # 报单(异步)
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
    global orderNewContractNum_noSync
    orderNewContractNum_noSync = ''
    def onOrderNew(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('期权报单结果：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            global orderNewContractNum_noSync
            orderNewContractNum_noSync = returnData.contractNum
            printObject(returnData, '期权报单结果：')
            printObject(msgHead)
    tradeServer.onOrderNew = onOrderNew
    msgHead = tradeServer.orderNew(orderInfo, False) #异步请求方法返回包头
    printObject(msgHead, '期权报单发送：')

    # 撤单(同步)
    orderCancelInfo = OrderCancelInfo()
    orderCancelInfo.acctId = acctId
    orderCancelInfo.exchId = exchId
    orderCancelInfo.contractNum = orderNewContractNum_sync
    cancellOrderResponse = tradeServer.orderCancel(orderCancelInfo)
    printObject(cancellOrderResponse, '期权撤单结果：')

    # 撤单(异步)
    time.sleep(1)
    orderCancelInfo = OrderCancelInfo()
    orderCancelInfo.acctId = acctId
    orderCancelInfo.exchId = exchId
    orderCancelInfo.contractNum = orderNewContractNum_noSync
    def onOrderCancel(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('期权撤单结果：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '期权撤单结果：')
            printObject(msgHead)
    tradeServer.onOrderCancel = onOrderCancel
    msgHead = tradeServer.orderCancel(orderCancelInfo, False) #异步请求方法返回包头
    printObject(msgHead, '期权撤单发送：')

    # 双边报单(同步)
    orderInfo1 = QuoteOrderNewInfo()
    orderInfo1.acctId = acctId
    orderInfo1.currencyId = '00'
    orderInfo1.exchId = exchId
    orderInfo1.stkId = stkId
    orderInfo1.orderType = 'B'
    orderInfo1.orderQty = 1
    orderInfo1.orderPrice = 0.001
    orderInfo1.f_offSetFlag = 'OPEN'
    orderInfo1.bsFlag = 'B'
    orderInfo1.businessMark = 'OTO'
    orderInfo1.orderLocalID = '179971'
    orderInfo1.f_orderPriceType = 'LIMIT'

    orderInfo2 = QuoteOrderNewInfo()
    orderInfo2.acctId = acctId
    orderInfo2.currencyId = '00'
    orderInfo2.exchId = exchId
    orderInfo2.stkId = stkId
    orderInfo2.orderType = 'S'
    orderInfo2.orderQty = 1
    orderInfo2.orderPrice = 0.002
    orderInfo2.f_offSetFlag = 'OPEN'
    orderInfo2.bsFlag = 'S'
    orderInfo2.businessMark = 'OTO'
    orderInfo2.orderLocalID = '179971'
    orderInfo2.f_orderPriceType = 'LIMIT'
    newOrderResponse = tradeServer.quoteOrderNew([orderInfo1,orderInfo2])
    printObject(newOrderResponse, '期权双边报单结果：')

    # 双边报单(异步)
    orderInfo1 = QuoteOrderNewInfo()
    orderInfo1.acctId = acctId
    orderInfo1.currencyId = "00"
    orderInfo1.exchId = exchId
    orderInfo1.stkId = stkId
    orderInfo1.orderType = 'B'
    orderInfo1.orderQty = 2
    orderInfo1.orderPrice = 0.001
    orderInfo1.f_offSetFlag = 'OPEN'
    orderInfo1.bsFlag = 'B'
    orderInfo1.businessMark = 'OTO'
    orderInfo1.f_orderPriceType = 'LIMIT'

    orderInfo2 = QuoteOrderNewInfo()
    orderInfo2.acctId = acctId
    orderInfo2.currencyId = "00"
    orderInfo2.exchId = exchId
    orderInfo2.stkId = stkId
    orderInfo2.orderType = 'S'
    orderInfo2.orderQty = 2
    orderInfo2.orderPrice = 0.002
    orderInfo2.f_offSetFlag = 'OPEN'
    orderInfo2.bsFlag = 'S'
    orderInfo2.businessMark = 'OTO'
    orderInfo2.f_orderPriceType = 'LIMIT'
    global orderNewContractNum_noSync
    orderNewContractNum_noSync = ''
    def onQuoteOrderNew(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('期权双边报单结果：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            global orderNewContractNum_noSync
            printObject(returnData, '期权双边报单结果：')
            printObject(msgHead)
    tradeServer.onQuoteOrderNew = onQuoteOrderNew
    msgHead = tradeServer.quoteOrderNew([orderInfo1,orderInfo2], False) #异步请求方法返回包头
    printObject(msgHead, '期权双边报单发送：')

    # 双边撤单(同步)
    orderCancelInfo1 = QuoteOrderCancelInfo()
    orderCancelInfo1.acctId = acctId
    orderCancelInfo1.exchId = exchId
    orderCancelInfo.contractNum = 'SZ003155'

    orderCancelInfo2 = QuoteOrderCancelInfo()
    orderCancelInfo2.acctId = acctId
    orderCancelInfo2.exchId = exchId
    orderCancelInfo2.contractNum = 'SZ003156'
    cancellOrderResponse = tradeServer.quoteOrderCancel([orderCancelInfo1,orderCancelInfo2])
    printObject(cancellOrderResponse, '期权双边撤单结果：')

    # 双边撤单(异步)
    orderCancelInfo1 = QuoteOrderCancelInfo()
    orderCancelInfo1.acctId = acctId
    orderCancelInfo1.exchId = exchId
    orderCancelInfo1.contractNum = 'SZ003159'

    orderCancelInfo2 = QuoteOrderCancelInfo()
    orderCancelInfo2.acctId = acctId
    orderCancelInfo2.exchId = exchId
    orderCancelInfo2.contractNum = 'SZ003160'
    def onQuoteOrderCancel(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('期权双边撤单结果：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '期权双边撤单结果：')
            printObject(msgHead)
    tradeServer.onQuoteOrderCancel = onQuoteOrderCancel
    msgHead = tradeServer.quoteOrderCancel([orderCancelInfo1,orderCancelInfo2], False) #异步请求方法返回包头
    printObject(msgHead, '期权双边撤单发送：')


    # 期权报单查询(同步)
    queryCond = QueryOrderCond()
    queryCond.acctId = acctId
    orderList = tradeServer.queryOrderList(queryCond, maxRowNum = 100, pageNum = 1,syncFlag = True)
    printObject(orderList,'期权报单查询：')
     
    # 期权报单查询(异步)
    queryCond = QueryOrderCond()
    queryCond.acctId = acctId
    def onQueryOrderList(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('期权报单查询：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '期权报单查询：')
            if (msgRespond.lastFlag):
                printString('查询数据全部返回')
    tradeServer.onQueryOrderList = onQueryOrderList
    msgHead = tradeServer.queryOrderList(queryCond, maxRowNum = 100, pageNum = 1,syncFlag = False)
    printObject(msgHead,'期权报单查询发送:')

    # 期权成交查询(同步)
    queryCond = QueryKnockCond()
    queryCond.acctId = acctId
    knockList = tradeServer.queryKnockList(queryCond, maxRowNum = 100, pageNum = 1, syncFlag = True)
    printObject(knockList,'期权成交查询：')

    # 期权成交查询(异步)
    queryCond = QueryKnockCond()
    queryCond.acctId = acctId
    def onQueryKnockList(returnData, msgRespond, msgHead):
        if(msgRespond.successFlg != 0):
            printString('期权成交查询：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '期权成交查询：')
            if (msgRespond.lastFlag):
                printString('查询数据全部返回')
    tradeServer.onQueryKnockList = onQueryKnockList
    msgHead = tradeServer.queryKnockList(queryCond, maxRowNum = 100, pageNum = 1, syncFlag = False)
    printObject(msgHead,'期权成交查询发送：')
    
except Exception as ex:
    Logger.error('Exception... %s' % ex)
