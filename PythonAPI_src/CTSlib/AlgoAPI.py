#coding=utf8
'''
Created on 2017年12月14日

Python API 服务
提供算法交易功能
'''
from CTSlib.ApiStruct import *
from CTSlib.ApiUtils import *

class AlgoServer():
    '''
   算法交易服务类
    '''
    def __init__(self, ctsServer):
        
        self.ctsServer = ctsServer
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ALGO_ORDER, self.onNewAlgoStrategy)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ALGO_WITHDRAW, self.onCancelAlgoStrategy)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ALGO_FORCEWITHDRAW, self.onForceCancelAlgoStrategy)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ALGO_QRY_STRATEGY, self.onQueryAlgoStrategy)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ALGO_QRY_DETAILORDER, self.onQueryAlgoDetailOrder)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ALGO_QRY_SUMORDER, self.onQueryAlgoSumOrder)
        self.ctsServer.addFunCallback(MsgTypeList.MSG_TYPE_ALGO_QRY_DETAILKNOCK, self.onQueryAlgoDetailKnock)
     
    def newAlgoStrategy(self, paraNewAlgoStrategy):
        """
        算法策略下单
        algoList    算法策略列表
        """
        # 创建发送数据包
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ALGO_ORDER, self.ctsServer.sessionId)
        msgRequest = {}
        msgRequest['algoList'] = paraNewAlgoStrategy

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)
        return reqDataValue.data
    
        
    def onNewAlgoStrategy(self, jsonData, msgRespond, msgHead):
        '''
        算法策略下单回调方法
        '''
        msgData = ''
        if (msgRespond.successFlg == 0 and "errorList" not in jsonData):
            Logger.debug("requestId:%s,算法策略下单成功！" %msgHead.requestId)
        else:
            Logger.debug("requestId:%s,算法策略下单失败！" %msgHead.requestId)
            msgData = []
            if ("errorList" in jsonData):
                msgDataList = jsonData["errorList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgNewAlgoStrategy()
                    msgDataDict.__dict__ = msgDataDictTmp
                    
                    msgData.append(msgDataDict)
                    
            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)
    
    
    def cancelAlgoStrategy(self, paraCancelAlgoStrategy):
        """
        算法策略撤单
        """
        # 创建发送数据包
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ALGO_WITHDRAW, self.ctsServer.sessionId)
        msgRequest = {}
        msgRequest['algoList'] = paraCancelAlgoStrategy

        msgData = MsgData(msgHead, msgRequest)

        
        reqDataValue = self.ctsServer.syncExchangeData(msgData)
        return reqDataValue.data
    
        
    def onCancelAlgoStrategy(self, jsonData, msgRespond, msgHead):
        '''
        算法策略撤单回调方法
        '''
        msgData = ''
        if (msgRespond.successFlg == 0 and "errorList" not in jsonData):
            Logger.debug("requestId:%s,算法策略撤单成功！" %msgHead.requestId)
        else:
            Logger.debug("requestId:%s,算法策略撤单失败！" %msgHead.requestId)
            msgData = []
            if ("errorList" in jsonData):
                msgDataList = jsonData["errorList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgCancelAlgoStrategy()
                    msgDataDict.__dict__ = msgDataDictTmp
                    
                    msgData.append(msgDataDict)
                    
            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)
            
    
    def forceCancelAlgoStrategy(self, paraForceCancelAlgoStrategy):
        """
        算法强制撤单
        """
        # 创建发送数据包
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ALGO_FORCEWITHDRAW, self.ctsServer.sessionId)
        msgRequest = {}
        msgRequest['algoList'] = paraForceCancelAlgoStrategy

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)
        return reqDataValue.data
    
        
    def onForceCancelAlgoStrategy(self, jsonData, msgRespond, msgHead):
        '''
        算法强制撤单回调方法
        '''
        msgData = ''
        if (msgRespond.successFlg == 0 and "errorList" not in jsonData):
            Logger.debug("requestId:%s,算法强制撤单成功！" %msgHead.requestId)
        else:
            Logger.debug("requestId:%s,算法强制撤单失败！" %msgHead.requestId)
            msgData = []
            if ("errorList" in jsonData):
                msgDataList = jsonData["errorList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgForceCancelAlgoStrategy()
                    msgDataDict.__dict__ = msgDataDictTmp
                    
                    msgData.append(msgDataDict)
                    
            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)

        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):

            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)
    
    
    
    #######################
    
    def queryAlgoStrategy(self, paraQueryAlgoStrategy):
        """
        算法策略查询
        """
        # 创建发送数据包
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ALGO_QRY_STRATEGY, self.ctsServer.sessionId)
        msgRequest = {}
        msgRequest['algoInfo'] = paraQueryAlgoStrategy

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)
        return reqDataValue.data
    
        
    def onQueryAlgoStrategy(self, jsonData, msgRespond, msgHead):
        '''
        算法策略查询回调方法
        '''
        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = []
            if ("algoList" in jsonData):
                msgDataList = jsonData["algoList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgQueryAlgoStrategy()
                    msgDataDict.__dict__ = msgDataDictTmp
                    
                    msgData.append(msgDataDict)
                    
            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)
    
    
    def queryAlgoDetailOrder(self, paraQueryAlgoDetailOrder):
        """
        算法报单明细查询
        """
        # 创建发送数据包
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ALGO_QRY_DETAILORDER, self.ctsServer.sessionId)
        msgRequest = {}
        msgRequest['algoInfo'] = paraQueryAlgoDetailOrder

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)
        return reqDataValue.data
    
        
    def onQueryAlgoDetailOrder(self, jsonData, msgRespond, msgHead):
        '''
        算法报单明细回调方法
        '''
        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = []
            if ("orderList" in jsonData):
                msgDataList = jsonData["orderList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgQueryAlgoDetailOrder()
                    msgDataDict.__dict__ = msgDataDictTmp
                    
                    msgData.append(msgDataDict)
                    
            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)
    
    def queryAlgoSumOrder(self, paraQueryAlgoSumOrder):
        """
        算法报单汇总查询
        """
        # 创建发送数据包
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ALGO_QRY_SUMORDER, self.ctsServer.sessionId)
        msgRequest = {}
        msgRequest['algoInfo'] = paraQueryAlgoSumOrder

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)
        return reqDataValue.data
    
        
    def onQueryAlgoSumOrder(self, jsonData, msgRespond, msgHead):
        '''
        算法报单汇总查询回调方法
        '''
        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = []
            if ("orderList" in jsonData):
                msgDataList = jsonData["orderList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgQueryAlgoSumOrder()
                    msgDataDict.__dict__ = msgDataDictTmp
                    
                    msgData.append(msgDataDict)
                    
            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)
            
    def queryAlgoDetailKnock(self, paraQueryAlgoDetailKnock):
        """
        指令成交查询
        """
        # 创建发送数据包
        msgHead = MsgHead(MsgTypeList.MSG_TYPE_ALGO_QRY_DETAILKNOCK, self.ctsServer.sessionId)
        msgRequest = {}
        msgRequest['algoInfo'] = paraQueryAlgoDetailKnock

        msgData = MsgData(msgHead, msgRequest)

        reqDataValue = self.ctsServer.syncExchangeData(msgData)
        return reqDataValue.data
    
        
    def onQueryAlgoDetailKnock(self, jsonData, msgRespond, msgHead):
        '''
        指令成交查询回调方法
        '''
        # 处理同步请求模式
        if (msgHead.requestId in self.ctsServer.reqMap):
            msgData = []
            if ("knockList" in jsonData):
                msgDataList = jsonData["knockList"]
                for msgDataDictTmp in msgDataList:
                    msgDataDict = MsgQueryAlgoDetailKnock()
                    msgDataDict.__dict__ = msgDataDictTmp
                    
                    msgData.append(msgDataDict)
                    
            self.ctsServer.handleSyncRequest2(msgHead.requestId, msgRespond, msgData)
    
