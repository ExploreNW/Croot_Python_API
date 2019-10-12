# -*- coding: utf-8 -*-
"""
Python API 扩展接口模块
"""
import time
from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *


class ExtendServer(object):

    def __init__(self, ctsServer):

        self.ctsServer = ctsServer
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_EXTEND_ORY_UNDUEREPURCHASE, self.onQueryUndueRepurchase)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_EXTEND_ORY_STKTRADINGLOG, self.onQueryStkTradingLogHis)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_EXTEND_ORY_FUTTRADINGLOG, self.onQueryFutTradingLogHis)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_EXTEND_ORY_STRATEGYPARA, self.onQueryCDRMarketStrategyPara)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_EXTEND_ADDMSGONLINE, self.onAddCDRMessage)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_EXTEND_SYSMESSAGE, self.onSetCDRSysModel)

    def queryUndueRepurchase(self, queryCond, maxRowNum = 100, pageNum = 1):
        '''
        查询未到期回购

        :parameters:  * queryCond : 查询条件
                          * acctId : 资金账号
                          * stkId : 证券代码(可选)
                      * maxRowNum : 最大查询记录数量(可选，默认为100)
                      * pageNum : 查询页数(可选，默认为1)
        '''

        msgHead = MsgHead(MsgTypeList.MSG_TYPE_EXTEND_ORY_UNDUEREPURCHASE, self.ctsServer.sessionId)

        msgRequest = ParaQueryUndueRepurchase(queryCond, maxRowNum, pageNum)
        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onQueryUndueRepurchase(self, jsonData, msgRespond, msgHead):
        '''
        查询未到期回购回调方法
        '''
        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = []
            if ("undueRepurchaseList" in jsonData):
                msgDataList = jsonData["undueRepurchaseList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgQueryUndueRepurchase()
                    msgDataDict.__dict__ = msgDataDictTmp

                    msgData.append(msgDataDict)

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)


    def queryStkTradingLogHis(self,queryCond, maxRowNum = 100, pageNum = 1):
        '''
        查询现货历史交易日志

        :parameters:  * queryCond : 查询条件
                          * queryOptId : 查询柜员代码(可选)
                          * beginDate : 起始日期(必送)
                          * endDate : 截止日期(必送)
                          * acctId : 资金帐号(必送)
                          * grantExchList : 交易所代码(可选，多个使用^隔开)
                          * stkId : 证券代码(可选)
                          * regId : 股东代码(可选)
                          * custId : 客户帐号(可选)
                          * briefId : 摘要代码(可选)
                          * currencyId : 货币代码(可选)
                          * bankId : 银行代码(可选)
                          * branchId : 客户开户营业部代码、所属营业部代码、营业部标识、营业部(可选)
                          * custType : 客户类别(可选)
                          * brokerId : 经纪人代码(可选)
                          * creditFundFlag : 信用资金帐户标志,账户属性(可选)
                      * maxRowNum : 最大查询数量(可选)
                      * pageNum : 查询页码(可选)
        '''

        msgHead = MsgHead(MsgTypeList.MSG_TYPE_EXTEND_ORY_STKTRADINGLOG, self.ctsServer.sessionId)

        msgRequest = ParaQueryStkTradingLogHis(queryCond, maxRowNum, pageNum)
        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onQueryStkTradingLogHis(self,jsonData, msgRespond, msgHead):
        '''
        查询现货历史交易日志回调方法
        '''
        # 处理同步请求模式
        if(msgHead.requestId in self.ctsServer.reqMap):
            msgData = []
            if ("tradingInfoList" in jsonData):
                msgDataList = jsonData["tradingInfoList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgQueryStkTradingLogHis()
                    msgDataDict.__dict__ = msgDataDictTmp

                    msgData.append(msgDataDict)

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

    def queryFutTradingLogHis(self, queryCond, maxRowNum = 100, pageNum = 1):
        '''
        查询期货历史交易日志

        :parameters:  * queryCond : 查询条件
                          * beginDate : 开始日期（必送）
                          * endDate : 截止日期（必送）
                          * f_productId : 品种代码
                          * exchId : 市场代码
                          * branchId : 营业部代码
                          * deskId : 席位代码
                          * acctId : 资金帐号
                          * regId : 交易编码
                          * futureId : 合约代码
                          * basketId : 投资组合代码(多选)【根据app处理逻辑进行注释】
                          * briefId : 操作摘要
                          * internalOffSetFlag : 内部开平标识
                          * internalCoveredFlag : 内部备兑标识
                          * brokerId : 经纪人代码(可选)
                          * creditFundFlag : 信用资金帐户标志,账户属性(可选)
                      * maxRowNum : 最大查询数量(可选)
                      * pageNum : 查询页码(可选)

        '''
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_EXTEND_ORY_FUTTRADINGLOG, self.ctsServer.sessionId)

        msgRequest = ParaQueryStkTradingLogHis(queryCond, maxRowNum, pageNum)
        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onQueryFutTradingLogHis(self,jsonData, msgRespond, msgHead):
        '''
        查询期货历史交易日志回调方法
        '''
        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = []
            if ("tradingInfoList" in jsonData):
                msgDataList = jsonData["tradingInfoList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgQueryFutTradingLogHis()
                    msgDataDict.__dict__ = msgDataDictTmp

                    msgData.append(msgDataDict)

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

    def queryCDRMarketStrategyPara(self,queryCond):
        '''
        沪伦通做市策略参数查询

        :parameters:  * queryCond : 查询条件
                          * exchId : 市场(可选)
        '''
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_EXTEND_ORY_STRATEGYPARA, self.ctsServer.sessionId)
        msgRequest = ParaQueryCDRMarketStrategyPara(queryCond)

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onQueryCDRMarketStrategyPara(self, jsonData, msgRespond, msgHead):
        '''
        沪伦通做市策略参数查询回调方法
        '''
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = MsgQueryMarketInfo()
            msgDataList = []
            if ("marketStrategyList" in jsonData):
                msgDataListTmp = jsonData["marketStrategyList"]
                for msgDataDictTmp in msgDataListTmp:
                    msgQueryStrategyInfo_StrategyList = MsgMarketStrategyList()
                    msgQueryStrategyInfo_StrategyList.__dict__ = msgDataDictTmp

                    msgDataList.append(msgQueryStrategyInfo_StrategyList)

                msgData.marketStrategyList = msgDataList

            if ("marketStrategyPara" in jsonData):
                msgQueryStrategyInfo_StrategyInfo = MsgMarketStrategyPara()
                msgQueryStrategyInfo_StrategyInfo.__dict__ = jsonData["marketStrategyPara"]
                msgData.marketStrategyPara = msgQueryStrategyInfo_StrategyInfo

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)


    def addCDRMessage(self, reqCond):
        '''
        沪伦通做市增加在线消息

        :parameters:  * regCond : 请求参数
                        * exchId : 市场代码（exchid,必送）
                        * stkId : 证券代码（CDR,必送）
                        * orderType : 业务类型（openorder表的orderType,必送）
                        * message : 消息内容（证券代码stkid，APP返回的错误信息failinfo,必送）
                        * sendTime : 发送时间（当前时间,必送）
                        * grantOptList : 柜员列表（23010089对应exchid+stkid的authOptId,必送）
        '''
        reqCond.stkId = 'CDR'

        reqCond.sendTime = time.strftime("%Y%m%d%H%M%S", time.localtime())

        msgHead = MsgHead(MsgTypeList.MSG_TYPE_EXTEND_ADDMSGONLINE, self.ctsServer.sessionId)
        msgRequest = ParaAddMessegeOnline(reqCond)

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onAddCDRMessage(self, jsonData, msgRespond, msgHead):
        '''
        沪伦通做市增加在线消息回调方法
        '''
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = ''
            if (msgRespond.successFlg == 0):
                msgData = '参数设置成功'
            elif (msgRespond.successFlg == 1):
                msgData = '参数设置失败'

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

    def setCDRSysModel(self, reqCond):
        '''
        沪伦通做市商报价参数模型设置

        :parameters: * reqCond : 请求参数
                        * actionFlag : 操作标志（*）(送MOD)(必送)
                        * exchId : 市场(必送)
                        * stkId : 证券代码(必送)
                        * acctId : 资金账号(必送)
                        * bidType : 报价策略(送B)(必送)
                        * templateId : 模型代码(必送)
                        * enabledFlag : 启动标志（送N）(必送)
        '''

        reqCond.actionFlag = 'MOD'
        reqCond.bidType = 'B'
        reqCond.enabledFlag = 'N'

        msgHead = MsgHead(MsgTypeList.MSG_TYPE_EXTEND_SYSMESSAGE, self.ctsServer.sessionId)
        msgRequest = ParaSysModel(reqCond)

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data

    def onSetCDRSysModel(self,jsonData, msgRespond, msgHead):
        '''
        沪伦通做市商报价参数回调方法
        '''
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = ''
            if (msgRespond.successFlg == 0):
                msgData = '参数设置成功'
            elif (msgRespond.successFlg == 1):
                msgData = '参数设置失败'

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)
            
    def tradeUnderlyOrder(self, orderInfo):
        """
        非交易锁定解锁功能

        :parameters: * reqCond : 请求参数
                        * acctId : 资金帐号(必送)
                        * exchId : 交易市场(必送)
                        * stkId : 证券代码(必送)
                        * orderType : 委托类型(必送)（B-解锁，S锁定）
                        * orderQty : 锁定解锁数量(必送)
                        * orderPrice : 委托价格(必送)
                        * regId : 股东代码(可选,默认报单市场的第一个股东)
                        * businessMark : 交易业务类型(必送)(OTO-期权订单，OTU-证券冻结与解冻，OTE-行权)
        """
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_NON_TRADE_LOCK_UNLOCK, self.ctsServer.sessionId)
        msgRequest = TradeOrderInfo(orderInfo)

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)

        return reqDataValue.data
    
    def onTradeUnderlyOrder(self, jsonData, msgRespond, msgHead):
        '''
        非交易锁定解锁回调方法
        '''
        if (msgHead.requestId in self.ctsServer.reqMap):            
            msgData = MsgOrderInfo()
            if (msgRespond.successFlg == 0):
               if ("contractNum" in jsonData):
                        msgData.contractNum = jsonData.get('contractNum','')

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

