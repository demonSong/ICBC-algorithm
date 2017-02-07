import numpy as np
from scipy import stats
import randomDate as rd

weeks = 12
data = stats.poisson.rvs(mu = 10,loc = 0,size = weeks)

# 生成12周的数据
startDate = "01-01"

allDates = []

# 第一周 startDate = "01-01" endDate = "01-07"
for i in range(weeks):
    startDate,endDate = rd.createWeekRange(startDate)
    dates = rd.randomDate(2017,startDate,endDate,data[i])
    startDate = rd.createNextDate(endDate)
    allDates.append(dates)


