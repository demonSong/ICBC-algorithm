class Trade:
    def __init__(self,date,isFraud):
        self.date = date
        self.isFraud = isFraud


    def getFraud(self):
        return self.isFraud

    def getTradeDate(self):
        return self.date

    def printTrade(self):
        print("Transaction date is " + self.date + " and fraud: " + str(self.isFraud))
