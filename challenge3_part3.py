# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at Mauna Loa, Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
# Annual average for each year in the dataset.
# #
import csv

years = []
year = []
ppm = []
with open('challenge3_part3.csv') as date_csv:
    next(date_csv)
    for row in csv.reader(date_csv):
        date = row[0]
        if date not in years:
            years.append(date)
            year, month, day = date.split("-")
            print(year)
#
for date in year:
    total = 0
    with open("challenge3_part3.csv") as value_csv:
        next(value_csv)
        for row in csv.reader(value_csv):
            year_test = row[0]
            if year == year_test:
                total += float(row[1])
    print(year + ": " + str(total))

# Minimum, maximum and average for the entire dataset.
#
#
# with open('challenge3_part3.csv') as value_csv:
#     next(value_csv)
#     for row in csv.reader(value_csv):
#         value = row[1]
#         if value not in ppm:
#             ppm.append(value)
#
# print(ppm)
# print(min(ppm))
# print(max(ppm))
# print(len(ppm))
# with open('challenge3_part3.csv') as value_csv:
#     next(value_csv)
#     total = 0
#     for row in csv.reader(value_csv):
#         total += float(row[1])
#     print(format(total, 'f'))
#     print(total/len(ppm))
#
# # Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
# spring_list = [3, 4, 5]
# summer_list = [6, 7, 8]
# autumn_list = [9, 10, 11]
# winter_list = [12, 1, 2]
# with open('challenge3_part3.csv') as date_csv:
#     next(date_csv)
#     for row in csv.reader(date_csv):
#         date = row[0]
#         if date not in years:
#             years.append(date)
#             year, month, day = date.split("-")
#             print(month)
#         if month == spring_list:
#             print(month + ((total)/len(ppm)))
#         if month == summer_list:
#             print(month + ((total)/len(ppm)))
#         if month == autumn_list:
#             print(month + ((total)/len(ppm)))
#         if month == winter_list:
#             print(month + ((total)/len(ppm)))
# #
#
# #
# Calculate the anomaly for each value in the dataset relative to the mean for the entire time series.

