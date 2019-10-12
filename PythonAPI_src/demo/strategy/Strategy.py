#coding=utf-8
import math
import threading
import time, Queue
from CTSlib.ApiUtils import *

twapList = []

# 成交订阅
def strategySubscript(tradeServer,acctId, pwd):
    def onTradeEvent(returnData, msgRespond):
        if(msgRespond.successFlg != 0):
            printString('成交数据：')
            printString('%s,%s' , (msgRespond.errorCode, msgRespond.errorMsg))
        else:
            printObject(returnData, '成交数据：')
            
            for strategyTWAP in twapList:
                strategyTWAP.dealKnockData(returnData)

            
    tradeServer.onTradeEvent = onTradeEvent #订阅数据推送方法
    tradeServer.subscriptTrade(acctId, pwd)

#策略参数
class StrategyPara(object):
    """
    beginTime         策略开始时间
    endTime           策略结束时间
    stgQty            策略数量，
    stgPriceLevel     策略盘口 (b1,s1, b2, s2, ...)
    orderInterval     报单间隔，20ms
    cancelInterval    撤单间隔，5ms
    acctId            账户代码
    exchId            市场代码
    stkId             合约代码
    bsFlag            委托方向
    f_offSetFlag      开平标记
    """
 
    beginTime = ""
    endTime = ""
    stgQty = 0
    stgPriceLevel = "" #策略盘口 (b1,s1, b2, s2, ...)
    orderInterval = 20*1000
    cancelInterval = 5*1000
    acctId  = ""
    exchId  = ""
    stkId   = ""
    bsFlag  = ""
    f_offSetFlag = ""
    
#策略执行信息
class StrategyInfo(object): 
    """
    beginTime         策略开始时间
    endTime           策略结束时间
    stgQty            策略数量，
    stgPriceLevel     策略盘口 (b1,s1, b2, s2, ...)
    totalOrderQty     总委托数量
    knockQty          成交数量
    orderStatus       当前状态
    """
    beginTime = ""      
    endTime = ""          
    stgQty  = 0          
    stgPriceLevel = ""     
    totalOrderQty =0    
    knockQty =0         
    orderStatus=""    
     
#twap策略
class StrategyTWAP(object):
    '''
          实现twap策略逻辑    
    '''
    
    strategyPara = None
    #策略报单列表
    orderInfoList = []
    #策略在途列表
    displayOrderMap = {}
    #策略成交
    knockList = []
    #策略执行信息
    strategyInfo = None
    
    lock=threading.RLock()
    
    def __init__(self,strategyPara,ctsServer):
        
        #首次需要检查各个参数值是否正确
        self.strategyPara = strategyPara
        self.ctsServer = ctsServer
        
        #初始化策略执行信息
        self.strategyInfo = StrategyInfo()
        self.strategyInfo.beginTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))+" "+strategyPara.beginTime
        self.strategyInfo.endTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))+" "+strategyPara.endTime
        self.strategyInfo.stgQty = strategyPara.stgQty
        self.strategyInfo.stgPriceLevel = strategyPara.stgPriceLevel
        self.strategyInfo.totalOrderQty = 0
        self.strategyInfo.knockQty = 0
        self.strategyInfo.orderStatus = 'NEW'
        self.queue = Queue.Queue()
        twapList.append(self)
        
        strategyPara.beginTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))+" "+strategyPara.beginTime
        strategyPara.endTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))+" "+strategyPara.endTime
        
        #启动报单线程
        self.orderThread = OrderThread(ctsServer,strategyPara,self.orderInfoList,self.displayOrderMap,self.strategyInfo,lock)
        Logger.debug('after OrderThread...')
        self.orderThread.start()
        
        #启动撤单线程
        self.cancelThread = CancelThread(ctsServer,strategyPara,self.orderInfoList,self.displayOrderMap,lock)
        Logger.debug('after CancelThread...')
        self.cancelThread.start()
        
        #启动补单线程
        self.appendThread = AppendThread(ctsServer,strategyPara,self.orderInfoList,self.displayOrderMap,lock,self.queue)
        Logger.debug('after CancelThread...')
        self.appendThread.start()
        
    #停止策略执行，中止线程执行
    def stop(self):
        print 'stop thread ...'
        self.orderThread.thread_stop = True
        self.cancelThread.thread_stop = True
        self.appendThread.thread_stop = True
    
    #返回策略报单列表
    def getOrderList(self):
        
        return self.orderInfoList
    
        
    #策略成交列表
    def getKnockList(self):   
        return self.knockList
    
    #返回策略执行信息
    def getStrategyInfo (self):   
        return self.strategyInfo
    
    #回调时成交数据处理
    def dealKnockData(self,returnData): 

        try:
