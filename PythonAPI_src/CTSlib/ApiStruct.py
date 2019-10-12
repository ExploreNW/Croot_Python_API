# coding=utf-8
"""
Python API 接口
提供行情、交易接口结构

"""
from CTSlib.SysUtils import *

sequenceManager = SequenceManager()

class MsgHead(object):
    """
    通讯数据包头类
    """
    
    # 功能类型
    msgType = 0
    
    # 会话序号
    sessionId = ""
    
    # 请求序号
    requestId = 0

    def __init__(self, msgType, sessionId = "-1", requestId = 0):
        
        self.msgType = msgType
        self.sessionId = sessionId
        self.requestId = sequenceManager.getNextId()
        

class MsgRespond(object):
    """
    通讯数据响应类

    :fieldmembers: * successFlg : 成功标记(0-成功，1-失败)
                   * errorCode : 错误代码
                   * errorMsg : 错误信息
                   * lastFlag : 数据包是否最后一个

    """
    
    # 成功标记(0-成功，1-失败)
    successFlg = 0
    
    # 错误代码
    errorCode = ""
    
    # 错误信息
    errorMsg = ""

    #数据包是否最后一个
    lastFlag = True
    
    def __init__(self, successFlg = 0, errorCode = "", errorMsg = "", lastFlag = True):
        
        self.successFlg = successFlg
        self.errorCode = errorCode
        self.errorMsg = errorMsg
        self.lastFlag = lastFlag


class MsgData(object):
    
    head = None
    
    request = None
    
    respond = None
    
    data = None
    
    def __init__(self, msgHead = None, request = None):
        
        self.head = msgHead
        self.request = request


class MsgConnectInfo(object):
    """
    服务器连接信息

    :fieldmembers:  * sysDate : 系统时间
                    * sysVersion : 系统版本号
                    * customer : 客户名称
                    * serverName : 服务器名称
                    * expireDate : 过期日期

    """


class MsgDisConnectInfo(object):
    """
    服务器断开信息

    :fieldmembers:  * sysDate : 系统时间

    """


class ParaStkInfo(object):
    """
    行情查询

    :fieldmembers: * exchId : 交易市场
                   * stkId : 证券代码
    """

    exchId = ""
    stkId = ""

    
    def __init__(self, exchId, stkId):
        
        self.exchId = exchId
        self.stkId = stkId

class MsgQueryFutureInfo (object):
    """
    futureInfo                  期货合约基本信息

    :fieldmembers:  * exchId : 市场
                    * f_productId : 品种
                    * stkId : 合约代码
                    * stkName : 合约名称
                    * stkStatus : 合约状态
                    * basicExchId : 标的证券所在市场
                    * basicStkId : 标的证券代码
                    * contractTimes : 合约乘数
                    * deliveryType : 交割方式
                    * deliveryYear : 交割年份
                    * deliveryMonth : 交割月份
                    * listDate : 上市日
                    * firstTrdDate : 首交易日
                    * lastTrdDate : 最后交易日
                    * matureDate : 到期日
                    * lastSettleDate : 最后结算日
                    * deliveryDate : 交割日
                    * stkOrderStatus : 合约交易状态
                    * stkOrderStatusDesc : 合约交易状态描述
                    * orderPriceUnit : 价格档位
                    * maxLimitOrderQty : 限价委托上限数量(每笔最大限量)
                    * maxMarketOrderQty : 市价委托上限数量(每笔最大限量)
                    * minLimitOrderQty : 限价委托下限数量(每单最小数量单位)
                    * minMarketOrderQty : 市价委托下限数量(每单最小数量单位)
                    * maxOrderPrice : 委托价格上限、上限价(涨停价格)
                    * minOrderPrice : 委托价格下限、下限价(跌停价格)
                    * upPercent : 涨幅比例
                    * downPercent : 跌幅比例
                    * preSettlementPrice : 昨日结算价
                    * preClosePrice : 昨收盘
                    * preOpenPosition : 市场昨持仓量
                    * openPrice : 开盘价
                    * highestPrice : 最高价
                    * lowestPrice : 最低价
                    * exchTotalKnockQty : 当天交易所总成交数量
                    * exchTotalKnockAmt : 当天交易所总成交金额
                    * openPosition : 市场持仓量
                    * closePrice : 收盘价
                    * settlementPrice : 结算价(全价)
                    * preDelta : 昨虚实度
                    * delta : 今虚实度
                    * basicStkType : 标的证券类型
                    * basicPreClosePrice : 标的证券昨收盘
                    * strikeStyle : 行权方式
                    * exerciseDate : 行权-行权日
                    * currMargin : 当前保证金总额
                    * stkType : 证券类型
                    * optionStkId : 权证代码
                    * newPrice : 最新价
                    * strikePrice : 行权价格
                    * optionType : 权证类型
                    * optExecType : 期权执行方式(0欧式，1 美式)
                    * marginRate1 : 保证金比率1
                    * marginRate2 : 保证金比率2
                    * optionMonth : 合约到期月份类型
                    * adjustedFlag : 是否调整标志(Y-是,N-否)
                    * preContractTimes : 上一交易日合约乘数
                    * expireType : 过期类型
                    * lastUpdateDate : 最后修改日期

    """

