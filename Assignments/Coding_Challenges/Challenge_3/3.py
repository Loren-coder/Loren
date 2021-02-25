# 3. Working with CSV

import csv

year_set, month_set, value_set = [], [], []

with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    line_count = 0
    next(co2)

    for row in csv_reader:
        year, month, day = row[0].split("-")
        if year not in year_set:
            year_set.append(year)
        if month not in month_set:
            month_set.append(month)

        value_set.append(float(row[1]))
        line_count = line_count + 1

print "Minimum = " + str(min(value_set))
print "Maximum = " + str(max(value_set))
print "Average = " + str(float(sum(value_set) / int(line_count)))


# Annual Averages
Annual_Averages = {}

for year in year_set:
    temp_year_set = []
    with open("co2-ppm-daily.csv") as co2:
        csv_reader = csv.reader(co2, delimiter=',')
        next(co2)

        for row in csv_reader:
            year_co2, month_co2, day = row[0].split("-")
            if year_co2 == year:
                temp_year_set.append(float(row[1]))

    Annual_Averages[year] = str(sum(temp_year_set) / len(temp_year_set))

print "Annual_Averages =" + str(Annual_Averages)

# Seasonal Averages

spring_set = []
summer_set = []
fall_set = []
winter_set = []
with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    next(co2)

    for row in csv_reader:
        year_co2, month_co2, day = row[0].split("-")
        if month_co2 == '03' or month_co2 == '04' or month_co2 == '05':
            spring_set.append(float(row[1]))
        if month_co2 == '06' or month_co2 == '07' or month_co2 == '08':
            summer_set.append(float(row[1]))
        if month_co2 == '09' or month_co2 == '10' or month_co2 == '11':
            fall_set.append(float(row[1]))
        if month_co2 == '12' or month_co2 == '01' or month_co2 == '02':
            winter_set.append(float(row[1]))

print "Spring Average= " + str(sum(spring_set) / len(spring_set))
print "Summer Average= " + str(sum(summer_set) / len(summer_set))
print "Autumn Average= " + str(sum(fall_set) / len(fall_set))
print "Winter Average= " + str(sum(winter_set) / len(winter_set))

# Anomaly Calculation

overall_average = sum(value_set) / len(value_set)
anomaly_set = {}

with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    next(co2)

    for row in csv_reader:
        year_co2, month_co2, day = row[0].split("-")
        anomaly_set[year_co2] = float(row[1]) - overall_average
