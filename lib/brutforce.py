import csv
import json
import os
import operator

from itertools import combinations
from model import All_Data

csvFilePath = '../../Stocks_data.csv'
jsonFilePath = '../../json_file_name.json'
list_of_tuples = []
stocks_list = []
data = {}
# data_name = []
# data_cost = []
# data_profit = []

# with open('../Stocks_data.csv', newline='') as csvfile:
with open(csvFilePath, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    index = 1
    for lines in csv_reader:
        g = All_Data(lines[0], lines[1], lines[2])
        data[index] = {"name":lines[0], "cost":lines[1], "profit":lines[2]}
        list_of_tuples.append((lines[0], lines[1], lines[2]))
        index += 1
    # for lines in csv_reader:
    #     g = All_Data(lines[0], lines[1], lines[2])
    #     data_name.append(lines[0])
    #     data_cost.append(lines[1])
    #     data_profit.append(lines[2])
    #     index += 1

# for i in range(len(data_name)):
#     print(data_name[i])
#     print(data_cost[i])
#     print(data_profit[i])

if os.path.exists(jsonFilePath):
    os.remove(jsonFilePath)
with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
print("Job's done")
# print(data)
# print(list_of_tuples)
new_list = sorted(list_of_tuples, key=operator.itemgetter(2), reverse = True)
print(new_list)

amount_in_bank = 500

tries = 1
# while amount_in_bank > 0 and tries != 20:
for tries in range(20):
    print(tries)
    for actions in new_list:
        cost = actions[1]
        # print(cost)
        new_amount_in_bank = amount_in_bank - int(cost)
        if new_amount_in_bank >= 0:
            amount_in_bank -= int(cost)
            stocks_list.append(actions[0])
        else:
            next
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(stocks_list, indent=4))
print(stocks_list)

print(list(combinations('ABCD', 2)))











