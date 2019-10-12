# coding=utf-8
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
    
    # 账户登录
    acctInfo = tradeServer.accountLogin(acctId, pwd)
    printObject(acctInfo, '账户登录：')
    
    # 资金账号查询
    queryAccountResponse = tradeServer.queryAccountInfo(acctId)
    printObject(queryAccountResponse, '账号查询：')

    # 资金账号查询(异步)
    def onQueryAccountInfo(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('账号查询：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '账号查询：')
    tradeServer.onQueryAccountInfo = onQueryAccountInfo
    tradeServer.queryAccountInfo(acctId, syncFlag = False)

    # 持仓查询(同步)
    queryCond = QueryPositionCond()
    queryCond.acctId = acctId
    positionList = tradeServer.queryPositionList(queryCond, maxRowNum = 100, pageNum = 1, syncFlag = True)
    printObject(positionList, '持仓查询：')

    # 持仓查询(异步)
    queryCond = QueryPositionCond()
    queryCond.acctId = acctId
    def onQueryPositionList(returnData, msgRespond, msgHead):
        print('stkId' in dir(returnData))
        if(msgRespond.successFlg != 0):
            printString('持仓查询：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '持仓查询：')
            if (msgRespond.lastFlag):
                printString('查询数据全部返回')
    tradeServer.onQueryPositionList = onQueryPositionList
    msgHead = tradeServer.queryPositionList(queryCond, maxRowNum = 100, pageNum = 1, syncFlag = False) #异步请求方法返回包头
    printObject(msgHead,'持仓查询发送：')

    # 成交订阅
    def onTradeEvent(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('成交数据：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '成交数据：')
    tradeServer.onTradeEvent = onTradeEvent #订阅数据推送方法
    tradeServer.subscriptTrade(acctId, pwd)
     
except Exception as ex:
    Logger.error('Exception... %s' % ex)