class ParaQueryFutTradingLogHis(object):
    '''
    期货历史交易日志查询参数

    :fieldmembers:  * queryCond : 查询条件
                        * acctId: 资金帐号（必送）
                        * beginDate : 开始日期（必送）
                        * endDate : 截止日期（必送）
                        * f_productId : 品种代码
                        * exchId: 市场代码
                        * regId : 交易编码
                        * futureId: 合约代码
                        * briefId : 操作摘要
                        * creditFundFlag: 信用资金帐户标志,账户属性(可选)
                    * maxRowNum : 最大查询数量(可选，默认为100)
                    * pageNum : 查询页码(可选，默认为1)

    '''


class MsgQueryFutTradingLogHis(object):
    '''
    tradingInfoList               期货交易信息列表

    :fieldmembers:  * serialNum : 流水号
                    * briefId : 摘要代码
                    * exteriorDesc : 摘要描述
                    * currencyId : 货币代码
                    * reckoningTime : 清算时间
                    * occurTime : 发生时间
                    * partId : 会员编号
                    * bankId : 银行代码
                    * contractNum : 合同序号
                    * branchId : 营业部代码
                    * custId : 客户代码
                    * custName : 客户姓名
                    * custType : 客户类别
                    * exchId : 交易市场
                    * acctId : 资金帐号
                    * acctName : 帐户名称
                    * regId : 交易编码
                    * offerRegId : 报盘股东代码
                    * F_productId : 产品代码
                    * stkId : 合约代码
                    * stkName : 合约名称
                    * deskId : 席位代码
                    * bsFlag : 买卖方向
                    * bsFlagDesc : 买卖方向描述
                    * settlementPrice : 今结算价格
                    * preSettlementPrice : 昨结算价格
                    * knockCode : 成交编号
                    * knockQty : 成交数量
                    * kncokPrice : 成交价格
                    * knockAmt : 成交金额
                    * knockTime : 成交时间
                    * reckoningAmt : 清算金额
                    * postAmt : 后资金额
                    * postQty : 后持有数量
                    * exchCommision : 交易所手续费
                    * custCommision : 客户手续费
                    * custMarginAmt : 客户保证金占用
                    * exchMarginAmt : 交易所保证金占用
                    * closePNL : 平仓盈亏
                    * realTimePNL : 实时盈亏
                    * F_hedgeFlag : 投保标志
                    * F_hedgeFlagDesc : 投保标志描述
                    * F_offsetFlagDesc : 开平标志描述
                    * internalOffSetFlag : 内部开平标识
                    * internalOffSetFlagDesc : 内部开平标识描述
                    * str2 : 备兑标识（外）
                    * str3 : 备兑标识（内）
                    * costCenterId : 成本中心代码
                    * salesId : 销售员代码
                    * accountingFlag : 后台记帐标志
                    * getAccountDate : 记帐日期
                    * getAccountNum : 记帐流水号
                    * selfFlag : 自营标志
                    * custodyMode : 托管方式
                    * settleDate : 清算日期
                    * settleOptId : 清算柜员代码
                    * optMode : 委托方式
                    * memo : 备注
                    * openPrice : 开仓价格
                    * openDate : 开仓日期
                    * openKnockCode : 开仓成交编号
                    * floatPNL : 浮动盈亏
                    * everyPositionPNL : 逐笔持仓盈亏
                    * basketId : 投资组合代码
                    * interContnum : 内部流水号
                    * F_MatchCondition : 有效期类型
                    * handlingfee : 经手费
                    * reckoningfee : 结算费
                    * da1 : 盈亏（不含手续费）
    '''


