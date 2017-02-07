import datetime
import random
    
# 随机生成小时范围
startHours = "00:00:00"
endHours = "23:59:59"

def time2seconds(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def seconds2time(sec):
    m,s = divmod(sec,60)
    h,m = divmod(m,60)
    return "%02d:%02d:%02d" % (h,m,s)

def time2date(t):
    m,d = t.strip().split("-")
    return int(m) * 30 + int(d)

def date2time(year,date):
    m,d = divmod(date,30)
    if(d == 0):
        d = 1
    return "%d-%02d-%02d" % (year,m,d)

# year 暂时不起作用 startDate 的格式为 "01-07",num 为生成的随机日期的个数
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
    
def createWeekRange(startDate):
    d1 = datetime.datetime.strptime(startDate,"%m-%d")
    d2 = d1 + datetime.timedelta(7)
    endDate = d2.strftime("%m-%d")
    return startDate,endDate

def createNextDate(startDate):
    d1 = datetime.datetime.strptime(startDate,"%m-%d")
    d2 = d1 + datetime.timedelta(1)
    nextDate = d2.strftime("%m-%d")
    return nextDate
    