class MsgStkInfo(object):
    """
    stkInfo                      证券信息

    :fieldmembers:  * exchId : 交易市场
                    * stkId : 证券代码
                    * stkName : 证券名称
                    * newPrice : 最新价格
                    * openPrice : 开盘价格
                    * closePrice : 昨收盘价
                    * buyPrice : 买盘价格
                    * sellPrice : 卖盘价格
                    * buyAmt : 买盘数量
                    * sellAmt : 卖盘数量
                    * closeFlag : 停牌标记
                    * highPrice : 今日最高
                    * lowPrice : 今日最低
                    * maxOrderPrice : 价格上限
                    * minOrderPrice : 价格下限
                    * knockQty : 成交数量
                    * knockAmt : 成交金额
                    * preClosePrice : 昨收盘价格
                    * preSettlementPrice : 昨日结算价
                    * F_productId : 产品内部编码
                    * basicExchId : 标的证券所在市场
                    * basicStkId : 标的证券代码
                    * F_BasisPrice : 挂牌基准价
                    * settleGrp : 结算组
                    * settleID : 结算编号
                    * stkOrderStatus : 合约交易状态
                    * preOpenPosition : 市场昨持仓量
                    * highestPrice : 最高价
                    * lowestPrice : 最低价
                    * exchTotalKnockQty : 当天交易所总成交数量
                    * exchTotalKnockAmt : 当天交易所总成交金额
                    * openPosition : 市场持仓量
                    * settlementPrice : 结算价
                    * preDelta : 昨虚实度
                    * delta : 今虚实度
                    * lastModifyTime : 最后修改时间
                    * mseconds : 最后修改毫秒
                    * contractTimes : 合约乘数
                    * deliveryDate : 交割日
                    * endDays : 计息截止天
                    * estimate : 约用资金
                    * beginPrice : 开始价格
                    * endPrice : 结束价格
                    * stkType : 证券类别
                    * lastTrdDate : 最后交易日
                    * orderPriceUnit : 价格单位
                    * qtyPerHand : 每手数量
                    * strikePrice : 行权价格
                    * optionType : 期权类型(P-看涨期权，C-看跌期权)
                    * optExecType : 期权执行方式(0-欧式，1-美式)
                    * optionStkId : 期权证券代码
                    * stkStatus : 合约状态
                    * stkStatusDesc : 合约状态描述
                    * deliveryType : 交割方式
                    * deliveryYear : 交割年份
                    * deliveryMonth : 交割月
                    * listDate : 上市日
                    * firstTrdDate : 首交易日
                    * matureDate : 到期日
                    * lastSettleDate : 最后结算日
                    * stkOrderStatusDesc : 合约交易状态描述
                    * maxLimitOrderQty : 限价委托上限数量
                    * maxMarketOrderQty : 市价委托上限数量
                    * upPercent : 涨幅比例
                    * downPercent : 跌幅比例
                    * tradeUnit : 交易单位
                    * basicStkType : 标的证券类型(EBS-ETF，ASH-A股,IDX-指数)
                    * basicPreClosePrice : 标的证券昨收盘
                    * strikeStyle : 行权方式欧式美式(欧式-E,美式-A)
                    * exerciseDate : 行权日(T+1)
                    * currMargin : 个股期权持空仓单位保证金
                    * referencePrice : 参考价格

    """


class ParaAccount(object):
    """
    账户登录参数
    """
    acctId = ""
    password = ""
    F_TerminalOut = ""
    AppId = ""
    operationMAC = ""

    def __init__(self, acctId, password):
        self.acctId = acctId
        self.password = password

class MsgAccount(object):
    """
    acctInfo                     账户信息

    :fieldmembers:  * acctId : 资金帐号
                    * acctName : 帐户姓名
                    * currencyId : 币种代码
                    * currentAmt : 资金余额
                    * usableAmt : 可用金额
                    * creditFundFlag : 帐户类型（0-现货帐户 9-期货帐户）
                    * sysDate : 系统时间
                    * regList : 股东信息列表
                        * exchId : 交易市场
                        * regId : 股东代码
                        * regName : 股东姓名

    """

class ParaOptLogin(object):
    """
    柜员登录参数
    """
    optId = ""
    password = ""

    def __init__(self, optId, password):
        self.optId = optId
        self.password = password


class ParaOrderNew(object):
    """
    orderInfo                    报单信息

    :fieldmembers: * acctId : 资金帐号(必送)
                   * currencyId : 资金代码(期货期权必送)
                   * exchId : 交易市场(必送)
                   * stkId : 证券代码(必送)
                   * orderType : 委托类型(现货必送)
                   * orderPrice : 委托价格(必送)
                   * orderQty : 委托数量(必送)
                   * contractNum : 合同序号(可选)
                   * regId : 股东代码(可选,默认报单市场的第一个股东)
                   * batchNum : 委托批号(可选)
                   * clientId : 客户端编号(可选)
                   * f_offSetFlag : 开平标记（OPEN-开仓，CLOSE-平仓）(期货期权必送)
                   * bsFlag : 委托类型（B-多头，S-空头）(期货期权必送)
                   * f_orderPriceType : 价格类型（ANY-任意价，LIMIT-限价）(期货期权必送)
                   * f_hedgeFlag : 投保标记 (可选)
                   * coveredFlag : 备兑标签(可选)(0-非备兑,1-备兑)
                   * businessMark : 交易业务类型(可选)(OTO-期权订单，OTU-证券冻结与解冻，OTE-行权)
                   * F_TerminalId : 期货终端信息采集ID

    """
    orderInfo = ""
    F_TerminalId = ""
    
    def __init__(self, orderInfo):
        self.orderInfo = orderInfo


