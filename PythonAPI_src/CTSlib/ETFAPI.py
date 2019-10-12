# -*- coding: utf-8 -*-
"""
Python API ETF接口模块
"""
from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *


class ETFServer(object):

    def __init__(self, ctsServer):

        self.ctsServer = ctsServer
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ETF_SUB_NETVALUE, self.onSubsciptETFNetValue)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ETF_SUB_NETVALUE_RETURN, self.onETFNetValueInternalEvent)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ETF_MODIFY_MMS_PRICE_MODEL2, self.onModifyMMSPriceModel2)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ETF_QRY_MMS_PRICE_MODE12, self.onQueryMMSPriceModel2)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ETF_MODIFY_MMS_ORDER_STATUS2, self.onModifyMMSOrderStatus2)

    def subscriptETFNetValue(self, quotaList, subType = 0):
        """
        ETF行情订阅

        :parameters: * quotaList : []
                            * exchId : 市场
                            * stkId : 证券代码
                     * subType : 订阅类型(必送，默认为0) 0-订阅 1-退订
        """

        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ETF_SUB_NETVALUE, self.ctsServer.sessionId)

        msgRequest = ParaSubETFNetValue(quotaList, subType)
        msgData = MsgData(msgHead, msgRequest)

        self.ctsServer.sendData(msgData)


    def onSubsciptETFNetValue(self, jsonData, msgRespond, msgHead):
        '''
        ETF行情订阅响应回调
        '''
        # 处理同步请求模式
        if (msgRespond.successFlg == 0):
            msgData = "订阅/退订成功!"
        elif (msgRespond.successFlg == 1):
            msgData = "订阅/退订失败!"

        printObject(msgData)
        

    def onETFNetValueInternalEvent(self, jsonData, msgRespond, msgHead):
        '''
        ETF行情订阅数据回调
        '''
        msgData = MsgSubETFNetValueReturn()
        if ("quotaInfo" in jsonData):
            msgData.__dict__ = jsonData["quotaInfo"]
        
        self.onETFNetValueEvent(msgData, msgRespond)


    def onETFNetValueEvent(self, data, msgRespond):
        '''
        ETF行情订阅数据推送回调方法

        :param CTSlib.ApiStruct.MsgSubETFNetValueReturn data:
        :param CTSlib.ApiStruct.MsgRespond msgRespond:

        '''
        Logger.debug('onETFNetValueEvent:')
        printObject(data)

    def modifyMMSPriceModel2(self,makertMakerModelInfo):
        '''
        做市商报价模型设置2
        :parameters:  * makertMakerModelInfo: 做市模型参数
                            * flag                   : 0-新增，1-修改，3-删除（必选）
                            * acctId                 : 资金账号（必选）
                            * exchId                 : 市场代码（必选）
                            * stkId                  : 证券代码（必选）
                            * projectId              : 模型代码（必选）
                            * buyPriceIncrement1     : 买入时如果与对手盘成交，则加减档位（可选）
                            * sellPriceIncrement1    : 卖出时如果与对手盘成交，则加减档位（可选）
                            * buyPriceIncrement2     : 买入变化量（在自动报单的界面调整）（可选）
                            * sellPriceIncrement2    : 卖出变化量（在自动报单的界面调整）（可选）
                            * projectName            : 模型名称（可选）
                            * enabledFlag            : 激活标志（0表示不启用，1表示启用)（可选）
                            * preshareDate           : 上次份额折算日（可选）
                            * fundinterestRate       : 基金参考利率（可选）
                            * fundType               : 基金类别（可选）
                            * sellFlag               : 允许卖标志（可选）
                            * buyFlag                : 允许买标志（可选）
                            * processFlag            : 处理标志（当入参processFlag=1时，只更新sellpriceincrement2、buypriceincrement2两个字段，其余字段不做更新）（可选）
                            * noDoubleOfferInterval  : 双边买卖申报持续时间（没有买卖申报且持续x1分钟以上）（可选）
                            * noSingleOfferInterval  : 单边买卖申报持续时间（只有单边买入申报或卖出申报且持续x2分钟以上）（可选）
                            * bsPriceDiffLevel       : 买卖盘口价差级别（卖1价与买1价之差超过）（可选）
                            * newPriceDiffRate       : 买卖价差同最新价比例（基金最新成交价格的x4）（可选）
                            * bsPriceDiffInterval    : 买卖价差持续时间（持续x5分钟以上）（可选）
                            * totalBuyDiffQty        : 买盘口数量和（五档买盘之和少于x6个基金份额）（可选）
                            * totalSellDiffQty       : 卖盘口数量和（五档卖盘之和少于x8个基金份额）（可选）
                            * singleSideInterval     : 盘口量持续时间（并持续x7分钟以上）（可选）
                                                     :
                            # 报单价格的策略设置     :
                            * buyPriceStrategy       : 买入价格策略（0--价位策略，1--比例策略）（可选）
                            * sellPriceStrategy      : 卖出价格策略（0--价位策略，1--比例策略）（可选）
                            * minBuyPriceLevel       : 最小买入价位 y4（如0.001、0.002）（可选）
                            * minSellPriceLevel      : 最小卖出价位 y5（如0.001、0.002）（可选）
                            * buyPriceRate           : 买入价格的百分比设置（可选）
                            * sellPriceRate          : 卖出价格的百分比设置（可选）
                            * buyPriceIncrement      : 买入变化量（可选）
                            * sellPriceIncrement     : 卖出变化量（可选）
                                                     :
                            # 报单数量的策略设置     :
                            * buyQtyStrategy         : 买入数量策略（0-单笔数量，1-分档数量，2-扫盘策略）（可选）
                            * sellQtyStrategy        : 卖出数量策略（0-单笔数量，1-分档数量，2-扫盘策略）（可选）
                            * maxBuyQty              : 最大买入数量（买入申报数量为y1个基金份额）（可选）
                            * maxSellQty             : 最大卖出数量（卖出申报数量为y2个基金份额）  （可选）
                            * maxBuyOrderLevel       : 报单买入最大档位（可选）
                            * maxSellOrderLevel      : 报单卖出最大档位（可选）
                                                     :
                            # 撤单时间与其它参数设置 :
                            * withdrawInterval       : 撤单时间，单位秒（可选）
                            * marketRiskEvaluation   : 市场风险估计（可选）
                            * basicExchId            : 参考市场代码（可选）
                            * basicStkId             : 参考证券代码（可选）
                            * buypriceMode           : 买入净值方式（可选）
                            * sellpriceMode          : 卖出净值方式（可选）
                                                     :
                            # 随机拆单需要的参数     :
                            * randomFlag             : 随机拆单启用标记（可选）
                            * minOrderQty            : 数量下限（可选）
                            * maxOrderQty            : 数量上限（可选）
                            * canRedeemQty           : 可赎回数量（可选）
                            * canSubscriptQty        : 可申购数量（可选）
                            * buyLevelList           : 买盘区域（可选）
                            * sellLevelList          : 卖盘区域（可选）
                            * totalBuyQtyDiff        : 累计买入数量差（可选）
                            * totalSellQtyDiff       : 累计卖出数量差（可选）
                            * buyOrderQtyDiff        : 买入对冲量设置（可选）
                            * sellOrderQtyDiff       : 卖出对冲量设置（可选）
                            * buywithdrawLevel       : 买入撤单盘口档位（可选）
                            * sellwithdrawLevel      : 卖出撤单盘口档位（可选）
                            * basicRate              : 基本利率（可选）
                            * optFlag                : 自定义计算净值标记（0-系统计算，1-自定义计算）（可选）
                            * paraSigma              : 波动率（可选）
                            * paraRF                 : 无风险利率（可选）
                            * paraG                  : 红利率（可选）
                            * paraK                  : 行权价（可选）
                            * paraH                  : 敲出价（可选）
                            * NAVIncrement           : 净值变化量（可选）
                            * targetNAV              : 目标基金的单位净值（可选）
                            * duration               : 触发周期（可选）
                            * priceChange            : 价格变动（可选）
                            * priceChangeRate        : 价格变动率（可选）
                            * knockqty               : 成交数量（可选）
                            * orderType              : 买卖方向（可选）
                            * orderSum               : 委托总笔数（可选）
                            * orderQty               : 委托数量（可选）
                            * qtyStrategy            : 数量策略（可选）
                            * offerPercent           : 吃盘比例（可选）
                            * orderPriceIncrement    : 价格每次变化增量（可选）
        '''
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ETF_MODIFY_MMS_PRICE_MODEL2, self.ctsServer.sessionId)
        msgRequest = ParaModifyMMSPriceModel2(makertMakerModelInfo)

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onModifyMMSPriceModel2(self,jsonData, msgRespond, msgHead):
        '''
        做市商报价运行状态设置2回调函数
        '''
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = ''
            if (msgRespond.successFlg == 0):
                msgData = '模型设置成功'
            elif (msgRespond.successFlg == 1):
                msgData = '模型设置失败'

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

    def queryMMSPriceModel2(self, queryInfo):
        '''
        做市商报价模型查询2

        :parameters:  * queryInfo : 查询条件
                          * acctId : 资金账号
                          * exchId : 市场代码（可选）
                          * stkId : 证券代码(可选)
                          * flag  : 0-查询报价模型，1-查询报单数量的详细信息（可选）
                          * optId : 柜员代码（可选）
                          * projectId : 模型代码（可选）
        '''

        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ETF_QRY_MMS_PRICE_MODE12, self.ctsServer.sessionId)

        msgRequest = ParaQueryMMSPriceMode12(queryInfo)
        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onQueryMMSPriceModel2(self, jsonData, msgRespond, msgHead):
        '''
        做市商报价模型查询2回调方法
        '''
        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = []
            if ("resultList" in jsonData):
                msgDataList = jsonData["resultList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgQueryMMSPriceMode12()
                    msgDataDict.__dict__ = msgDataDictTmp

                    msgData.append(msgDataDict)

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

    def modifyMMSOrderStatus2(self, makertMakerStatusInfo):
        '''
        做市商报价运行状态设置2

        :parameters: * makertMakerInfo : 做市状态参数
                        * acctId      : 资金账号（必选）
                        * exchId      : 市场代码（可选）
                        * stkId       : 证券代码（可选）
                        * optId       : 柜员代码（可选）
                        * projectid   : 模型代码（可选）
                        * offerStatus : 运行状态（必选）
                           * '0' : 未执行
                           * '1' : 开始执行
                           * '2' : 暂停
                           * '3' : 完成
                           * '4' : 继续完成
                           * '5' : 等待终止
                           * '6' : 挂起
        '''

        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ETF_MODIFY_MMS_ORDER_STATUS2, self.ctsServer.sessionId)
        msgRequest = ParaModifyMMSOrderStatus2(makertMakerStatusInfo)

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onModifyMMSOrderStatus2(self,jsonData, msgRespond, msgHead):
        '''
        做市商报价运行状态设置2回调函数
        '''
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = ''
            if (msgRespond.successFlg == 0):
                msgData = '状态设置成功'
            elif (msgRespond.successFlg == 1):
                msgData = '状态设置失败'

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)