class ParaQueryStkTradingLogHis(object):
    '''
    现货历史交易日志查询参数

    :fieldmembers:  * queryCond : 查询条件
                        * beginDate :起始日期(必送)
                        * endDate :截止日期(必送)
                        * acctId:资金帐号(必送)
                        * regId :股东代码(可选)
                        * stkId :证券代码(可选)
                        * briefId :摘要代码(可选)
                        * currencyId:货币代码(可选)
                        * creditFundFlag:信用资金帐户标志,账户属性(可选)
                    * maxRowNum : 最大查询数量(可选，默认为100)
                    * pageNum : 查询页码(可选，默认为1)
    '''
    queryCond = ''
    maxRowNum = ''
    pageNum = ''

    def __init__(self, queryCond, maxRowNum, pageNum):
        self.queryCond = queryCond
        self.maxRowNum = maxRowNum
        self.pageNum = pageNum


class MsgQueryStkTradingLogHis(object):
    '''
    tradingInfoList               现货交易信息列表

    :fieldmembers:  * serialNum : 流水号
                    * briefId : 摘要代码
                    * occurTime : 发生时间
                    * reckoningTime : 清算时间
                    * acctId : 资金帐号
                    * acctName : 帐户姓名
                    * regId : 股东帐户
                    * optmode : 委托方式
                    * reckoningAmt : 资金发生数
                    * postAmt : 资金余额
                    * currencyId : 货币
                    * exchId : 交易所
                    * contractNum : 合同序号
                    * stkId : 证券代码
                    * stkName : 证券名称
                    * knockPrice : 成交价格
                    * knockAmt : 成交金额
                    * fullknockamt : 全价成交金额
                    * knockQty : 成交数量(单位为委托单位)
                    * knockQtyF : 成交数量(支持小数位，场外开放基金会有小数)
                    * postQty : 股份余额
                    * undoFlagDesc : 冲正标志
                    * exteriorDesc : 摘要说明
                    * stampTax : 印花税
                    * commision : 手续费
                    * tradeTransFee : 过户费
                    * exchTransFee : 一级过户费
                    * reckoningFee : 清算费
                    * transruleFee : 交易规费
                    * perorderFee : 委托单费
                    * withdrawFee : 撤单单费
                    * knockFee : 成交单费
                    * exteriorAcctId : 外部帐号
                    * tradeCurrencyId : 交易币种(港股通业务用)
                    * exchRate : 结算汇率(港股通业务用)
                    * tradeReckoningAmt : 交易币种资金发生数(港股通业务用)
                    * settleKnockAmt : 结算币种成交金额(港股通业务用)
                    * settleFullKnockAmt : 结算币种全价成交金额(港股通业务用)
    '''