class OrderNewInfo(object):
    '''
    orderInfo                    报单信息

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * currencyId : 资金代码(期货期权必送)
                    * exchId : 交易市场(必送)
                    * stkId : 证券代码(必送)
                    * orderType : 委托类型(现货必送)
                        * B : 普通买入
                        * S : 普通卖出
                        * YB : 对手最优价买(市价委托,exchId=1)
                        * YS : 对手最优价卖(市价委托,exchId=1)
                        * XB : 本方最优价买(市价委托,exchId=1)
                        * XS : 本方最优价卖(市价委托,exchId=1)
                        * 2B : 即时成交买(市价委托,exchId=1)
                        * 2S : 即时成交卖(市价委托,exchId=1)
                        * VB : 最优五档买(市价委托,exchId=0,1)
                        * VS : 最优五档卖(市价委托,exchId=0,1)
                        * WB : 全额成交买(市价委托,exchId=0,1)
                        * WS : 全额成交卖(市价委托,exchId=0,1)
                    * orderPrice : 委托价格(必送)
                    * orderQty : 委托数量(必送)
                    * contractNum : 合同序号(可选)
                    * regId : 股东代码(可选,默认报单市场的第一个股东)
                    * batchNum : 委托批号(可选)
                    * clientId : 客户端编号(可选)
                    * f_offSetFlag : 开平标记（OPEN-开仓，CLOSE-平仓）(期货期权必送)
                    * bsFlag : 委托类型（B-多头，S-空头）(期货期权必送)
                    * f_orderPriceType : 价格类型（ANY-任意价，LIMIT-限价）(期货期权必送)
                    * f_hedgeFlag : 投保标记 (可选)
                    * coveredFlag : 备兑标签(可选)(0-非备兑,1-备兑)
                    * businessMark : 交易业务类型(可选)(OTO-期权订单，OTU-证券冻结与解冻，OTE-行权)

    '''
    orderInfo = ""
    acctId = ""
    currencyId = ""
    exchId = ""
    stkId = ""
    orderType = ""
    orderPrice = ""
    orderQty = ""
    contractNum = ""
    regId = ""
    batchNum = ""
    clientId = ""
    f_offSetFlag = ""
    bsFlag = ""
    f_orderPriceType = ""
    f_hedgeFlag = ""
    coveredFlag = ""
    businessMark = ""

class QuoteOrderNewInfo(object):
    '''
    orderInfo                    双边报单信息

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * currencyId : 资金代码(期货期权必送)
                    * exchId : 交易市场(必送)
                    * stkId : 证券代码(必送)
                    * orderType : 委托类型(现货必送)
                        * B : 普通买入
                        * S : 普通卖出
                        * YB : 对手最优价买(市价委托,exchId=1)
                        * YS : 对手最优价卖(市价委托,exchId=1)
                        * XB : 本方最优价买(市价委托,exchId=1)
                        * XS : 本方最优价卖(市价委托,exchId=1)
                        * 2B : 即时成交买(市价委托,exchId=1)
                        * 2S : 即时成交卖(市价委托,exchId=1)
                        * VB : 最优五档买(市价委托,exchId=0,1)
                        * VS : 最优五档卖(市价委托,exchId=0,1)
                        * WB : 全额成交买(市价委托,exchId=0,1)
                        * WS : 全额成交卖(市价委托,exchId=0,1)
                    * orderPrice : 委托价格(必送)
                    * orderQty : 委托数量(必送)
                    * contractNum : 合同序号(可选)
                    * regId : 股东代码(可选,默认报单市场的第一个股东)
                    * batchNum : 委托批号(可选)
                    * clientId : 客户端编号(可选)
                    * f_offSetFlag : 开平标记（OPEN-开仓，CLOSE-平仓）(期货期权必送)
                    * bsFlag : 委托类型（B-多头，S-空头）(期货期权必送)
                    * f_orderPriceType : 价格类型（ANY-任意价，LIMIT-限价）(期货期权必送)
                    * f_hedgeFlag : 投保标记 (可选)
                    * coveredFlag : 备兑标签(可选)(0-非备兑,1-备兑)
                    * businessMark : 交易业务类型(可选)(OTO-期权订单，OTU-证券冻结与解冻，OTE-行权)
                    * orderSource : 订单来源(可选)

    '''
    orderInfo = ""
    acctId = ""
    currencyId = ""
    exchId = ""
    stkId = ""
    orderType = ""
    orderPrice = ""
    orderQty = ""
    contractNum = ""
    regId = ""
    batchNum = ""
    clientId = ""
    f_offSetFlag = ""
    bsFlag = ""
    f_orderPriceType = ""
    f_hedgeFlag = ""
    coveredFlag = ""
    businessMark = ""
    orderSource = ""


class OrderCancelInfo(object):
    '''
    撤单信息

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * exchId : 交易市场(必送)
                    * contractNum : 合同序号(必送)

    '''
    acctId = ""
    exchId = ""
    contractNum = ""

class QuoteOrderCancelInfo(object):
    '''
    双边撤单信息

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * exchId : 交易市场(必送)
                    * contractNum : 合同序号(必送)

    '''
    acctId = ""
    exchId = ""
    contractNum = ""

class MsgOrderNew(object):
    '''
    报单信息

    :fieldmembers:  * contractNum : 合同号
                    * orderAmt : 委托金额
                    * usableAmt : 可用金额

    '''

class MsgQuoteOrderNew(object):
    '''
    双边报单信息

    :fieldmembers:  * contractNum : 合同号
                    * batchNum : 批号
                    * bsFlag : 买卖方向
                    * f_offsetFlag : 开平标记(OPEN-开仓，CLOSE-平仓)
    '''


class ParaOrderCancel(object):
    '''
    orderCancelInfo             撤单功能

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * exchId : 交易市场(必送)
                    * contractNum : 合同序号(必送)
                    * F_TerminalId : 期货终端信息采集ID

    '''

    orderCancelInfo = ""
    F_TerminalId = ""

    def __init__(self, orderCancelInfo):
        self.orderCancelInfo = orderCancelInfo


class MsgOrderCancel(object):
    '''
    撤单信息

    撤单成功 Fieldmembers:
        * contractNum : 合同序号
        * completeNum : 成功笔数
        * orderTime : 委托时间

    撤单失败 Fieldmembers:
        * acctId : 资金帐号(必送)
        * exchId : 交易市场(必送)
        * contractNum : 合同序号

    '''