#           #在在图列表中遍历成交订阅回来的合同号
            if self.displayOrderMap.has_key(returnData.contractNum):
                if returnData.returnType ==2:
                    self.knockList.append(returnData)
                    with self.lock:
                        self.strategyInfo.knockQty = self.strategyInfo.knockQty+returnData.knockQty
                        if self.strategyInfo.knockQty > 1 and self.strategyInfo.knockQty < self.strategyInfo.stgQty :
                            self.strategyInfo.orderStatus = 'P_TRD_Q'
                        elif self.strategyInfo.knockQty == self.strategyInfo.stgQty :
                            self.strategyInfo.orderStatus = 'ALLTRD'
                        if returnData.knockQty == returnData.orderQty:
                            del self.displayOrderMap[returnData.contractNum]
                #将撤单信息放入队列并进行补单          
                elif returnData.returnType ==3 or returnData.returnType ==4:
                    with self.lock:
                        del self.displayOrderMap[returnData.contractNum]
                        self.queue.put(returnData)
 
                #对委托确认非法的场景 记录日志不在进行补单      
                elif returnData.returnType ==1:
                    with self.lock:
                        del self.displayOrderMap[returnData.contractNum]
                        self.strategyInfo.totalOrderQty = self.strategyInfo.totalOrderQty - returnData.knockQty
                        Logger.error('Illegal order contractNum %s' % returnData.contractNum)    
                        
                                       
        except Exception as ex:
                Logger.error('dealKnockData error... %s' % ex)        
                    
