import uuid
import tabula
import pandas as pd
import json
import csv

convertedCsv = uuid.uuid4().hex + "_converted.csv"
tabula.convert_into("NORTHERN JUPITER LOAD SEQ SHEET.pdf", convertedCsv, format="csv", pages="all")

df = pd.read_csv(convertedCsv, on_bad_lines='skip')
df['Unnamed: 0'] = df['Unnamed: 0'].fillna(0)
filt = (df['Unnamed: 0'] == 0) | (df['Unnamed: 0'] == 'Seq')
df2 = df.loc[~filt, 'Unnamed: 0': 'Unnamed: 10']
cleanedCsv = uuid.uuid4().hex + "_cleaned.csv"
df2.to_csv(cleanedCsv, index=False)

df3 = pd.read_csv(cleanedCsv, on_bad_lines='skip')
df3.columns = ['Seq', 'CONTAINER', 'FROM', 'TO', 'CRANE', 'TYPE', 'QUESTION', 'CAT', 'PRT', 'WT', 'SqStow']

df4 = df3.assign(status='', vesselName="", bay="", cell="", position="", loadingPort="")
df4.columns = ['sequence', 'containerRef', 'sfrom', 'sto', 'crane', 'sheetType', 'question', 'cat', 'prt', 'wt',
               'SqStow', 'status', 'vesselName', 'bay', 'cell', 'position', 'loadingPort']

df4['sto'] = df4.sto.astype(str)
df4['bay'] = df4['sto'].str[:2]
df4['cell'] = df4['sto'].str[2:4]
df4['position'] = df4['sto'].str[4:6]
df4.to_csv(cleanedCsv, index=False)


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


csvFilePath = cleanedCsv
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)
