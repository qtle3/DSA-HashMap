# Exercise Hash Table

# Exercise 1:
# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

import csv

arr = []
with open("nyc_weather.csv", mode="r") as file:
    for lines in file:
        tokens = lines.split(",")
        try:
            temp = int(tokens[1])
            arr.append(temp)
        except:
            print("invalid temperature, ignore row")
print(arr)

# What was the average temperature in first week of Jan
avg_temp = sum(arr[0:7]) / 7
print(round(avg_temp, 2))

# What was the maximum temperature in first 10 days of Jan
max_temp = arr[0]

for i in range(len(arr[0:10])):
    if arr[i] > max_temp:
        max_temp = arr[i]
print(max_temp)