class MsgQueryUndueRepurchase(object):
    '''
    undueRepurchaseList           未到期回购列表

    :fieldmembers:  * acctId :资金账号
                    * exchId : 市场
                    * stkId : 证券代码
                    * regId : 股东代码
                    * rollbackDate : 购回日期
                    * rollbackAmt : 购回金额（平仓时使用）
                    * orderTime :回购委托时间
                    * knockQty : 成交数量
                    * knockPrice : 成交金额
                    * contractNum : 合同号
                    * deskId : 席位
                    * custId : 客户编号
                    * financeOrderFlag : 回购方向(0-买入融资,1-卖出融券)
                    * stkType : 证券类别
                    * deposit : 履约金
                    * bondId : 债券代码
                    * creditFundFlag : 信用资金帐户标志
                    * totalRollBackAmt : 累计已经购回金额
                    * totalKnockQty : 总成交数量
                    * needSettleQty : 未交收数量
                    * needSettleAmt : 在途资金
                    * exteriorAcctId : 外部帐号
                    * repurchaseDay : 交易期限(回购天数)
                    * targetDeskId : 对方席位代码
                    * registerNo : 登记结算编号
                    * knockCode : 成交编号
                    * knockAmt : 成交金额
                    * branchId : 所属营业部代码
                    * regName : 股东姓名
                    * stkName : 证券名称
                    * financeInterest : 借款利息

    '''


