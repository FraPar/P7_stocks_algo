import csv
import json
import os
import operator

# csvFilePath = '../dataset2_Python.csv'
# csvFilePath = '../dataset1_Python.csv'
csvFilePath = '../Stocks_data.csv'
jsonFilePath = '../json_file_name.json'
list_of_tuples = []
stocks_list = []




# We are importing CSV file directly from our root repository
# And creating the Json file to store data
def openFile(csvFilePath, jsonFilePath):
    with open(csvFilePath, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        index = 0
        for lines in csv_reader:
            totalCalculate = round((float(lines[1])*float(lines[2])/100),2)
            dataTuple[index] = {"name":lines[0], "cost":float(lines[1]), "profit":float(lines[2]), "total_profit":totalCalculate}
            list_of_tuples.append(dataTuple[index])
            index += 1

    if os.path.exists(jsonFilePath):
        os.remove(jsonFilePath)

    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(list_of_tuples, indent=4))

# Calculating the different possibilities for investing
def findStocks(amount_in_bank):
    for actions in new_list:
        cost = actions["cost"]
        new_amount_in_bank = amount_in_bank - float(cost)
        if new_amount_in_bank >= 0 and cost > 0:
            amount_in_bank -= float(cost)
            stocks_list.append(actions["name"])
            with open(jsonFilePath, 'w') as jsonFile:
                jsonFile.write(json.dumps(stocks_list, indent=4))

# Getting the value from the dictionnary
def getKeysByValue(dictOfElements, valueToFind, totalCost, totalProfit):
    listOfItems = dictOfElements
    for item in listOfItems:
        if item['name'] == valueToFind:
            totalCost.append(float(item["cost"]))
            totalProfit.append(float(item["total_profit"]))
    return totalCost, totalProfit

# Print the stock solution for the user
def printSolution():
    print("The best Stocks to buy are :")
    for data in stocks_list:
        print(data)
    print("For " + str(round(calculate_the_cost, 2)) + " it's worth " + str(round(calculate_the_profit, 2)) + " after 2 years!")

dataTuple = {}
most_profit = 0
combination_for_most_value = []
totalCost = []
totalProfit = []

openFile(csvFilePath, jsonFilePath)

with open(jsonFilePath, 'r') as file:
    distros_dict = json.load(file)

# We sort the list by profit from the dataset
new_list = sorted(list_of_tuples, key=operator.itemgetter("profit"), reverse = True)

amount_in_bank = 500

findStocks(amount_in_bank)

for data in stocks_list:
    listOfKeys = getKeysByValue(distros_dict, data, totalCost, totalProfit)

calculate_the_cost = 0
for cost in totalCost:
    calculate_the_cost += cost

calculate_the_profit = 0
for profit in totalProfit:
    calculate_the_profit += profit

printSolution()