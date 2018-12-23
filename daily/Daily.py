import urllib.request  as urllib2
import requests
from openpyxl import load_workbook
import json
import datetime
import pandas as pd
import xlrd
import numpy as np
import csv
from bs4 import BeautifulSoup



#dls = "http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls"
#resp = requests.get(dls)

#output = open('daily.xls', 'wb')
#output.write(resp.content)
#output.close()
def getData():
    dailyGas = pd.read_excel('http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls',sheet_name=1);

    totalRows = dailyGas.__len__()
    dailyGasArray = np.array(dailyGas)

    retData = []

    for rowNum in range(2,totalRows):
        rowObject = {}
        print(dailyGasArray[rowNum,0])
        rowObject['dateValue'] = dailyGasArray[rowNum,0].date()
        rowObject['priceValue'] = dailyGasArray[rowNum,1]
        retData.append(rowObject)

    return retData


def createCsv(data):
    myFile = open('../DataPackage/dailyPrices.csv', 'w')
    with myFile:
        myFields = ['date', 'value']
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writeheader()
        for x in data:
            writer.writerow({'date': x['dateValue'], 'value': x['priceValue']})


def main():

    data = getData()
    createCsv(data)




if __name__ == "__main__":
    main()