class ParaQueryUndueRepurchase(object):
    '''
    未到期回购查询参数

    :fieldmembers:  * queryCond : 查询条件
                        * acctId : 资金账号
                        * stkId : 证券代码(可选)
                    * maxRowNum : 最大查询记录数量(可选，默认为100)
                    * pageNum : 查询页数(可选，默认为1)
    '''

    queryCond = ''
    maxRowNum = ''
    pageNum = ''

    def __init__(self, queryCond, maxRowNum, pageNum):
        self.queryCond = queryCond
        self.maxRowNum = maxRowNum
        self.pageNum = pageNum


class QueryCond(object):
    '''
    queryCond查询公共类
    '''

class ParaQueryCDRMarketStrategyPara(object):
    '''
    沪伦通做市策略参数查询

    :fieldmembers:  * queryCond : 查询条件
                          * exchId : 市场(可选)
    '''
    queryCond = ''

    def __init__(self, queryCond):
        self.queryCond = queryCond

class MsgQueryMarketInfo(object):
    '''
    查询条件

    :fieldmembers:  * marketStrategyPara : 系统参数
                    * marketStrategyList : 报价参数
    '''
    marketStrategyPara = ''
    marketStrategyList = ''

class MsgMarketStrategyPara(object):
    '''
    marketStrategyPara            系统参数

    :fieldmembers:  * minOrderQty : 连续竞价最小报价数量（单位：份）
                    * minLimitOrderQty : 集合竞价最小报价数量（单位：份）
                    * priceDiffRate : 最大买卖价差（单位：%）
                    * exchRate : GBPCNY参考汇率
                    * amAggBeginTime : 开盘集合竞价开始时间时分
                    * amAggEndTime : 开盘集合竞价结束时间时分
                    * amTradeBeginTime : 上午连续竞价开始时间时分
                    * amTradeEndTime : 上午连续竞价结束时间时分
                    * pmTradeBeginTime : 下午连续竞价开始时间时分
                    * pmTradeEndTime : 下午连续竞价结束时间时分
                    * pmAggEndTime : 收盘集合竞价结束时间时分
                    * intervalTime : 集合竞价线程轮询间隔
                    * offerInterval : 连续竞价线程轮询间隔
    '''


