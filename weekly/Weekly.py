import pandas as pd

import numpy as np
import csv
import plotly as py
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


def plot(dates,values):
    py.offline.plot({
        "data": [go.Scatter(x=dates, y=values)],
        "layout": go.Layout(title="weekly gas price value")
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