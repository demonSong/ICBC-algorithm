import numpy as np
from scipy import stats
import randomDate as rd
import trade

# simple MMPP P(G->F) P(F->G)

def simpleMMPP(pgf,pfg):
    sums = pgf + pfg
    rateG = 1 / (sums) * pfg
    rateF = 1 / (sums) * pgf
    return rateG,rateF

tradeCount = 20 # 每周平均交易笔数
pgf = 0.2 # 正常交易转异常交易概率
pfg = 0.6 # 异常交易转正常交易概率

rateG,rateF = simpleMMPP(pgf,pfg)

# 正常交易数据仿真
weeks = 12
data = stats.poisson.rvs(mu = tradeCount * rateG,loc = 0,size = weeks)

# 生成12周的数据
startDate = "03-01"

allDates = []

# 第一周 startDate = "01-01" endDate = "01-07"
for i in range(weeks):
    startDate,endDate = rd.createWeekRange(startDate)
    dates = rd.randomDate(2017,startDate,endDate,data[i])
    startDate = rd.createNextDate(endDate)
    allDates.append(dates)

# 交易数据初始化
trades = []
for dates in allDates:
    for date in dates:
        t = trade.Trade(date,False)
        trades.append(t)

#异常交易数据仿真
weeks = 12
data = stats.poisson.rvs(mu = tradeCount * rateF,loc = 0,size = weeks)

# 生成12周的数据
startDate = "03-01"

allDates = []

# 第一周 startDate = "01-01" endDate = "01-07"
for i in range(weeks):
    startDate,endDate = rd.createWeekRange(startDate)
    dates = rd.randomDate(2017,startDate,endDate,data[i])
    startDate = rd.createNextDate(endDate)
    allDates.append(dates)

# 交易数据初始化
for dates in allDates:
    for date in dates:
        t = trade.Trade(date,True)
        trades.append(t)


# 仿真数据可视化
import dateVisual
a,b= dateVisual.plotDate(trades)
