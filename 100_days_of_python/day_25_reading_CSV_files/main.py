# with open("100_days_of_python/day_25_reading_CSV_files/Aiiden income 06:23:24.csv") as Aiiden_Income:
#     data = Aiiden_Income.readlines()
    
# import csv
# with open("100_days_of_python/day_25_reading_CSV_files/Aiiden income 06:23:24.csv") as aiiden_income:
#     data = csv.reader(aiiden_income)
    
#     incomes = []
#     for row in data:
#         incomes.append(row[8])
#     incomes.remove("Amount")
#     float_incomes = list(map(float,incomes))
#     print(sum(float_incomes))

import pandas 
data = pandas.read_csv("100_days_of_python/day_25_reading_CSV_files/Aiiden income 06:23:24.csv")
print(data['Amount'])
first_paycheck = data[data.Amount == -85.51]
print(first_paycheck.date)

#creating a dataframe from scratch 

data_dict = [
    "students":['ian','aiiden','chris'],
    "scores":[10,10,10]
]

data = pandas.DataFrame(data_dict)
data.to_csv("/Users/ianleblanc/Desktop")
        
