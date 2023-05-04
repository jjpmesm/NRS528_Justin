# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at Mauna Loa,
# Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
# Using Python (csv) calculate the following:
# Annual average for each year in the dataset.
import csv

years = []
ppm = []

# Creating a list of the years:
with open('challenge3_part3.csv') as date_csv:
    next(date_csv)
    for row in csv.reader(date_csv):
        date = row[0]
        year, month, day = date.split("-")
        if year not in years:
            years.append(year)
print(years)

# Finding the average ppm per year in the dataset:
for year_test in years:
    total = 0
    counter = 0
    initial_math_value = 0.0
    with open("challenge3_part3.csv") as value_csv:
        next(value_csv)
        for row in csv.reader(value_csv):
            year, month, day = row[0].split("-")
            if year == year_test:
                total += float(row[1])
        for i in csv.reader(value_csv):
            counter = counter + 1
            initial_math_value = initial_math_value + float(i)
    print(year + ": " + str(total))

# Minimum, maximum and average for the entire dataset.
with open('challenge3_part3.csv') as value_csv:
    next(value_csv)
    for row in csv.reader(value_csv):
        value = row[1]
        if value not in ppm:
            ppm.append(float(value))

# print(ppm)
print("The minimum ppm value: " + str(min(ppm)))
print("The maximum ppm value: " + str(max(ppm)))
with open('challenge3_part3.csv') as value_csv:
    next(value_csv)
    total = 0
    for row in csv.reader(value_csv):
        total += float(row[1])
    print("The average ppm for the entire dataset: " + str(total / len(ppm)))
    mean_ppm_all_dataset = total / len(ppm)

# Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October,
# November) and Winter (December, January, February).
spring_list = ['03', '04', '05']
summer_list = ['06', '07', '08']
autumn_list = ['09', '10', '11']
winter_list = ['12', '01', '02']

spring_value_list = []
summer_value_list = []
autumn_value_list = []
winter_value_list = []

with open('challenge3_part3.csv') as date_csv:
    next(date_csv)
    for row in csv.reader(date_csv):
        date = row[0]
        year, month, day = date.split("-")
        if month in spring_list:
            spring_value_list.append(float(row[1]))
        if month in summer_list:
            summer_value_list.append(float(row[1]))
        if month in autumn_list:
            autumn_value_list.append(float(row[1]))
        if month in winter_list:
            winter_value_list.append(float(row[1]))

print("Spring value:")
print(sum(spring_value_list) / len(spring_value_list))
print("Summer value:")
print(sum(summer_value_list) / len(summer_value_list))
print("Autumn value:")
print(sum(autumn_value_list) / len(autumn_value_list))
print("Winter value:")
print(sum(winter_value_list) / len(winter_value_list))

# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.
# current value - mean
# 1. calculate mean for entire dataset DONE
# 2. Subtract mean value from each observation

with open('challenge3_part3.csv') as date_csv:
    next(date_csv)
    for row in csv.reader(date_csv):
        date = row[0]
        ppm_value = row[1]
        print(date + ": " + str(float(ppm_value) - mean_ppm_all_dataset))