class ParaNewAlgoStrategy():
    '''
    algoList[]                    算法策略列表

    :fieldmembers:   * instructId : 指令ID
                     * acctId : 资金帐户
                     * exchId : 交易市场
                     * stkId : 证券代码
                     * orderType : 买卖方向
                     * orderQty : 策略目标数量(对应intelligentOrder.totalQty)
                     * securityType : 证券类型（CS-现货，FUT-期货）
                     * f_offSetFlag : 开平标志（OPEN-开仓，CLOSE-平仓）(期货必送)
                     * f_hedgeFlag : 投保标记（SPEC-投机，HEDGE-套保，ARB-套利）
                     * priceMode : 价格策略（1--限价，3--市价）
                     * orderPrice  : 委托价格
                     * fixText  : Tag58
                     * strategyType  : 策略类型标识
                     * offerStartTime  : 策略开始执行时间(Tag6062；必送；允许修改)
                     * offerStopTime  : 策略结束执行时间(Tag6063；必送；允许修改)
                     * expireTime  : 策略时效时间(Tag126；可选，默认为offerStopTime；允许修改；一般offerStopTime后，ALGO不会继续发送订单，但是需要等待到expiryTime时，UBS才会给出订单全部完成或者是unsolicited cancel的处理；相当于需要有一段时间继续处理在交易所的在途数据)
                     * fixTargetSubId  : 发送目标
                     * orderPosition  : 报单盘口
                         * SP1  : 本方盘口1
                         * OP1  : 对方盘口1
                         * MXP  : 涨停价
                         * MNP  : 跌停价
                         * SP5  : 本方盘口5
                         * OP5  : 对方盘口5
                     * orderTick  : 报单偏差
                     * appendPostion  : 补单盘口
                         * SP1  : 本方盘口1
                         * OP1  : 对方盘口1
                         * MXP  : 涨停价
                         * MNP  : 跌停价
                         * SP5  : 本方盘口5
                         * OP5  : 对方盘口5
                     * appendTick : 补单偏差
                     * cancelCycle : 撤单周期
                         * 单位说明：TWAP-报单间隔倍数
                     * numRate：量比比例
                     * secondTime：twap_v7第二阶段时间
                     * firstPosition：twap_v7第一阶段报价
                         * SP1  : 本方盘口1
                         * OP1  : 对方盘口1
                         * SP5  : 本方盘口5
                         * OP5  : 对方盘口5
                     * secondPosition：twap_v7第二阶段报价
                         * SP1  : 本方盘口1
                         * OP1  : 对方盘口1
                         * SP5  : 本方盘口5
                         * OP5  : 对方盘口5
                     * orderQtyInTotalQtyRate: 已报数量占总委托量比例
                     * knockQtyInOrderQtyRate: 已成交数量占已委托比例
                     * limitPrice: 限价价格
                     * openSpeed: 开盘集合竞价是连续竞价的倍数
                     * visibleRate: 可见比例(冰山策略)
                     * strategyStyle: 策略风格
                         * 1 : 紧
                         * 3 : 正常
                         * 5 : 宽
                     * instructType: 策略类型
                     * orderAmt: 策略金额
                     * customAlgosId: 策略ID
                     * actionFlag: 支持设置涨跌停价格标志
                     * keepPriceFlag: 保留限价挂单
                     * parameter: 特殊参数汇总列表
                     * insiderFlag: 策略标识（Y表示根网算法策略，N表示外部ALGO策略）
                     * algoDefaultPara: 策略参数组

    '''
    