class MsgMarketStrategyList(object):
    '''
    marketStrategyList[]          报价参数

    :fieldmembers:  * exchId : 市场
                    * stkId : 证券代码
                    * acctId : 资金账号
                    * regId : 股东代码
                    * starttime : 报价开始时间
                    * endtime : 报价结束时间
                    * flag : 豁免标志（*）（0-无豁免，1-买入豁免，2-卖出
                    * convertQty : 转换系数,例如：伦敦100股，转换1000份C
                    * basicClosePrice : 伦敦交易所收盘价
                    * minPosition : 帐户最低持仓（份）
                    * maxPosition : 帐户最高持仓（份）
                    * templateId : 模型代码
                    * templateName : 模型名称
                    * bidType : 报价策略（从CDR_Strategy获取，A-做市义务
                    * orderqty : 委托数量（份）
                    * stkRate3 : 价格初始偏移率（%）
                    * stkRate4 : 价格偏移率上限（%）
                    * stkRate5 : 价格偏移率下限（%）
                    * patchPriceIncrement : 初始理论价偏移量
                    * orderPriceIncrement : 每档价格偏移量
                    * orderRate  : 每档价格偏移比例
                    * enabledFlag : 启动标志（N表示未启动，Y表示已启动)
    '''


class ParaAddMessegeOnline(object):
    '''
    reqCond       请求参数

    :fieldmembers:  * reqCond ：请求参数
                        * exchId : 市场代码（exchid,必送）
                        * stkId : 证券代码（CDR,必送）
                        * orderType : 业务类型（openorder表的orderType,必送）
                        * message : 消息内容（证券代码stkid，APP返回的错误信息failinfo,必送）
                        * sendTime : 发送时间（当前时间,必送）
                        * grantOptList : 柜员列表（23010089对应exchid+stkid的authOptId,必送）
    '''
    reqCond = ''

    def __init__(self, reqCond):
        self.reqCond = reqCond

class ParaSysModel(object):
    '''
    reqCond       请求参数

    :fieldmembers:  * reqCond ：请求参数
                        * actionFlag : 操作标志（*）(送MOD)(必送)
                        * exchId : 市场(必送)
                        * stkId : 证券代码(必送)
                        * acctId : 资金账号(必送)
                        * bidType : 报价策略(送B)(必送)
                        * templateId : 模型代码(必送)
                        * enabledFlag : 启动标志（送N）(必送)
    '''
    reqCond = ''

    def __init__(self, reqCond):
        self.reqCond = reqCond


class ReqCond(object):
    '''
    查询公共类
    '''
    
class OrderInfo(object):
    '''
    非交易锁定解锁功能
    orderInfo 报单信息

    :fieldmembers:  * orderInfo : 报单信息
                       * acctId : 资金帐号(必送)
                       * exchId : 交易市场(必送)
                       * stkId : 证券代码(必送)
                       * orderType : 委托类型(必送)（B-解锁，S锁定）
                       * orderQty : 锁定解锁数量(必送)
                       * orderPrice : 委托价格(必送)
                       * regId : 股东代码(可选,默认报单市场的第一个股东)
                       * businessMark : 交易业务类型(必送)(OTO-期权订单，OTU-证券冻结与解冻，OTE-行权)
    '''
    acctId = ''
    exchId = ''
    stkId = ''
    orderType = ''
    orderQty = ''
    orderPrice = ''
    regId = ''
    businessMark = ''

class TradeOrderInfo(object):
    '''
    非交易锁定解锁功能
    orderInfo 报单信息

    :fieldmembers:  * orderInfo : 报单信息
                       * acctId : 资金帐号(必送)
                       * exchId : 交易市场(必送)
                       * stkId : 证券代码(必送)
                       * orderType : 委托类型(必送)（B-解锁，S锁定）
                       * orderQty : 锁定解锁数量(必送)
                       * orderPrice : 委托价格(必送)
                       * regId : 股东代码(可选,默认报单市场的第一个股东)
                       * businessMark : 交易业务类型(必送)(OTO-期权订单，OTU-证券冻结与解冻，OTE-行权)
    '''
    orderInfo = ''
    
    def __init__(self,orderInfo):
        self.orderInfo = orderInfo
      
class MsgOrderInfo(object):
    '''
      非交易锁定解锁功能
    msgOrderInfo 报单返回信息

    :fieldmembers:  * msgOrderInfo                 :报单返回信息
                       * contractNum               :合同号
    '''
    contractNum = ''