class MsgQuoteOrderCancel(object):
    '''
    双边撤单信息

    撤单成功 Fieldmembers:
        * contractNum : 合同序号
        * completeNum : 成功笔数
        * orderTime : 委托时间
        * failInfo : 错误信息
        * errorCode : 错误代码

    撤单失败 Fieldmembers:
        * ErrorCode : 错误代码
        * errorMsg : 错误信息
        * contractNum : 合同序号

    '''


class ParaAccontQuery(object):
    '''
    资金账号查询

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * currencyId : 币种(必送)

    '''

    acctId = ""
    currencyId = ""

    def __init__(self, acctId, currencyId):
        self.acctId = acctId
        self.currencyId = currencyId


class ParaQueryFutAcctInfo(object):
    '''
    资金账号查询

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * currencyId : 币种(必送)

    '''

    acctId = ""
    currencyId = ""

    def __init__(self, acctId, currencyId):
        self.acctId = acctId
        self.currencyId = currencyId


class MsgAccontQuery(object):
    '''
    acctInfo                     账户信息

    :fieldmembers:  * acctId : 资金帐号
                    * currencyId : 币种
                    * currencyName : 货币名称
                    * custId : 客户帐号
                    * custName : 客户姓名
                    * currentAmt : 余额
                    * usableAmt : 可用数
                    * stkValue : 证券市值
                    * tradeFrozenAmt : 交易冻结
                    * exceptFrozenAmt : 异常冻结
                    * currentStkValue : 参考市值
                    * creditFundFlag : 信用资金标志
                    * acctAtRiskLevel : 帐户风险承受等级

    '''


class MsgQueryFutAcctInfo(object):
    '''
    acctInfo                      账户信息

    :fieldmembers:  * acctId : 资金帐户
                    * currencyId : 币种代码
                    * acctName : 帐户姓名
                    * custType : 客户类别
                    * custId : 客户代码
                    * currentAmt : 当前余额
                    * usableAmt : 可用余额（实时计算）
                    * realtimeAmt : 权益（实时计算）
                    * closePNL : 平仓盈亏
                    * realtimePNL : 实时盈亏（实时计算）
                    * ydMarginUsedAmt : 昨日保证金占用
                    * marginUsedAmt : 当日保证金占用（实时计算）
                    * tradeFrozenAmt : 交易冻结金额
                    * cashMovementAmt : 当日出入金
                    * commision : 手续费用
                    * marginAmt : 实时保证金占用
    '''


class ParaSubQuote(object):
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


class SubQuotaContent(object):
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


class MsgSubQuoteReturn(object):
    '''
    quotaInfo                    行情信息

    :fieldmembers:  * exchId : 市场
                    * stkId : 证券代码
                    * newPrice : 最新价
                    * highPrice : 今日最高价
                    * lowPrice : 今日最低价
                    * closePrice : 昨收盘
                    * buy : 买盘价
                    * buyAmt : 买盘量
                    * sell : 卖盘价
                    * sellAmt : 卖盘量
                    * referencePrice : 参考价格
                    * openPosition : 持仓量
                    * exchTotalKnockQty : 成交量
                    * exchTotalKnockAmt : 成交金额
                    * lastModifyTime : 行情时间
                    * bidOrders : 买一委托队列
                    * askOrders : 卖一委托队列

    '''


class ParaSubscriptTrade(object):
    """
    成交订阅

    :fieldmembers: * acctId : 资金账号(必送)
                   * pwd : 交易密码(必送)
                   * subType : 订阅类型(必送，默认为0) 0-订阅 1-退订
                   * clientId : 客户端编号(可选)
    """
    # 资金账号
    acctId = ''
    # 密码
    password = ''
    # 0-订阅，1-退订（必送）
    subType = ''
    # 客户端编号(可选)
    clientId = ''


    def __init__(self, acctId, pwd, subType, clientId):
        self.acctId = acctId
        self.password = pwd
        self.subType = subType
        self.clientId = clientId


class MsgSubscriptTradeReturn(object):
    '''
    subKnockInfo                    账户信息

    :fieldmembers:  * acctId : 资金帐号
                    * exchId : 市场
                    * stkId : 证券代码
                    * orderQty : 委托数量
                    * orderPrice : 委托价格
                    * contractNum : 合同号
                    * orderType : 买卖方向
                    * returnType : 回报类型
                    * tradingResultType : 成交类型
                    * knockQty : 成交数量
                    * knockPrice : 成交价格
                    * knockAmt : 成交金额
                    * fullKnockAmt : 全价成交金额
                    * reckoningAmt : 清算金额
                    * accuredInterestAmt : 应计利息金额
                    * accuredInteres : 应计利息
                    * knockTime : 交易所成交时间
                    * knockCode : 交易所成交编号
                    * serialNum : 根网内部成交编号
                    * exchErrorCode : 交易所错误编码
                    * memo : 交易所错误编码描述
                    * regId : 市场股东代码
                    * stkType : 证券类别
                    * tradeType : 交易类型
                    * f_offSetFlag : 开平标记
                    * closePNL : 平仓盈亏
                    * openUsedMarginAmt : 今开占用保证金
                    * offsetMarginAmt : 平仓释放保证金
                    * bsFlag : 买卖标志
                    * batchNum : 委托批号
                    * ownerType : 订单所有类型
                    * orderTime : 委托时间
                    * f_hedgeFlag : 投保标记
                    * clientId : 客户端编号(可选)
    '''


