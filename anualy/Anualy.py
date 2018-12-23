import pandas as pd

import numpy as np
import csv
import matplotlib.pyplot as plt





def getData():
    anualGas = pd.read_excel('https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDa.xls',sheet_name=1);


    totalRows = anualGas.__len__()
    anualGasArray = np.array(anualGas)

    retData = []

    print(anualGas)

    for rowNum in range(2,totalRows):
        rowObject = {}
        rowObject['dateValue'] = anualGasArray[rowNum,0].date()
        rowObject['priceValue'] = anualGasArray[rowNum,1]
        retData.append(rowObject)

    return retData


def createCsv(data):
    myFile = open('../DataPackage/annualyPrices.csv', 'w')
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
  #  print(data)
   # plot(data)



if __name__ == "__main__":
    main()