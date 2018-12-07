import math
def calculatePerformancePercentage(startPrice,endPrice):
    performance = dict()
    performance["profit"] = False
    profit=True
    diff = endPrice - startPrice
    if(diff < 0):
        performance["profit"]=False
    performance["percent"] = abs(diff)/startPrice*100
    return performance

print(calculatePerformancePercentage(125,121))
