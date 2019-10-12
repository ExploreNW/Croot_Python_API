# coding=utf-8
from CTSlib import Logger

# 设置日志路径
Logger.setLogPath('./log')

# 设置日志级别
Logger.setLogLevel(Logger.logLevelDebug)

# 打开控制台输出
Logger.setLogOutputFlag(True)


# 服务器信息
serverHost = '192.168.0.94'
serverPort = 9880

# 资金账号,密码
# 000000001637 777777
acctId = '000000007721'
pwd = '666666'

# 柜员，密码
optId = '00076'
optPw = '666666'

# 交易市场
exchId = '0'

# 证券代码
stkId = '600030'
