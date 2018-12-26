import pandas as pd
import numpy as np
import plotly as py
import plotly.graph_objs as go
import csv


def getData():
    # acquiring data using pandas
    dailyGas = pd.read_excel('http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls',sheet_name=1);

    # turning it into array
    totalRows = dailyGas.__len__()
    dailyGasArray = np.array(dailyGas)

    retData = []

    for rowNum in range(2,totalRows):
        rowObject = {}
      #  print(dailyGasArray[rowNum,0])
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

def plot(dates,values):
    py.offline.plot({
        "data": [go.Scatter(x=dates, y=values)],
        "layout": go.Layout(title="daily gas price value")
    }, auto_open=True)


def main():

    data = getData()
    createCsv(data)

    dates = []
    values = []


    for rowNum in range(0,data.__len__()):
        print(rowNum)
        rowDate = data[rowNum]['dateValue']
        rowValue = data[rowNum]['priceValue']
        dates.append(rowDate)
        values.append(rowValue)


    plot(dates,values)




if __name__ == "__main__":
    main()


