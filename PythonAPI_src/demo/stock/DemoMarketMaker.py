# coding=utf-8
from config import *
from CTSlib.ExtendAPI import *

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

    # 沪伦通做市策略参数查询
    queryCond = QueryCond()
    queryCond.exchId = exchId
    CDRMarketStrategyPara = extendServer.queryCDRMarketStrategyPara(queryCond)
    printMutiObject(CDRMarketStrategyPara, '沪伦通策略参数:')

    # 沪伦通做市增加在线消息
    reqCond = ReqCond()
    reqCond.exchId = exchId
    reqCond.orderType = 'B'
    reqCond.message = 'Error'
    extendServer.addCDRMessage(reqCond)

    # 沪伦通做市商报价参数模型设置
    reqCond = ReqCond()
    reqCond.exchId = exchId
    reqCond.stkId = stkId
    reqCond.acctId = acctId
    reqCond.templateId = '00040'
    extendServer.setCDRSysModel(reqCond)


except Exception as ex:
    Logger.error('Exception... %s' % ex)
