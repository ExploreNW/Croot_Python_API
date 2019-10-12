# coding=utf8
'''
Created on 2018年4月25日

@author: Administrator
'''
from multiprocessing.pool import ThreadPool

class OrderNewHandle():
    """
    多线程报单
    """
    def __init__(self, multiProcessCnt):
        self.multiProcessCnt = multiProcessCnt
        self.initReadProcess()
        

    def order(self, orderNew, orderInfo):
        return self.pool.apply(orderNew, (orderInfo,False,))
    
            
    def initReadProcess(self):
        self.pool = ThreadPool(processes = self.multiProcessCnt)

        
    def destroy(self):
        self.pool.close()
        self.pool.join()
