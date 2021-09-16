import csv
import json
import os
import operator

#from itertools import permutations
from math import *
from itertools import combinations, chain
from model import All_Data

csvFilePath = '../Stocks_data.csv'
jsonFilePath = '../json_file_stocks_data.json'
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
    index = 0
    for lines in csv_reader:
        #g = All_Data(lines[0], lines[1], lines[2])
        print(lines)
        print(lines[0])
        print(lines[1])
        print(lines[2])
        totalCalculate = round((float(lines[1])*float(lines[2])),2)
        data[index] = {"name":lines[0], "cost":float(lines[1]), "profit":float(lines[2]), "total_profit":totalCalculate}
        print(data[index])
        list_of_tuples.append(data[index])
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
    jsonFile.write(json.dumps(list_of_tuples, indent=4))
print("Job's done")


# print(data)
# print(list_of_tuples)
#new_list = sorted(list_of_tuples, key=operator.itemgetter(2), reverse = True)
#print(new_list)

#amount_in_bank = 500

#tries = 1
# while amount_in_bank > 0 and tries != 20:

#for actions in new_list:
#    cost = actions[1]
#    # print(cost)
#    new_amount_in_bank = amount_in_bank - int(cost)
#    print(new_amount_in_bank)

#    if new_amount_in_bank >= 0:
#        amount_in_bank -= int(cost)
#        stocks_list.append(actions[0])
#   else:
#        new_amount_in_bank = new_amount_in_bank + int(cost)

#        next
#with open(jsonFilePath, 'w') as jsonFile:
#    jsonFile.write(json.dumps(stocks_list, indent=4))
#print(stocks_list)
#print(new_amount_in_bank)

#print(list(combinations('0123456789', 9)))

#print("je suis dans la fonction combinations")
#pool = tuple(range(10))
#n = len(pool)
#r = 3
#for indices in permutations(range(n), r):
#    print("indices")
#    print(indices)
#    if sorted(indices) == list(indices):
#        tuple(pool[i] for i in indices)
#        print(tuple(pool[i] for i in indices))

def getCombination(index):
    result = list(combinations('abcdefgihlmnopqrstuv', index))
    return result

def valeurMax(valeur):
    #print("if true on autorise la sauvegarde sinon on pass")
    valeurOk = True
    return valeurOk

def treatementData():
    i = 1
    goodOne = []
    for i in range(20):
        print(i)
        combinaisonList = getCombination(i)
        for combinaison in range(len(combinaisonList)):
            if valeurMax(combinaison):
                goodOne.append(combinaison)
        #print(len(list(combinations('abcdefgihlmnopqrstuv', i))))
    print(goodOne)
    pass

def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def calculateProfit():
    pass

combinaisons = powerset([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])

print(combinaisons)

dataset = []

for data in combinaisons:
    #print(data)
    calculateProfit()
    dataset.append(data)

print(len(dataset))

most_value = []

with open(jsonFilePath, 'r') as f:
    distros_dict = json.load(f)
for data in dataset:
    #print("distro")
    #print(distro)
    #print(distro['total_profit'])
    print("dataset[1048570]")
    print(dataset[1048570])
    total_test = 0
    for stock_value in data:
        print(stock_value)
        total_test += distros_dict[stock_value]['cost']
    print(total_test)



#treatementData()