class QueryOrderCond(object):
    '''
    queryCond                    查询条件

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * exchId : 市场代码(可选)
                    * batchNum : 批号(可选)
                    * contractNum : 合同号(可选)
                    * stkId : 证券代码(可选)
                    * withdrawFlag : 撤单标志(可选, N-报单, Y-撤单)
                    * isCancellable : 是否可撤单标志(可选)
                    * beginTime : 起始时间(可选, hh:mm:ss)
                    * endTime : 结束时间(可选, hh:mm:ss)
    '''
    acctId = ''
    exchId = ''
    batchNum = ''
    contractNum = ''
    stkId = ''
    withdrawFlag = ''
    isCancellable = ''
    beginTime = ''
    endTime = ''


class ParaQueryOrderInfo(object):
    '''
    queryCond                      报单查询条件

    :fieldmembers:  * queryCond : 查询条件
                    * maxRowNum : 最大查询记录数量(可选，默认为100)
                    * pageNum : 查询页数(可选，默认为1)
                    * queryType : 同步异步数据返回标记
    '''

    queryCond = ''
    maxRowNum = ''
    pageNum = ''
    queryType = ''
    def __init__(self, queryCond, maxRowNum, pageNum, queryType):
        self.queryCond = queryCond
        self.maxRowNum = maxRowNum
        self.pageNum = pageNum
        self.queryType = queryType


class MsgQueryOrderInfo(object):
    '''
    orderInfo                    报单信息

    :fieldmembers:  * exchId : 市场代码
                    * contractNum : 合同序号
                    * acctId : 资金帐号
                    * regId : 股东代码
                    * regName : 股东姓名
                    * orderType : 委托类型
                    * stkId : 证券代码
                    * stkName : 证券名称
                    * orderPrice : 委托价格
                    * orderQty : 委托数量
                    * knockQty : 成交数量
                    * withdrawQty : 撤单数量
                    * orderTime : 委托时间
                    * offerTime : 申报时间
                    * orderPuttingQty : 申报数量
                    * validFlag : 合法标志
                        * -1 : 待回报
                        * 0 : 合法
                        * 1 : 非法
                        * 2 : 未开户
                    * validFlagDesc : 合法标志描述
                    * sendFlag : 报送标志
                    * sendFlagDesc : 报送标志描述
                    * withdrawFlag : 撤单标志
                    * withdrawFlagDesc : 撤单标志描述
                    * withdrawOrderFlag : 已下撤单委托标志
                    * memo : 备注
                    * batchNum : 委托批号
                    * stkType : 证券类别
                    * tradeType : 交易类型
                    * orderAmt : 委托金额
                    * statusId : 委托状态
                    * exchErrorCode : 交易所的委托确认码
                    * orderStatus : 交易状态
                    * isCancellable : 可撤单标志
                    * occurTime : 发生时间
                    * operationMAC : 委托主机MAC地址
                    * basketId : 篮子代码
                    * f_orderStatus : 报单状态
                    * orderId : 交易的订单编号
                    * serialNum : 流水号，作为交易所的requestId使用
                    * actionFlag : 报单的操作类型(NEW-报单, DELETE-撤单)
                    * f_hedgeFlag : 投保标记
                    * f_offSetFlag : 开平标志
                    * bsFlag : 合约方向(B-多头，S-空头)
                    * f_orderPriceType : 报单价格条件
                    * futureOrderPrice : 委托价格(精确到小数点后4位)
                    * f_MatchCondition : 有效期类型
                    * GTDDate : GTS日期
                    * filledQtyCondition : 成交量类型
                    * minimalVolume : 最小成交量
                    * queuedCondition : 触发条件
                    * stopPrice : 止损价格
                    * autoSuspend : 自动挂起标志
                    * f_forceCloseReason : 强平原因
                    * exchErrorMsg : 错误信息
                    * openUsedMarginAmt : 今开占用保证金
                    * closePNL : 平仓损益
                    * offsetMarginAmt : 平仓释放保证金
                    * openFrozMargin : 开仓冻结保证金
                    * coveredFlag : 备兑标签(0-非备兑,1-备兑)
    '''

class MsgQueryPositionInfo(object):
    '''
    positionInfo                 持仓信息

    :fieldmembers:  * exchId : 交易市场
                    * exchAbbr : 市场简称
                    * stkId : 证券代码
                    * stkName : 证券名称
                    * orderUnit : 交易单位
                    * orderUnitDesc : 委托单位描述
                    * exceptFrozenQty : 异常冻结数量
                    * sellFrozenQty : 卖出冻结数量
                    * buyFrozenQty : 买入冻结数量
                    * newPrice : 最新价
                    * regId : 股东代码
                    * previousQty : 昨日余额
                    * previousCost : 昨日买入成本金额
                    * previousIncome : 昨日收益
                    * acctId : 资金帐号
                    * currentStkValue : 当前证券市值
                    * currentQtyForAsset : 计算资产用的股份余额
                    * realtimeCost : 实时成本
                    * realtimeIncome : 实时收入
                    * usableQty : 可用数量(单位为委托单位)
                    * unsaleableQty : 非流通余额非流通股份（股票）
                    * rightsQty : 权益数量
                    * frozenQty : 冻结权益数量
                    * stkValue : 证券市值
                    * currentQty : 实时股份余额（考虑实时买卖）
                    * expectedbuyamt : 回报买入金额
                    * expectedsellamt : 回报卖出金额
                    * maxSellStkQty : 回报卖出数量
                    * qtyPerHand : 委托单位
                    * bsFlag : 合约方向(B-多头，S-空头)
                    * f_hedgeFlag : 投保标记
                    * currentPositionQty : 当前持仓数量
                    * realTimePositionQty : 实时持仓数（实时计算）
                    * ydPositionUsableQty : 昨日持仓可平仓数
                    * todayPositionUsableQty : 今日持仓可平仓数
                    * todayPositionCost : 今开持仓均价
                    * preSettlementPrice : 昨日结算价
                    * closePNL : 平仓盈亏
                    * realtimePNL : 实时盈亏（实时计算）
                    * openFrozPositionQty : 开仓冻结数量
                    * todayOffsFrozPositionQty : 平今冻结
                    * ydOffsFrozPositionQty : 平昨冻结数
                    * marginFrozenAmt : 保证金冻结金额
                    * marginUsedAmt : 当日保证金占用（实时计算）
                    * todayContractAmt : 今日合约金额
                    * ydContractAmt : 昨日持仓合约金额
                    * coveredFlag : 备兑标签(可选)(0-备兑,1-非备兑)
                    * securityType : 证券类型（CS-现货，FUT-期货）
    '''


