import numpy as np
from scipy import stats

# 模拟1000个服从泊松分布的随机变量？
data = stats.poisson.rvs(mu = 10,loc = 0,size = 12)

# 现在要生成2017年 某个月的交易数据  每个月分为四周，平均每周交易10笔

# 生成一个季度的交易数据 总共有 3 *４　＝　１２周

# 把对应的每周交易数随机落在某个时间段

# 随机生成指定时间段内的日期
import datetime
import random
    

startHours = "00:00:00"
endHours = "23:59:59"

def time2seconds(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def seconds2time(sec):
    m,s = divmod(sec,60)
    h,m = divmod(m,60)
    return "%02d:%02d:%02d" % (h,m,s)

startDate = "2017-01-01"
endDare = "2017-01-07"

def time2date(t):
    m,d = t.strip().split("-")
    return int(m) * 30 + int(d)

def date2time(year,date):
    m,d = divmod(date,30)
    return "%d-%02d-%02d" % (year,m,d)

def randomDate(year,startDate,endDate,num):
    sd = time2date(startDate)
    ed = time2date(endDate)

    shs = time2seconds(startHours)
    ehs = time2seconds(endHours)

    dates = []
    for i in range(num):
        randomDate = random.randint(sd,ed)
        randomSeconds = random.randint(shs,ehs)
        date = date2time(year,randomDate)        
        date += " "+seconds2time(randomSeconds)
        dates.append(date)
    
    return dates
    



