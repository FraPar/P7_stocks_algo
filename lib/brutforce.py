import csv
import json
import os

from itertools import combinations, chain
# from model import All_Data

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

# Preparation for the combination of all possible stocks
def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

# Get all the possible data stocks
def getCombination(combinaisons):
    for data in combinaisons:
        print(data)
        dataset.append(data)

# Get the maximum value of the data set
def valeurMax(dataset):
    most_value = 0
    for data in dataset:
        total_test = 0
        for stock_value in data:
            total_test += distros_dict[stock_value]['cost']
        if total_test < maximum_cost:
            combination_for_most_value.append(data)
            if most_value < total_test:
                most_value = total_test

# Calculate the profit for all valid stocks combination
def calculateProfit(most_profit, combination_for_most_value):
    for data in combination_for_most_value:
        total_profit = 0
        for profit in data:
            total_profit += distros_dict[profit]['total_profit']
        if total_profit > most_profit:
            most_profit = total_profit
            combination_profit_most_value = data
    return combination_profit_most_value, most_profit

# Print the stock solution for the user
def printSolution():
    print("After " + str(len(combination_for_most_value)) + " combinations under your rules, the best Stocks to buy are :")
    for data in all_profit_data[0]:
        print(distros_dict[data]['name'])
    print("It's worth " + str(round(all_profit_data[1],2)) + " after 2 years!")

# Calculate the profit for the chosen stock combination
def calculateFinalProfit():
    price_stock = 0
    for data in all_profit_data[0]:
        price_stock += distros_dict[data]['cost']
        

csvFilePath = '../Stocks_data.csv'
jsonFilePath = '../json_file_stocks_data.json'
list_of_tuples = []
stocks_list = []
dataTuple = {}
dataset = []
combination_for_most_value = []
maximum_cost = 500
most_profit = 0
combination_profit_most_value = []

openFile(csvFilePath, jsonFilePath)

combinaisons = powerset([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])

getCombination(combinaisons)

with open(jsonFilePath, 'r') as file:
    distros_dict = json.load(file)

valeurMax(dataset)

all_profit_data = calculateProfit(most_profit, combination_for_most_value)

calculateFinalProfit()

printSolution()
