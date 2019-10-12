# coding=utf-8
from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *
from CTSlib.ExtendAPI import *
from config import *
import time

try:
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

    # 查询期货历史交易日志
    extendServer = ExtendServer(tradeServer)
    queryCond = QueryCond()
    queryCond.acctId = acctId
    queryCond.beginDate = '2018-07-16'
    queryCond.endDate = '2018-07-17'
    futTradingLogHis = extendServer.queryFutTradingLogHis(queryCond, maxRowNum=100, pageNum=1)
    printObject(futTradingLogHis, '查询期货历史交易日志：')

except Exception as ex:
    Logger.error('Exception... %s' % ex)