class ParaSubETFNetValue(object):
    """
    行情订阅

    :fieldmembers: * quotaList :
                        * exchId : 市场
                        * stkId : 证券代码
                   * subType : 订阅类型(必送，默认为0) 0-订阅 1-退订
    """
    # 0-订阅，1-退订（必送）
    subType = ''

    quotaList = []

    def __init__(self, quotaList, subType):
        self.subType = subType
        self.quotaList = quotaList


class MsgSubETFNetValueReturn(object):
    '''
    ETFNetValueInfo                    ETF行情信息

    :fieldmembers:  * exchId : 市场
                    * stkId : 证券代码
                    * stkName : 证券名称
                    * closePrice : 昨收盘
                    * openPrice : 开盘价
                    * highPrice : 今日最高价
                    * lowPrice : 今日最低价
                    * newPrice : 最新价
                    * newNet : 最新净值
                    * IOPV : 交易所净值
                    * knockAmt : 成交总金额
                    * totalKnockQty : 成交总数量
                    * buy : 买盘价
                    * buyAmt : 买盘量
                    * sell : 卖盘价
                    * sellAmt : 卖盘量
                    * buyNet : 买净值 
                    * sellNet : 卖净值 
                    * optTime : 时间（精度到秒）

    '''

class SubETFNetValue(object):
    """
    行情订阅

    :fieldmembers:  * exchId : 市场
                    * stkId : 证券代码
    """
    exchId = ''
    stkId = ''
    
    def __init__(self, exchId, stkId):
        self.exchId = exchId
        self.stkId = stkId