class QueryFutureCond(object):
    """
    queryCond                   期货合约查询条件

    :fieldmembers:  * exchId : 市场(可选)
                    * f_productId : 品种(可选)
                    * basicExchId : 标的市场(可选)
                    * basicStkId : 标的代码(可选)
    """

    exchId = ''
    f_productId = ''
    basicExchId = ''
    basicStkId = ''


class ParaQueryFutureInfo(object):
    """
    期货合约查询参数

    :fieldmembers:  * queryCond : 查询条件
                        * exchId : 市场(可选)
                        * f_productId : 品种(可选)
                        * basicExchId : 标的市场(可选)
                        * basicStkId : 标的代码(可选)
                    * maxRowNum : 最大查询记录数量(可选，默认为100)
                    * pageNum : 查询页数(可选，默认为1)

    """

    queryCond = ''
    maxRowNum = ''
    pageNum = ''

    def __init__(self, queryCond, maxRowNum, pageNum):
        self.queryCond = queryCond
        self.maxRowNum = maxRowNum
        self.pageNum = pageNum



class QueryKnockCond(object):
    '''
    queryCond                    查询条件

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * contractNum : 合同号(可选)
                    * stkId : 证券代码(可选)
                    * beginTime : 起始时间(可选, hh:mm:ss)
                    * endTime : 结束时间(可选, hh:mm:ss)
    '''
    acctId = ''
    contractNum = ''
    stkId = ''
    beginTime = ''
    endTime = ''

class QueryPositionCond(object):
    '''
    queryCond                    查询条件

    :fieldmembers:  * acctId : 资金帐号(必送)
                    * exchId : 市场代码(可选)
                    * stkId : 证券代码(可选)
                    * regId : 股东代码(可选)
                    * bsFlag : 合约方向(期货，期权可选)(B-多头，S-空头)
                    * f_hedgeFlag : 投保标记(期货，期权可选)(HEDGE-套保，SPEC-投机)
                    * coveredFlag : 备兑标签(期货，期权可选)(0-备兑,1-非备兑)
    '''
    acctId = ''
    exchId = ''
    stkId = ''
    regId = ''
    bsFlag = ''
    f_hedgeFlag = ''
    coveredFlag = ''

class ParaQueryKnockInfo(object):
    '''
    成交查询参数

    :fieldmembers:  * maxRowNum : 最大查询记录数量(可选，默认为100)
                    * pageNum : 查询页数(可选，默认为1)
    '''

    queryCond = ''
    maxRowNum = ''
    pageNum = ''
    queryType = ''

    def __init__(self, queryCond, maxRowNum, pageNum, queryType):
        self.queryCond = queryCond
        self.maxRowNum = maxRowNum
        self.pageNum = pageNum
        self.queryType = queryType

class ParaQueryPositionInfo(object):
    '''
    持仓查询参数

    :fieldmembers:  * maxRowNum : 最大查询记录数量(可选，默认为100)
                    * pageNum : 查询页数(可选，默认为1)
    '''

    queryCond = ''
    maxRowNum = ''
    pageNum = ''
    queryType = ''

    def __init__(self, queryCond, maxRowNum, pageNum, queryType):
        self.queryCond = queryCond
        self.maxRowNum = maxRowNum
        self.pageNum = pageNum
        self.queryType = queryType

class MsgQueryKnockInfo(object):
    '''
    knockInfo                    成交信息

    :fieldmembers:  * acctId : 资金帐号
                    * exchId : 市场
                    * stkName : 证券名称
                    * occurTime : 发生时间
                    * stkId : 证券代码
                    * totalWithdrawQty : 总撤单数量
                    * orderQty : 委托数量
                    * regName : 股东名称
                    * postQty : 本次可用股份
                    * orderPrice : 委托价格
                    * contractNum : 合同号
                    * orderType : 买卖方向
                    * knockQty : 成交数量
                    * knockPrice : 成交价格
                    * knockAmt : 成交金额
                    * fullKnockAmt : 全价成交金额
                    * reckoningAmt : 清算金额
                    * accuredInterestAmt : 应计利息金额
                    * accuredInterest : 应计利息
                    * knockTime : 交易所成交时间
                    * knockCode : 交易所成交编号
                    * serialNum : 根网内部成交编号
                    * exchErrorCode : 交易所错误编码
                    * memo : 交易所错误编码描述
                    * stkType : 证券类别
                    * tradeType : 交易类型
                    * deskId : 席位代码
                    * optId : 操作柜员
                    * optMode : 委托方式
                    * branchId : 营业部
                    * custType : 客户类别
                    * brokerId : 经纪人
                    * custId : 客户代码
                    * tradingResultTypeDesc : 成交类别说明
                    * briefId : 摘要代码
                    * internalBizMark : 业务交易类型
                    * internalOrderType : 内部委托类型
                    * productGrp : 产品集编码
                    * knockNum : 产品集成交序号
                    * operationMAC : 委托主机MAC地址
                    * basketId : 篮子代码
                    * orderId : 交易的订单编号
                    * f_hedgeFlag : 投保标记
                    * f_offSetFlag : 开平标志
                    * bsFlag : 合约方向(B-多头，S-空头)
                    * futureOrderPrice : 报单价格
                    * execType : 执行状态
                    * cumQty : 累计成交数量
                    * leavesQty : 剩余数量
                    * orderSerial : 按时间排队的序号
                    * knockPrice : 成交价格
                    * openUsedMarginAmt : 今开占用保证金
                    * closePNL : 平仓盈亏
                    * offsetMarginAmt : 平仓释放保证金
                    * exchErrorMsg : 错误信息
                    * commision : 手续费
                    * coveredFlag : 备兑标签(0-非备兑,1-备兑)
    '''

