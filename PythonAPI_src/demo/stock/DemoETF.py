#coding=utf-8
from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *
from CTSlib.ETFAPI import *
from config import *
import traceback

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
    
    # ETF行情订阅
    etfServer = ETFServer(tradeServer)
    subETF1 = SubETFNetValue('0', '510050')
    subETF2 = SubETFNetValue('1', '159919')
    def onETFNetValueEvent(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, 'ETF行情数据：')
    etfServer.onETFNetValueEvent = onETFNetValueEvent #订阅数据推送方法
    etfServer.subscriptETFNetValue([subETF1,subETF2])

    # 做市商报价模型设置2(同步)
    makertMakerModelInfo = MakertMakerModelInfo()
    makertMakerModelInfo.flag = 1
    makertMakerModelInfo.acctId = '000000015225'
    makertMakerModelInfo.basicExchId = 0
    makertMakerModelInfo.basicRate = 100.0
    makertMakerModelInfo.basicStkId =''
    makertMakerModelInfo.bsPriceDiffInterval = -1
    makertMakerModelInfo.bsPriceDiffLevel = 0.0
    makertMakerModelInfo.buyFlag = 0
    makertMakerModelInfo.buyLevelList = 'B1 ^ B2 ^ B3 ^ B4 ^ B5'
    makertMakerModelInfo.buyOrderQtyDiff = 0
    makertMakerModelInfo.buyPriceIncrement = 0.0
    makertMakerModelInfo.buyPriceIncrement1 = 0.0
    makertMakerModelInfo.buyPriceIncrement2 = 0.0
    makertMakerModelInfo.buyPriceRate = 100.0
    makertMakerModelInfo.buyPriceStrategy = 0
    makertMakerModelInfo.buyQtyStrategy = 0
    makertMakerModelInfo.buypriceMode = 0
    makertMakerModelInfo.buywithdrawLevel = -1
    makertMakerModelInfo.canRedeemQty = -1
    makertMakerModelInfo.canSubscriptQty = -1
    makertMakerModelInfo.duration = -1
    makertMakerModelInfo.enabledFlag = 1
    makertMakerModelInfo.exchId = 0
    makertMakerModelInfo.fundType = 0
    makertMakerModelInfo.fundinterestRate = 0.0
    makertMakerModelInfo.knockqty = -1.0
    makertMakerModelInfo.marketRiskEvaluation = 0.0
    makertMakerModelInfo.maxBuyOrderLevel = 1
    makertMakerModelInfo.maxBuyQty = -1
    makertMakerModelInfo.maxOrderQty = -1
    makertMakerModelInfo.maxSellOrderLevel = 1
    makertMakerModelInfo.maxSellQty = -1
    makertMakerModelInfo.minBuyPriceLevel = 0.0
    makertMakerModelInfo.minOrderQty = -1
    makertMakerModelInfo.minSellPriceLevel = 0.0
    makertMakerModelInfo.nAVIncrement = -1.0
    makertMakerModelInfo.newPriceDiffRate = -1.0
    makertMakerModelInfo.noDoubleOfferInterval = -1
    makertMakerModelInfo.noSingleOfferInterval = -1
    makertMakerModelInfo.offerPercent = 5e-324
    makertMakerModelInfo.optFlag = 0
    makertMakerModelInfo.orderPriceIncrement = 5e-324
    makertMakerModelInfo.orderQty = 10
    makertMakerModelInfo.orderSum = 10
    makertMakerModelInfo.paraG = 0.0
    makertMakerModelInfo.paraH = 0.0
    makertMakerModelInfo.paraK = 0.0
    makertMakerModelInfo.paraRF = 0.0
    makertMakerModelInfo.paraSigma = 0.0
    makertMakerModelInfo.preshareDate =''
    makertMakerModelInfo.priceChange = -1.0
    makertMakerModelInfo.priceChangeRate = -1.0
    makertMakerModelInfo.projectId = 'ALL'
    makertMakerModelInfo.projectName = 'ALL'
    makertMakerModelInfo.randomFlag = 0
    makertMakerModelInfo.sellFlag = 0
    makertMakerModelInfo.sellLevelList = 'S1 ^ S2 ^ S3 ^ S4 ^ S5'
    makertMakerModelInfo.sellOrderQtyDiff = 0
    makertMakerModelInfo.sellPriceIncrement = 0.0
    makertMakerModelInfo.sellPriceIncrement1 = 0.0
    makertMakerModelInfo.sellPriceIncrement2 = 0.0
    makertMakerModelInfo.sellPriceRate = 100.0
    makertMakerModelInfo.sellPriceStrategy = 0
    makertMakerModelInfo.sellQtyStrategy = 0
    makertMakerModelInfo.sellpriceMode = 0
    makertMakerModelInfo.sellwithdrawLevel = -1
    makertMakerModelInfo.singleSideInterval = -1
    makertMakerModelInfo.stkId = 501001
    makertMakerModelInfo.targetNAV = 0.0
    makertMakerModelInfo.totalBuyDiffQty = -1
    makertMakerModelInfo.totalBuyQtyDiff = -1
    makertMakerModelInfo.totalSellDiffQty = -1
    makertMakerModelInfo.totalSellQtyDiff = -1
    makertMakerModelInfo.withdrawInterval = 60
    etfServer.modifyMMSPriceModel2(makertMakerModelInfo)

    # 做市商报价模型查询2(同步)
    queryInfo = QueryMMSPriceInfo()
    queryInfo.acctId = acctId
    queryInfo.exchId = exchId
    queryInfo.stkId = stkId
    queryInfo.flag = 1
    queryInfo.optId = optId
    queryInfo.projectId = 'ALL'
    makertMakerInfoList = etfServer.queryMMSPriceModel2(queryInfo)
    printObject(makertMakerInfoList, '做市商报价模型查询2：')

    # 做市商报价运行状态设置2(同步)
    makertMakerStatusInfo = MakertMakerStatusInfo()
    makertMakerStatusInfo.offerStatus = 1
    makertMakerStatusInfo.acctId = acctId
    makertMakerStatusInfo.exchId = exchId
    makertMakerStatusInfo.stkId = stkId
    makertMakerStatusInfo.optId = optId
    makertMakerStatusInfo.projectid = 'ALL'
    etfServer.modifyMMSOrderStatus2(makertMakerStatusInfo)

except Exception as ex:
    Logger.error('Exception... %s' % ex)
    print(traceback.format_exc())