class MsgNewAlgoStrategy():
    '''
    errorList[]                     错误返回列表

    :fieldmembers:   * instructId : 指令ID
                     * exchId: 交易市场
                     * stkId: 证券代码
                     * errorCode: 错误代码
                     * failInfo: 中文失败信息
                     * englishFailInfo: 英文失败信息

    '''
    
class ParaCancelAlgoStrategy():
    '''
    algoList[]                    算法策略列表

    :fieldmembers:   * instructId : 指令ID
                     * acctId : 资金帐户
                     * exchId : 交易市场
                     * stkId : 证券代码
                     * batchNum : 策略批号

    '''
    
class MsgCancelAlgoStrategy():
    '''
    errorList[]                     错误返回列表

    :fieldmembers:   * instructId : 指令ID
                     * exchId : 交易市场
                     * stkId : 证券代码
                     * errorCode : 错误代码
                     * failInfo : 中文失败信息
                     * englishFailInfo: 英文失败信息

    '''
    
class ParaForceCancelAlgoStrategy():
    '''
    algoList[]                    算法策略列表

    :fieldmembers:   * instructId : 指令ID
                     * acctId : 资金帐户
                     * exchId : 交易市场
                     * stkId : 证券代码
                     * batchNum : 策略批号
    '''
    
class MsgForceCancelAlgoStrategy():
    '''
    errorList[]                     错误返回列表

    :fieldmembers:   * instructId : 指令ID
                     * exchId : 交易市场
                     * stkId : 证券代码
                     * errorCode : 错误代码
                     * failInfo : 中文失败信息
                     * englishFailInfo : 英文失败信息

    '''
    
    
    
#########################################    
    
