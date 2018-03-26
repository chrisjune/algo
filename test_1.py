#!/bin/python3

import sys
import os

# Complete the function below.

def verifyItems(origItems, origPrices, items, prices):
    wrongcnt=0
    li = len(items)
    lj = len(origItems)
    for i in range(li):
        idx = origItems.index(items[i])
        if prices[i]!=origPrices[idx]:
            wrongcnt+=1
    return wrongcnt

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    origItems_cnt = 0
    origItems_cnt = int(input())
    origItems_i = 0
    origItems = []
    while origItems_i < origItems_cnt:
        try:
            origItems_item = str(input())
        except:
            origItems_item = None
        origItems.append(origItems_item)
        origItems_i += 1


    origPrices_cnt = 0
    origPrices_cnt = int(input())
    origPrices_i = 0
    origPrices = []
    while origPrices_i < origPrices_cnt:
        origPrices_item = float(input())
        origPrices.append(origPrices_item)
        origPrices_i += 1


    items_cnt = 0
    items_cnt = int(input())
    items_i = 0
    items = []
    while items_i < items_cnt:
        try:
            items_item = str(input())
        except:
            items_item = None
        items.append(items_item)
        items_i += 1


    prices_cnt = 0
    prices_cnt = int(input())
    prices_i = 0
    prices = []
    while prices_i < prices_cnt:
        prices_item = float(input())
        prices.append(prices_item)
        prices_i += 1


    res = verifyItems(origItems, origPrices, items, prices);
    f.write(str(res) + "\n")


    f.close()
