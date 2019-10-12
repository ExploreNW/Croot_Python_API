# coding=utf8
from config import *
from CTSlib.ApiUtils import *
from CTSlib.AlgoAPI import *
from CTSlib.SysUtils import printObject
import copy
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
    
    # 账户登录
    acctInfo = tradeServer.accountLogin(acctId_F, pwd_F)
    printObject(acctInfo, '账户登录：')
    
    # 创建算法服务
    algoServer = AlgoServer(tradeServer)
    
    # 指令ID
    instructId = '00006Z'
    # 策略接收方ID
    fixTargetSubId = 'Scale_Strategy-251'
    
    # 策略下单(现货)
    paraNewAlgoStrategy = ParaNewAlgoStrategy()
    paraNewAlgoStrategy.instructId = instructId
    paraNewAlgoStrategy.acctId = acctId
    paraNewAlgoStrategy.exchId = '0'
    paraNewAlgoStrategy.stkId = '600030'
    paraNewAlgoStrategy.orderType = 'B'
    paraNewAlgoStrategy.orderQty = 20000
    paraNewAlgoStrategy.priceMode = 3
    paraNewAlgoStrategy.orderPrice = 0.00
    paraNewAlgoStrategy.fixText = ''
    paraNewAlgoStrategy.offerStartTime = '09:30:00'
    paraNewAlgoStrategy.offerStopTime = '16:10:00'
    paraNewAlgoStrategy.expireTime = ''
    paraNewAlgoStrategy.fixTargetSubId = fixTargetSubId
    # 策略下单(期货)
    paraNewAlgoStrategyFuture = ParaNewAlgoStrategy()
    paraNewAlgoStrategyFuture.instructId = instructId
    paraNewAlgoStrategyFuture.acctId = acctId_F
    paraNewAlgoStrategyFuture.exchId = 'D'
    paraNewAlgoStrategyFuture.stkId = 'c1805'
    paraNewAlgoStrategyFuture.orderType = 'B'
    paraNewAlgoStrategyFuture.orderQty = 50
    paraNewAlgoStrategyFuture.priceMode = 3
    paraNewAlgoStrategyFuture.orderPrice = 0.00
    paraNewAlgoStrategyFuture.offerStartTime = '09:30:00'
    paraNewAlgoStrategyFuture.offerStopTime = '09:40:00'
    paraNewAlgoStrategyFuture.f_offSetFlag = 'OPEN'
    paraNewAlgoStrategyFuture.fixTargetSubId = fixTargetSubId
    #TWAP-OPT策略
    paraNewAlgoStrategy1 = copy.deepcopy(paraNewAlgoStrategy)
    paraNewAlgoStrategy1.strategyType = 'TWAP-OPT'
    paraNewAlgoStrategy1.firstPosition = 'SP1'
    paraNewAlgoStrategy1.secondPosition = 'OP1'
    msgNewAlgoStrategy1 = algoServer.newAlgoStrategy([paraNewAlgoStrategy1])
    if(msgNewAlgoStrategy1):
        printObject(msgNewAlgoStrategy1, "errorList:")
    #VWAP-OPT策略
    paraNewAlgoStrategy2 = copy.deepcopy(paraNewAlgoStrategy)
    paraNewAlgoStrategy2.strategyType = 'VWAP-OPT'
    msgNewAlgoStrategy2 = algoServer.newAlgoStrategy([paraNewAlgoStrategy2])
    if(msgNewAlgoStrategy2):
        printObject(msgNewAlgoStrategy2, "errorList:")
          
    # 算法策略查询
    paraQueryAlgoStrategy = ParaQueryAlgoStrategy()
    paraQueryAlgoStrategy.instructId = instructId
    paraQueryAlgoStrategy.securityType = 'CS'
    algoStrategyList = algoServer.queryAlgoStrategy(paraQueryAlgoStrategy)
    printObject(algoStrategyList, '算法策略查询:')
              
    # 策略撤单
    paraCancelAlgoStrategy = ParaCancelAlgoStrategy()
    paraCancelAlgoStrategy.instructId = instructId
    paraCancelAlgoStrategy.acctId = acctId
    paraCancelAlgoStrategy.exchId = '0'
    paraCancelAlgoStrategy.stkId = '600030'
    paraCancelAlgoStrategy.batchNum = algoStrategyList[0].batchNum
    msgCancelAlgoStrategy = algoServer.cancelAlgoStrategy([paraCancelAlgoStrategy])
    if(msgCancelAlgoStrategy):
        printObject(msgCancelAlgoStrategy, "errorList:")
              
    # 策略强制撤单
    paraForceCancelAlgoStrategy = ParaForceCancelAlgoStrategy()
    paraForceCancelAlgoStrategy.instructId = instructId
    paraForceCancelAlgoStrategy.acctId = acctId
    paraForceCancelAlgoStrategy.exchId = '0'
    paraForceCancelAlgoStrategy.stkId = '600030'
    paraForceCancelAlgoStrategy.batchNum = algoStrategyList[0].batchNum
    msgForceCancelAlgoStrategy = algoServer.forceCancelAlgoStrategy([paraForceCancelAlgoStrategy])
    if(msgForceCancelAlgoStrategy):
        printObject(msgForceCancelAlgoStrategy, "errorList:")
           
    # 算法报单明细查询
    paraQueryAlgoOrder = ParaQueryAlgoDetailOrder()
    paraQueryAlgoOrder.instructId = instructId
    paraQueryAlgoOrder.securityType = 'FUT'
    paraQueryAlgoOrder.stkId = '600030'
    paraQueryAlgoOrder.batchNum = algoStrategyList[0].batchNum
    paraQueryAlgoOrder.queryType = 1
    paraQueryAlgoOrder.beginTime = '09:30:00'
    paraQueryAlgoOrder.endTime = '18:30:00'
    algoOrderList = algoServer.queryAlgoDetailOrder(paraQueryAlgoOrder)
    printObject(algoOrderList, '算法报单明细查询:')
    
    # 算法报单汇总查询
    paraQueryAlgoSumOrder = ParaQueryAlgoSumOrder()
    paraQueryAlgoSumOrder.instructId = instructId
    paraQueryAlgoSumOrder.batchNum = 1100007
    algoOrderList = algoServer.queryAlgoSumOrder(paraQueryAlgoSumOrder)
    printObject(algoOrderList, '算法报单汇总查询:')
     
    # 算法成交明细查询
    paraQueryAlgoDetailKnock = ParaQueryAlgoDetailKnock()
    paraQueryAlgoDetailKnock.instructId = instructId
    paraQueryAlgoDetailKnock.securityType = 'FUT'
    paraQueryAlgoDetailKnock.batchNum = 1100007
    algoKnockList = algoServer.queryAlgoDetailKnock(paraQueryAlgoDetailKnock)
    printObject(algoKnockList, '算法成交明细查询:')
    
    
except Exception as ex:
    print(traceback.format_exc())
    Logger.error('Exception... %s' % ex)