class ParaQueryAlgoStrategy():
    '''
    algoInfo                      算法策略信息

    :fieldmembers:   * instructId : 指令ID
                     * securityType : 证券类别
                     * algoStatus : 策略状态（可选）
                     * stkId : 证券代码（可选）

    '''
    
class MsgQueryAlgoStrategy():
    '''
    algoList                      算法策略列表

    :fieldmembers:  * instructId : 指令ID
                    * acctId : 资金账号
                    * exchId : 市场
                    * stkId : 证券代码
                    * stkName : 证券名称
                    * orderType : 委托方向
                    * f_offSetFlag : 开平标志（OPEN-开仓，CLOSE-平仓）
                    * f_hedgeFlag : 投保标记（SPEC-投机，HEDGE-套保，ARB-套利）
                    * batchNum : 策略批号
                    * offerStartTime : 策略起始时间
                    * offerStopTime : 策略结束时间
                    * totalQty : 策略数量
                    * offerStrategy : 策略类型
                    * offerStatus : 报盘状态(0未执行, 1开始执行, 2暂停, 3完成, 4暂停之后继续完成)
                    * algoStatus : 策略状态
                        * 1 : 正常
                        * 2 : 撤销中
                        * 3 : 强制撤销中
                        * 4 : 策略修改中
                        * 5 : 已撤销
                        * 6 : 已完成
                    * F_orderStatus : FIX链接状态
                    * knockQty : 成交数量
                    * cancelTime : 策略撤销时间
                    * forceCancelTime : 策略强制撤销时间
                    * remarktime : 超时时间
                    * clOrdId : Strategy Order 合同号码（Tag11）
                    * nextClOrdId : 执行中的Strategy Order合同号码
                    * sendTime : 发送时间
                    * orderPrice : 委托价格
                    * strategyType : 策略名称(Tag6061)
                    * expireTime  : 策略时效时间(Tag126)
                    * numRate  : 量比比例(Tag6064)
                    * minNumRate : 最小量比比例(Tag6067)
                    * strategyStyle  : 策略风格(Tag6065)
                    * displaySize : 在途数量(Tag111)
                    * minDisplaySize : 最少在途数量(Tag6317)
                    * referencePrice : 参考价格(Tag6087)
                    * opg : 开盘集合竞价(Tag6075)
                    * moc : 收市价格(Tag6076)
                    * stopPrice : 止损价格(Tag99)
                    * limitPriceVol : 限价量比(Tag6298)
                    * resetVolOnAmend : 量比修改后生效时机(Tag6297)
                    * refIndex : 参考指数(Tag6073)
                    * refIndexPxIntercept : 触发拦截的指数点位(Tag6071)
                    * traderId : senderSubID(Tag50)
                    * knockAmt : 成交金额
                    * FixText  : 策略备注
                    * salesId : 指令管理员
                    * memo  : 指令明细中的备注
                    * FixTargetSubId : 发送目标
                    * dispatchMode : (实际是获取fixalgo_parentorder.interiorId填写：表示"Scale实例组ID"，其中：0-手动指定实例组，1-APP自动指定实例组，2-DSA)
                    * constDisplayName : dispatchmode在GlobalConstCust中对应的constDisplayName，英文描述
                    * instrucType : 策略类型
                    * orderAmt : 策略金额
                    * customAlgosId : 策略ID
                    * description : 备注
                    * securityType : 证券类别
                    * actionFlag : 支持设置涨跌停价格标志
                    * keepPriceFlag : 保留限价挂单
                    * parameter : 特殊参数汇总列表
                    * insiderFlag : 策略标识（Y表示根网算法策略，N表示外部ALGO策略）
                    * algoDefaultPara :策略参数组
                    * orderPosition : 报单盘口
                        * SP1 : 本方盘口1
                        * OP1 : 对方盘口1
                        * MXP : 涨停价
                        * MNP : 跌停价
                        * SP5 : 本方盘口5
                        * OP5 : 对方盘口5
                    * orderTick : 报单偏差
                    * appendPostion : 补单盘口
                        * SP1 : 本方盘口1
                        * OP1 : 对方盘口1
                        * MXP : 涨停价
                        * MNP : 跌停价
                        * SP5 : 本方盘口5
                        * OP5 : 对方盘口5
                    * appendTick : 补单偏差
                    * cancelCycle : 撤单周期
                        * 单位说明：TWAP:报单间隔倍数
                    * numRate : 量比比例
                    * secondTime : twap_v7第二阶段时间
                    * firstPosition : twap_v7第一阶段报价
                        * SP1:本方盘口1
                        * OP1:对方盘口1
                        * SP5:本方盘口5
                        * OP5:对方盘口5
                    * secondPosition : twap_v7第二阶段报价
                        * SP1:本方盘口1
                        * OP1:对方盘口1
                        * SP5:本方盘口5
                        * OP5:对方盘口5
                    * orderQtyInTotalQtyRate : 已报数量占总委托量比例
                    * knockQtyInOrderQtyRate : 已成交数量占已委托比例
                    * limitPrice : 限价价格
                    * openSpeed : 开盘集合竞价是连续竞价的倍数
                    * visibleRate : 可见比例(冰山策略)
    '''
    
