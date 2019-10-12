# coding=utf-8
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

    # 获取扩展模块接口
    extendServer = ExtendServer(tradeServer)

    # 查询未到期回购
    queryCond = QueryCond()
    queryCond.acctId = acctId
    undueRepurchase = extendServer.queryUndueRepurchase(queryCond, maxRowNum=100, pageNum=1)
    printObject(undueRepurchase, '查询未到期回购：')

    # 查询现货历史交易日志
    queryCond = QueryCond()
    queryCond.acctId = acctId
    queryCond.beginDate = '2018-07-16'
    queryCond.endDate = '2018-07-17'
    stkTradingLogHis = extendServer.queryStkTradingLogHis(queryCond, maxRowNum=100, pageNum=1)
    printObject(stkTradingLogHis, '查询现货历史交易日志：')

    #非交易锁定解锁功能
    orderInfo = OrderInfo()
    orderInfo.acctId = acctId
    orderInfo.regId = "Sh77210000"
    orderInfo.exchId = exchId
    orderInfo.stkId = stkId
    orderInfo.orderType = 'S'
    orderInfo.orderQty = 100
    orderInfo.orderPrice = 12.6
    msgHead = extendServer.tradeUnderlyOrder(orderInfo)
    printObject(msgHead,'非交易锁定解锁：')


except Exception as ex:
    Logger.error('Exception... %s' % ex)