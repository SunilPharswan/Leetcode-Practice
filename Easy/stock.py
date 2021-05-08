"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""
import sys
prices = [10,20,230]
minprice=sys.maxsize
maxprofit=0
for i in range(len(prices)):
    for j in range(i,len(prices)):
        maxprofit=max(maxprofit,prices[j]-prices[i])
            