class ParaQueryAlgoDetailOrder():
    '''
    algoInfo                      算法策略信息

    :fieldmembers:  * instructId : 指令ID（必送）
                    * securityType : 证券类型（CS-股票，FUT-期货）
                    * stkId : 证券代码（必送）
                    * batchNum : 策略批号（必送）
                    * queryType : 查询类型（必送，0-未完成，1-全部含撤单，2-全部不含撤单)
                    * beginTime : 起始时间（必送，HH:MM:SS）
                    * endTime : 截止时间（必送，HH:MM:SS）

    '''
    
class MsgQueryAlgoDetailOrder():
    '''
    orderList                     算法报单列表

    :fieldmembers:  * batchNum : 策略批号
                    * orderTime : 委托时间
                    * acctId : 资金账号
                    * regId : 股东帐户
                    * exchId : 交易所代码
                    * stkId : 证券代码
                    * stkName : 证券名称
                    * orderType : 委托类型
                    * f_offSetFlag : 开平标志（OPEN-开仓，CLOSE-平仓）
                    * f_hedgeFlag : 投保标记（SPEC-投机，HEDGE-套保，ARB-套利）
                    * orderQty : 委托数量
                    * orderPrice : 委托价格(精确到小数点后3位)
                    * contractNum : 合同序号
                    * knockQty : 成交数量
                    * knockAmt : 成交金额
                    * withdrawQty : 撤单数量
                    * withdrawFlag : 撤单标志（F-委托，T-撤单）
                    * validFlag : 合法标志
                    * orderStatus : 委托状态
                    * exchErrorCode : 交易所错误代码
                    * memo : 备注

    '''

class ParaQueryAlgoSumOrder():
    '''
    algoInfo        策略报单汇总查询参数
    
    :fieldmembers:  * instructId : 指令ID(必送)
                    * stkId : 证券代码(可选)
                    * batchNum : 策略批号（必送）

    '''
    
class MsgQueryAlgoSumOrder():
    '''
    orderList        策略报单汇总查询返回
    
    :fieldmembers:  * instructId : 指令ID
                    * batchNum : 策略批号
                    * acctId : 资金帐号
                    * exchId : 市场
                    * stkId : 证券代码
                    * regId : 股东代码
                    * orderType : 买卖反向
                    * f_offSetFlag : 开平标志（OPEN-开仓，CLOSE-平仓）
                    * orderQty : 委托数量
                    * knockQty : 成交数量
                    * orderAmt : 委托金额
                    * knockAmt : 成交金额
                    * knockAvgPx : 成交均价

    '''
    
class ParaQueryAlgoDetailKnock():
    '''
    algoInfo        策略成交明细查询参数
    
    :fieldmembers:  * instructId : 指令ID
                    * securityType : 证券类型（CS-股票，FUT-期货）
                    * batchNum : 批号

    '''
    
class MsgQueryAlgoDetailKnock():
    '''
    knockList         策略成交明细查询返回

    :fieldmembers: * instructId : 指令代码
                   * acctId : 资金帐号
                   * orderType : 买卖方向
                   * f_offSetFlag : 开平标志（OPEN-开仓，CLOSE-平仓）
                   * f_hedgeFlag : 投保标记（SPEC-投机，HEDGE-套保，ARB-套利）
                   * stkId : 证券代码
                   * stkName : 证券名称
                   * batchNum : 批号
                   * contractNum : 合同号
                   * orderQty : 指令数量
                   * knockQty : 成交数量
                   * exchId : 市场
                   * regId : 股东代码
                   * status : 执行状态
                       * 0 : 完全成交
                       * 1 : 部分成交
                   * knockTime : 成交时间
                   * knockPrice : 成交价格
                   * knockAmt : 成交金额

    '''