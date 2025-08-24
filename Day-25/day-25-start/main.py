# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
from numpy.ma.extras import average

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].max())

# print(data[data.day == 'Monday'])
# print(data[data.temp== data["temp"].max()])

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp *9/5 + 32
# print(monday)
# print(monday_temp)
# print(monday_temp_F)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_colors = data["Primary Fur Color"].unique()
squirrel_dict = {}
for color in squirrel_colors:
    squirrel_color = data[data["Primary Fur Color"] == color]
    squirrel_color_count = len(squirrel_color)
    squirrel_dict[color] = squirrel_color_count

first_key = next(iter(squirrel_dict))
print(first_key)
squirrel_dict_final = squirrel_dict.pop(first_key)
print(squirrel_dict)
print(squirrel_dict_final)
