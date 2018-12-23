import pandas as pd
import xlrd
import numpy as np
import csv
import matplotlib.pyplot as plt

import plotly.plotly as py
import plotly.graph_objs as go



def getData():
    weeklyGas = pd.read_excel('https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDw.xls',sheet_name=1);


    totalRows = weeklyGas.__len__()
    weeklyGasArray = np.array(weeklyGas)

    retData = []

    print(weeklyGas)

    for rowNum in range(2,totalRows):
        rowObject = {}
        rowObject['dateValue'] = weeklyGasArray[rowNum,0].date()
        rowObject['priceValue'] = weeklyGasArray[rowNum,1]
        retData.append(rowObject)

    return retData


def createCsv(data):
    myFile = open('../DataPackage/weeklyPrices.csv', 'w')
    with myFile:
        myFields = ['date', 'value']
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writeheader()
        for x in data:
            writer.writerow({'date': x['dateValue'], 'value': x['priceValue']})


def plot(data):
    x = np.linspace(0,5,100)
    y = np.linspace(0,5,100)
    plt.figure()
    plt.plot(x,y)
    plt.show()

def main():
    data = getData()
    createCsv(data)
    print(data)
#    plot(data)



if __name__ == "__main__":
    main()