class QueryMMSPriceInfo(object):
    '''
    queryInfo          做市商报价模型查询2 查询条件

    :fieldmembers:  * acctId    : 资金账号（必选）
                    * exchId    : 市场代码（可选）
                    * stkId     : 证券代码（可选）
                    * flag      : 0-查询报价模型，1-查询报单数量的详细信息（可选）
                    * optId     : 柜员代码（可选）
                    * projectId : 模型代码（可选）
    '''

    acctId = ''
    exchId = ''
    stkId = ''
    flag = ''
    optId = ''
    projectId = ''

class ParaQueryMMSPriceMode12(object):
    '''
    做市商报价模型查询2
    :fieldmembers: * queryInfo : 查询条件
                        * acctId : 资金账号
                        * exchId : 市场代码（可选）
                        * stkId : 证券代码(可选)
                        * flag  : 0-查询报价模型，1-查询报单数量的详细信息（可选）
                        * optId : 柜员代码（可选）
                        * projectId : 模型代码（可选）
    '''

    queryInfo = ''

    def __init__(self, queryInfo):
        self.queryInfo = queryInfo

class MsgQueryMMSPriceMode12(object):
    '''
    resultList       做市商报价模型查询2 返回结果列表

    :fieldmembers:  * acctId                : 资金帐号
                    * exchId                : 市场代码
                    * stkId                 : 证券代码
                    * offerStatus           : 运行状态
                    * noDoubleOfferInterval : 双边买卖申报持续时间（没有买卖申报且持续x1分钟以上）
                    * noSingleOfferInterval : 单边买卖申报持续时间（只有单边买入申报或卖出申报且持续x2分钟以上）
                    * bsPriceDiffLevel      : 买卖盘口价差级别（卖1价与买1价之差超过）
                    * newPriceDiffRate      : 买卖价差同最新价比例（基金最新成交价格的x4）
                    * bsPriceDiffInterval   : 买卖价差持续时间（持续x5分钟以上）
                    * totalBuyDiffQty       : 买盘口数量和（五档买盘之和少于x6个基金份额）
                    * totalSellDiffQty      : 卖盘口数量和（五档卖盘之和少于x8个基金份额）
                    * singleSideInterval    : 盘口量持续时间（并持续x7分钟以上）
                    * buyPriceStrategy      : 买入价格策略
                    * sellPriceStrategy     : 卖出价格策略
                    * minBuyPriceLevel      : 最小买入价位 y4（如0.001、0.002）
                    * minSellPriceLevel     : 最小卖出价位 y5（如0.001、0.002）
                    * buyPriceRate          : 买入价格的百分比设置
                    * sellPriceRate         : 卖出价格的百分比设置
                    * buyPriceIncrement     : 买入变化量
                    * sellPriceIncrement    : 卖出变化量
                    * buyQtyStrategy        : 买入数量策略
                    * sellQtyStrategy       : 卖出数量策略
                    * maxBuyQty             : 最大可买数量
                    * maxSellQty            : 最大可卖数量
                    * maxBuyOrderLevel      : 报单买入最大档位
                    * maxSellOrderLevel     : 报单卖出最大档位
                    * withdrawInterval      : 撤单时间间隔
                    * marketRiskEvaluation  : 市场风险估计
                    * basicExchId           : 标的证券所在市场
                    * basicStkId            : 标的证券代码
                    * buypriceMode          : 买入净值方式
                    * sellpriceMode         : 卖出净值方式
                    * randomFlag            : 随机拆单启用标记
                    * minOrderQty           : 数量下限
                    * maxOrderQty           : 委托数量上限
                    * totalBuyQtyDiff       : 累计买入数量差
                    * totalSellQtyDiff      : 累计卖出数量差
                    * buyOrderQtyDiff       : 买入对冲量设置
                    * sellOrderQtyDiff      : 卖出对冲量设置
                    * buywithdrawLevel      : 买入撤单盘口档位
                    * sellwithdrawLevel     : 卖出撤单盘口档位
                    * buyPriceIncrement1    : 买入时如果与对手盘成交，则加减档位
                    * sellPriceIncrement1   : 卖出时如果与对手盘成交，则加减档位
                    * buyPriceIncrement2    : 买入变化量（在自动报单的界面调整）
                    * sellPriceIncrement2   : 卖出变化量（在自动报单的界面调整）
                    * projectId             : 模型代码
                    * projectName           : 模型名称
                    * enabledFlag           : 激活标志（0表示不启用，1表示启用)
                    * canRedeemQty          : 可赎回数量
                    * canSubscriptQty       : 可申购数量
                    * buyLevelList          : 买盘区域
                    * sellLevelList         : 卖盘区域
                    * preshareDate          : 上次份额折算日
                    * fundinterestRate      : 基金参考利率
                    * fundType              : 基金类别
                    * basicRate             : 基本利率
                    * optFlag               : 操作标志
                    * paraSigma             : 波动率
                    * paraRF                : 无风险利率
                    * paraG                 : 红利率
                    * paraK                 : 行权价
                    * paraH                 : 敲出价
                    * sellFlag              : 允许卖标志
                    * buyFlag               : 允许买标志
                    * NAVIncrement          : 净值变化量
                    * targetNAV             : 目标基金的单位净值
                    * duration              : 触发周期
                    * priceChange           : 价格变动
                    * priceChangeRate       : 价格变动率
                    * knockqty              : 成交数量
                    * orderType             : 买卖方向
                    * orderSum              : 委托总笔数
                    * orderQty              : 委托数量
                    * qtyStrategy           : 数量策略
                    * offerPercent          : 吃盘比例
                    * orderPriceIncrement   : 价格每次变化增量
    '''