#报单线程
class OrderThread(threading.Thread):
    #子订单报单数量
    childOrderQty = 0
    
    #剩余数量
    leaveQty = 0
    
    #等待时间
    waitTime = 0
    
    #策略参数
    strategyPara = None
    
    #策略总委托数量
    totalOrderQty = 0

    def __init__(self, ctsServer,strategyPara,orderInfoList,displayOrderMap,strategyInfo,lock):
        threading.Thread.__init__(self)
        self.ctsServer = ctsServer
        self.thread_stop = False
        self.strategyPara = strategyPara
        self.orderInfoList = orderInfoList
        self.strategyInfo = strategyInfo
        self.displayOrderMap = displayOrderMap
        self.lock = lock
        
        beginTime  = time.mktime(time.strptime(strategyPara.beginTime,'%Y-%m-%d %H:%M:%S'))
        endTime  = time.mktime(time.strptime(strategyPara.endTime,'%Y-%m-%d %H:%M:%S'))
        beginTime_real = 0
        totalTime = 0
        #计算报单次数
        if time.time()> beginTime:
           beginTime = time.time()
           self.waitTime = 0
           
        else:
           self.waitTime = beginTime -  time.time()
         
        #计算报单的总时长  
        totalTime = endTime - beginTime
        
        #计算报单总次数 
        totalCnt = math.floor(totalTime/strategyPara.orderInterval)
        
        #计算子订单报单数量
        self.childOrderQty = strategyPara.stgQty/totalCnt

       
    def run(self):

        threadname = threading.currentThread().getName()
        Logger.debug('Thread [%s] is running... ' % threadname)
        strategyPara = self.strategyPara
        #距离策略开始 还需等待waitTime
        if self.waitTime!=0:
            time.sleep(self.waitTime)   
            
        while (not self.thread_stop):
            try:
                beginTime_c = time.time()
                endTime  = time.mktime(time.strptime(strategyPara.endTime,'%Y-%m-%d %H:%M:%S'))
                
                #如果当前时间大于策略结束时间则退出线程
                if time.time() > endTime:
                    self.thread_stop = True     
                    break;
                
                #计算报单数量取整
                orderQty = math.floor(self.childOrderQty+ self.leaveQty) 
                self.leaveQty = self.childOrderQty - orderQty 
                orderQty = int(orderQty)
                
                #最后一笔报单检查
                if self.childOrderQty < strategyPara.stgQty - self.totalOrderQty and strategyPara.stgQty - self.totalOrderQty < 2*self.childOrderQty:
                   orderQty = strategyPara.stgQty - self.totalOrderQty
                   
                   
                # 查询行情
                stkInfo = self.ctsServer.queryStkInfo(strategyPara.exchId, strategyPara.stkId)
                orderPrice  = self.getQuotaPrice(stkInfo,strategyPara)
                
                if orderQty>=1 and self.totalOrderQty < strategyPara.stgQty :
                    
                    # 报单(同步)
                    orderInfo = OrderNewInfo()
                    orderInfo.acctId = strategyPara.acctId
                    orderInfo.currencyId = '00'
                    orderInfo.exchId = strategyPara.exchId
                    orderInfo.stkId = strategyPara.stkId
                    orderInfo.orderQty = orderQty
                    orderInfo.orderPrice = orderPrice
                    orderInfo.f_offSetFlag = strategyPara.f_offSetFlag
                    orderInfo.bsFlag = strategyPara.bsFlag
                    orderInfo.businessMark = 'OTO'
                    orderInfo.f_orderPriceType = 'LIMIT'
                    newOrderResponse = self.ctsServer.orderNew(orderInfo)
                    printObject(newOrderResponse, '期权报单结果：')
                    orderNewContractNum_sync = newOrderResponse.contractNum
                    orderInfo.contractNum = newOrderResponse.contractNum
                    self.totalOrderQty = self.totalOrderQty + orderQty
                    try: 
                        
                        with lock:
                            #更新策略执行数据
                            self.strategyInfo.totalOrderQty = self.strategyInfo.totalOrderQty + orderQty
                            
                            #将报单的合同号和报单时间固定放入map中
                            self.displayOrderMap[orderNewContractNum_sync] = time.time()
                        
                        #将报单数据放入orderInfoList中
                        self.orderInfoList.append(orderInfo)
                    except Exception as ex:
                        Logger.error('orderThread error... %s' % ex)
                endTime_c = time.time()
                stgWaitTime = strategyPara.orderInterval  - (endTime_c-beginTime_c)
                print stgWaitTime
                time.sleep(stgWaitTime)   
            except Exception as ex:
                Logger.error('orderThread error... %s' % ex)
                
    #计算报价           
    def getQuotaPrice(self,stkInfo,strategyPara):
        orderPrice = 0 
        if strategyPara.stgPriceLevel == 'b1':
            orderPrice = stkInfo.buyPrice[0]
        elif strategyPara.stgPriceLevel == 'b2':
            orderPrice = stkInfo.buyPrice[1]
        elif strategyPara.stgPriceLevel == 'b3':
            orderPrice = stkInfo.buyPrice[2]
        elif strategyPara.stgPriceLevel == 'b4':
            orderPrice = stkInfo.buyPrice[3]
        elif strategyPara.stgPriceLevel == 'b5':
            orderPrice = stkInfo.buyPrice[4]
        elif strategyPara.stgPriceLevel == 's1':
            orderPrice = stkInfo.sellPrice[0]
        elif strategyPara.stgPriceLevel == 's2':
            orderPrice = stkInfo.sellPrice[1]
        elif strategyPara.stgPriceLevel == 's3':
           orderPrice = stkInfo.sellPrice[2]
        elif strategyPara.stgPriceLevel == 's4':
            orderPrice = stkInfo.sellPrice[3]
        elif strategyPara.stgPriceLevel == 's5':
            orderPrice = stkInfo.sellPrice[4]
        #如果盘口为null 取最新价报单       
        if orderPrice ==0:
            orderPrice = stkInfo.newPrice  
        return  orderPrice              
           

    def stop(self):
        self.thread_stop = True  
        
#撤单线程
class CancelThread(threading.Thread):   
    
    def __init__(self, ctsServer,strategyPara,orderInfoList,displayOrderMap,lock):
        threading.Thread.__init__(self)
        self.ctsServer = ctsServer
        self.thread_stop = False
        self.strategyPara = strategyPara  
        self.displayOrderMap = displayOrderMap  
        self.orderInfoList = orderInfoList  
        self.lock = lock 
            
    def run(self):

        threadname = threading.currentThread().getName()
        Logger.debug('Thread [%s] is running... ' % threadname)
        
        while (not self.thread_stop):
            try:
                beginTime_c = time.time()
                endTime  = time.mktime(time.strptime(self.strategyPara.endTime,'%Y-%m-%d %H:%M:%S'))
                #如果当前时间大于策略结束时间则退出线程
                if time.time() > endTime:
                    self.thread_stop = True     

                for key,value in self.displayOrderMap.items():

                    try:
                        # 如果当前时间距离报单时间大于5s则撤单
                        if time.time()-value >= self.strategyPara.cancelInterval:
                            # 撤单(同步)
                            orderCancelInfo = OrderCancelInfo()
                            orderCancelInfo.acctId = self.strategyPara.acctId
                            orderCancelInfo.exchId = self.strategyPara.exchId
                            orderCancelInfo.contractNum = key
                            cancellOrderResponse = self.ctsServer.orderCancel(orderCancelInfo)
                            printObject(cancellOrderResponse, '期权撤单结果：')
                            
                    except Exception as ex:
                        Logger.error('CancelThread error... %s' % ex)   
                
                
                endTime_c = time.time()
                stgWaitTime = self.strategyPara.cancelInterval - (endTime_c-beginTime_c)
                if stgWaitTime>0:
                    time.sleep(stgWaitTime)   
            except Exception as ex:
                Logger.error('CancelThread error... %s' % ex)            
            
