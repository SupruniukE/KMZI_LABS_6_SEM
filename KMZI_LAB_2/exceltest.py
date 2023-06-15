import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType, ChartType
import pandas as pd

# Russian text
with open('textRU.txt') as f:
    symbols = f.read()
letter_frequency = pd.Series(list(filter(str.isalpha, symbols.lower()))).value_counts()
# print(letter_frequency)
f.close()

workbook = Workbook(FileFormatType.XLSX)
i = 1
for key in letter_frequency.keys(): 
    workbook.getWorksheets().get(0).getCells().get("A"+str(i)).putValue(key)
    i+=1
i = 1
for value in letter_frequency: 
    workbook.getWorksheets().get(0).getCells().get("B"+str(i)).putValue(value)
    i+=1

# sheet = workbook.getWorksheets().get(0)
# charts = sheet.getCharts()
# chartIndex = charts.add(ChartType.PYRAMID, 5, 0, 15, 5)
# chart = charts.get(chartIndex)
# serieses = chart.getNSeries()
# serieses.add("A1:B3", True)

sheet = workbook.getWorksheets().get(0)
charts = sheet.getCharts()
chartIndex = charts.add(ChartType.COLUMN, 5, 0, 15, 5)
chart = charts.get(chartIndex)
serieses = chart.getNSeries()
serieses.add(("A1:B"+str(letter_frequency.count())), True)

workbook.save("output1.xlsx")

jpype.shutdownJVM()