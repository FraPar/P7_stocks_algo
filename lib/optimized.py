import csv
import json
import os
import operator

from model import All_Data

csvFilePath = '../Stocks_data.csv'
jsonFilePath = '../json_file_name.json'
list_of_tuples = []
stocks_list = []
data = {}

# We are importing CSV file directly from our root repository
# And creating the Json file to store data
def openFile(csvFilePath, jsonFilePath):
    with open(csvFilePath, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        index = 0
        for lines in csv_reader:
            totalCalculate = round((float(lines[1])*float(lines[2])),2)
            dataTuple[index] = {"name":lines[0], "cost":float(lines[1]), "profit":float(lines[2]), "total_profit":totalCalculate}
            list_of_tuples.append(dataTuple[index])
            index += 1

    if os.path.exists(jsonFilePath):
        os.remove(jsonFilePath)

    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(list_of_tuples, indent=4))

def findStocks(amount_in_bank):
    for actions in new_list:
        cost = actions["cost"]
        new_amount_in_bank = amount_in_bank - int(cost)
        if new_amount_in_bank >= 0:
            amount_in_bank -= int(cost)
            stocks_list.append(actions["name"])
        else:
            next
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(stocks_list, indent=4))
    return stocks_list

# Calculate the profit for all valid stocks combination
def calculateProfit(stocks_list):
    total_profit = 0
    for data in stocks_list:
        print("data")
        print(data)
        print("distros_dict")
        print(distros_dict)
        print("distros_dict[0]")
        print(distros_dict[0])

        total_profit += distros_dict['total_profit']
        if total_profit > most_profit:
            most_profit = total_profit
            combination_profit_most_value = data

def getKeysByValue(dictOfElements, valueToFind, totalCost, totalProfit):
    listOfItems = dictOfElements
    for item in listOfItems:
        if item['name'] == valueToFind:
            totalCost.append(float(item["cost"]))
            totalProfit.append(float(item["total_profit"]))
    return totalCost, totalProfit

dataTuple = {}
most_profit = 0
combination_for_most_value = []
all_profit_data = calculateProfit(stocks_list)
totalCost = []
totalProfit = []

openFile(csvFilePath, jsonFilePath)

with open(jsonFilePath, 'r') as file:
    distros_dict = json.load(file)

new_list = sorted(list_of_tuples, key=operator.itemgetter("profit"), reverse = True)

amount_in_bank = 500

findStocks(amount_in_bank)

for data in stocks_list:
    listOfKeys = getKeysByValue(distros_dict, data, totalCost, totalProfit)

calculate_the_Cost = 0
for cost in totalCost:
    calculate_the_Cost += cost

calculate_the_Profit = 0
for profit in totalProfit:
    calculate_the_Profit += profit

print(calculate_the_Cost)
print(calculate_the_Profit)