class MakertMakerStatusInfo (object):

    '''
    makertMakerInfo  : 做市参数

    :fieldmembers:  * offerStatus :    运行状态（必选）
                         * '0' : 未执行
                         * '1' : 开始执行
                         * '2' : 暂停
                         * '3' : 完成
                         * '4' : 继续完成
                         * '5' : 等待终止
                         * '6' : 挂起
                    * acctId    : 资金账号（必选）
                    * exchId    : 市场代码（可选）
                    * stkId     : 证券代码（可选）
                    * optId     : 柜员代码（可选）
                    * projectid : 模型代码（可选）
    '''
    offerStatus = ''
    acctId = ''
    exchId = ''
    stkId = ''
    optId = ''
    projectid = ''

class ParaModifyMMSOrderStatus2(object):
    '''
    做市商报价运行状态设置2
    :fieldmembers:  * makertMakerInfo : 做市状态请求参数
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

    makertMakerInfo = ''
    def __init__(self, makertMakerInfo):
        self.makertMakerInfo = makertMakerInfo

class MakertMakerModelInfo(object):
    ''''
    makertMakerInfo 做市参数
    :fieldmembers:  * flag                   : 0-新增，1-修改，3-删除（必选）
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
    flag = ''
    acctId = ''
    exchId = ''
    stkId = ''
    projectId = ''
    buyPriceIncrement1 = ''
    sellPriceIncrement1 = ''
    buyPriceIncrement2 = ''
    sellPriceIncrement2 = ''
    projectName = ''
    enabledFlag = ''
    preshareDate = ''
    fundinterestRate = ''
    fundType = ''
    sellFlag = ''
    buyFlag = ''
    processFlag = ''
    noDoubleOfferInterval = ''
    noSingleOfferInterval = ''
    bsPriceDiffLevel = ''
    newPriceDiffRate = ''
    bsPriceDiffInterval = ''
    totalBuyDiffQty = ''
    totalSellDiffQty = ''
    singleSideInterval = ''

    # 报单价格的策略设置
    buyPriceStrategy = ''
    sellPriceStrategy = ''
    minBuyPriceLevel = ''
    minSellPriceLevel = ''
    buyPriceRate = ''
    sellPriceRate = ''
    buyPriceIncrement = ''
    sellPriceIncrement = ''

    # 报单数量的策略设置
    buyQtyStrategy = ''
    sellQtyStrategy = ''
    maxBuyQty = ''
    maxSellQty = ''
    maxBuyOrderLevel = ''
    maxSellOrderLevel = ''

    # 撤单时间与其它参数设置
    withdrawInterval = ''
    marketRiskEvaluation = ''
    basicExchId = ''
    basicStkId = ''
    buypriceMode = ''
    sellpriceMode = ''

    # 随机拆单需要的参数
    randomFlag = ''
    minOrderQty = ''
    maxOrderQty = ''
    canRedeemQty = ''
    canSubscriptQty = ''
    buyLevelList = ''
    sellLevelList = ''
    totalBuyQtyDiff = ''
    totalSellQtyDiff = ''
    buyOrderQtyDiff = ''
    sellOrderQtyDiff = ''
    buywithdrawLevel = ''
    sellwithdrawLevel = ''
    basicRate = ''
    optFlag = ''
    paraSigma = ''
    paraRF = ''
    paraG = ''
    paraK = ''
    paraH = ''
    NAVIncrement = ''
    targetNAV = ''
    duration = ''
    priceChange = ''
    priceChangeRate = ''
    knockqty = ''
    orderType = ''
    orderSum = ''
    orderQty = ''
    qtyStrategy = ''
    offerPercent = ''
    orderPriceIncrement = ''

class ParaModifyMMSPriceModel2(object):
    '''
    做市商报价模型设置2
    makertMakerInfo 做市参数

    :fieldmembers:  * makertMakerInfo        : 做市模型请求参数
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
    makertMakerInfo = ''

    def __init__(self, makertMakerInfo):
        self.makertMakerInfo = makertMakerInfo


class ParaQueryTransInfo(object):
    """
    逐笔成交信息查询

    :fieldmembers: * exchId : 交易市场
                   * stkId : 证券代码
    """

    exchId = ""
    stkId = ""

    def __init__(self, exchId, stkId):
        self.exchId = exchId
        self.stkId = stkId


class MsgQueryTransInfo(object):
    """
    knockInfo                    逐笔成交信息

    :fieldmembers: * sn : 成交序号
                   * exchId : 市场
                   * stkId : 证券代码
                   * knockTime : 成交时间
                   * knockPrice : 成交价格
                   * knockQty : 成交数量
                   * buyOrderNo : 买方委托序号
                   * sellOrderNo : 卖方委托序号
                   * bsDirect : 买卖性质
                   * ExecType : 成交类别，4=撤销，F=成交

    """


class ParaSubTransQuote(object):
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


class MsgSubTransQuotaReturn(object):
    """
    knockInfo                    逐笔成交信息

    :fieldmembers: * sn : 成交序号
                   * exchId : 市场
                   * stkId : 证券代码
                   * knockTime : 成交时间
                   * knockPrice : 成交价格
                   * knockQty : 成交数量
                   * buyOrderNo : 买方委托序号
                   * sellOrderNo : 卖方委托序号
                   * bsDirect : 买卖性质
                   * ExecType : 成交类别，4=撤销，F=成交

    """