
import pandas as pd
import plotly as py
import plotly.graph_objs as go
import numpy as np
import csv



def getData():
    dailyGas = pd.read_excel('http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls',sheet_name=1);

    totalRows = dailyGas.__len__()
    dailyGasArray = np.array(dailyGas)

    ftdData = []


    # months can start on monday first monday in the month can only fall on 1,2,3 of the month
    for rowNum in range(2,totalRows):
        ftObject = {}
        if dailyGasArray[rowNum,0].day == 1:
            ftObject['dateValue'] = dailyGasArray[rowNum,0].date()
            ftObject['firstPriceValue'] = dailyGasArray[rowNum,1]
            ftObject['secondPriceValue'] = -1
            ftObject['thirdPriceValue'] = -1
            ftdData.append(ftObject)
        elif dailyGasArray[rowNum,0].day == 2:
            ftObject['dateValue'] = dailyGasArray[rowNum, 0].date()
            ftObject['firstPriceValue'] = -1
            ftObject['secondPriceValue'] = dailyGasArray[rowNum, 1]
            ftObject['thirdPriceValue'] = -1
            ftdData.append(ftObject)
        elif dailyGasArray[rowNum,0].day == 3:
            ftObject['dateValue'] = dailyGasArray[rowNum, 0].date()
            ftObject['firstPriceValue'] = -1
            ftObject['secondPriceValue'] = -1
            ftObject['thirdPriceValue'] = dailyGasArray[rowNum, 1]
            ftdData.append(ftObject)




    retData = []

    print(ftdData)

    for rowNum in range(0, ftdData.__len__()):
        rowObject = {}
        rowObject['dateValue'] = ftdData[rowNum]['dateValue']
        if ftdData[rowNum]['firstPriceValue'] != -1:
            rowObject['priceValue'] = ftdData[rowNum]['firstPriceValue']

        elif ftdData[rowNum]['secondPriceValue'] != -1:
            rowObject['priceValue'] = ftdData[rowNum]['secondPriceValue']

        elif ftdData[rowNum]['thirdPriceValue'] != -1:
            rowObject['priceValue'] = ftdData[rowNum]['thirdPriceValue']

        retData.append(rowObject)

    return retData


def createCsv(data):
    myFile = open('../DataPackage/monthlyPrices.csv', 'w')
    with myFile:
        myFields = ['date', 'value']
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writeheader()
        for x in data:
            writer.writerow({'date': x['dateValue'], 'value': x['priceValue']})

def plot(dates,values):
    py.offline.plot({
        "data": [go.Scatter(x=dates, y=values)],
        "layout": go.Layout(title="monthly gas price value")
    }, auto_open=True)


def main():

    data = getData()
    createCsv(data)
    dates = []
    values = []

    for rowNum in range(0, data.__len__()):
        rowDate = data[rowNum]['dateValue']
        rowValue = data[rowNum]['priceValue']
        dates.append(rowDate)
        values.append(rowValue)

    plot(dates, values)




if __name__ == "__main__":
    main()


