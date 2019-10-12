# coding=utf-8
import time

from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *
from config import *
from Strategy import *



try:
    
    # 设置日志级别
    Logger.setLogOutputFlag(True)
    Logger.setLogLevel(Logger.logLevelDebug)
    
    # 测试连接服务器
    tradeServer = CtsServer()
    connInfo = tradeServer.connect(serverHost, serverPort)
    printObject(connInfo, '系统连接：')
    
    # 测试账户登录
    acctInfo = tradeServer.accountLogin(acctId, pwd)
    printObject(acctInfo, '账户登录：')
    
    strategySubscript(tradeServer,acctId, pwd)
    # TWAP 报单测试
    strategyPara  = StrategyPara()
    strategyPara.beginTime = '15:19:00'
    strategyPara.endTime = '18:14:00'
    strategyPara.stgQty = 200
    strategyPara.stgPriceLevel = 's1'
    strategyPara.orderInterval = 30
    strategyPara.cancelInterval = 5
    strategyPara.bsFlag = 'B'
    strategyPara.f_offSetFlag = 'OPEN'
    strategyPara.acctId = acctId
    strategyPara.exchId = 'X'
    strategyPara.stkId = '10001065'
    
    strategyTWAP1 = StrategyTWAP(strategyPara,tradeServer)
    
    # TWAP 报单测试
    strategyPara1  = StrategyPara()
    strategyPara1.beginTime = '13:38:00'
    strategyPara1.endTime = '13:58:00'
    strategyPara1.stgQty = 140
    strategyPara1.stgPriceLevel = 's1'
    strategyPara1.orderInterval = 30
    strategyPara1.cancelInterval = 5
    strategyPara1.bsFlag = 'B'
    strategyPara1.f_offSetFlag = 'OPEN'
    strategyPara1.acctId = acctId
    strategyPara1.exchId = 'X'
    strategyPara1.stkId = '10000898'
      
    strategyTWAP2 = StrategyTWAP(strategyPara1,tradeServer)

    
    time.sleep(60)
    strategyTWAP1.stop()
except Exception as ex:
    Logger.error('Exception... %s' % ex)