#补单线程
class AppendThread(threading.Thread):   
    
    def __init__(self, ctsServer,strategyPara,orderInfoList,displayOrderMap,lock,queue):
        threading.Thread.__init__(self)
        self.ctsServer = ctsServer
        self.thread_stop = False
        self.strategyPara = strategyPara  
        self.displayOrderMap = displayOrderMap  
        self.orderInfoList = orderInfoList  
        self.lock = lock 
        self.queue = queue
            
    def run(self):

        threadname = threading.currentThread().getName()
        Logger.debug('Thread [%s] is running... ' % threadname)
        
        while not self.thread_stop:
            try:
                returnData = self.queue.get()
                #撤单成功之后需要进行补单
                # 报单(同步)
                orderInfo = OrderNewInfo()
                orderInfo.acctId = self.strategyPara.acctId
                orderInfo.currencyId = '00'
                orderInfo.exchId = self.strategyPara.exchId
                orderInfo.stkId = self.strategyPara.stkId
                orderInfo.orderQty = returnData.knockQty  #撤单成交数量
                
                # 查询行情
                stkInfo = self.ctsServer.queryStkInfo(self.strategyPara.exchId, self.strategyPara.stkId)
                orderPrice  = self.getQuotaPrice(stkInfo,self.strategyPara)
                orderInfo.orderPrice = orderPrice
                 
                orderInfo.f_offSetFlag = self.strategyPara.f_offSetFlag
                orderInfo.bsFlag = self.strategyPara.bsFlag
                orderInfo.businessMark = 'OTO'
                orderInfo.f_orderPriceType = 'LIMIT'
                newOrderResponse = self.ctsServer.orderNew(orderInfo)
                printObject(newOrderResponse, '期权补单结果：')
                orderNewContractNum_sync = newOrderResponse.contractNum 
                orderInfo.contractNum = newOrderResponse.contractNum
                with self.lock:
                    #将报单的合同号和报单时间固定放入map中
                    self.displayOrderMap[orderNewContractNum_sync] = time.time()
                    #将报单数据放入orderInfoList中
                    self.orderInfoList.append(orderInfo)  
                    
            except Exception as ex:
                Logger.error('AppendThread error... %s' % ex)        
     #计算报价           
    def getQuotaPrice(self,stkInfo,strategyPara):
        orderPrice = 0 
        if strategyPara.stgPriceLevel == 'b1':
            orderPrice = stkInfo.buyPrice[0]
        elif strategyPara.stgPriceLevel == 'b2':
            orderPrice = stkInfo.buyPrice[1]
        elif strategyPara.stgPriceLevel == 'b3':
            orderPrice = stkInfo.buyPrice[2]
        elif strategyPara.stgPriceLevel == 'b4':
            orderPrice = stkInfo.buyPrice[3]
        elif strategyPara.stgPriceLevel == 'b5':
            orderPrice = stkInfo.buyPrice[4]
        elif strategyPara.stgPriceLevel == 's1':
            orderPrice = stkInfo.sellPrice[0]
        elif strategyPara.stgPriceLevel == 's2':
            orderPrice = stkInfo.sellPrice[1]
        elif strategyPara.stgPriceLevel == 's3':
           orderPrice = stkInfo.sellPrice[2]
        elif strategyPara.stgPriceLevel == 's4':
            orderPrice = stkInfo.sellPrice[3]
        elif strategyPara.stgPriceLevel == 's5':
            orderPrice = stkInfo.sellPrice[4]
        #如果盘口为null 取最新价报单       
        if orderPrice ==0:
            orderPrice = stkInfo.newPrice  
        return  orderPrice                             