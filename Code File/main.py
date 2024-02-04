import pandas as pd
import matplotlib.pyplot as mpl
from prettytable import PrettyTable


df = pd.read_csv('cancer.csv')

from prettytable import PrettyTable

states_dict = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "District Of Columbia":"DOC",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}

table = PrettyTable()
table.field_names = ["State", "Abbreviation"]

for state, abbr in states_dict.items():
    table.add_row([state, abbr])

print(table)

table2 = PrettyTable()
table2.field_names = ["Year", "Total Population", "Total Lung Cancer Cases","Total Breast Cancer Cases",  "Cancer Rate"]
table2.add_row(["2014", "318386329", "224210", "232670", "143.99"])
table2.add_row(["2015", "320738994", "221200", "231840", "141.5"])
table2.add_row(["2016", "323071755", "224390", "246660", "145.8"])
table2.add_row(["2017", "325122128", "222500", "252710", "146.16"])
table2.add_row(["2018", "326838199", "234030", "266120", "153.02"])
table2.add_row(["2019", "328329953", "228150", "268600", "151.29"])
table2.add_row(["2020", "331501080", "228820", "276480", "156.34"])
table2.add_row(["2021", "331893745", "235760", "281550", "155.86"])
table2.add_row(["2022", "332403650", "236740", "287850", "157.81"])
print(table2)
print("To refer the graphs use the table above !")
#The rate of Lung and breast cancer in the states of USA using scatter plot
mpl.scatter(df['State'], df['Total.Rate'])
mpl.xlabel('State')
mpl.ylabel('Total Rate')
mpl.title('Cancer Rate In various states of USA in a Scatter Graph')
mpl.show()


#The total number of breast cancer and lung cancer in various states of USA represented in a bar graph
mpl.bar(df['State'], df['Total.Number'])
mpl.xlabel('State')
mpl.ylabel('Total.Number')
mpl.title('Total number of breast cancer and lung cancer in various states of USA')
mpl.show()


#The Cancer Rate of people below the age of 18 of breast cancer and lung cancer in various states of USA represented in a bar graph
mpl.bar(df['State'], df['Rates.Age.< 18'])
mpl.xlabel('State')
mpl.ylabel('Cancer Rates at Age< 18')
mpl.title('Cancer Rate of people below the age of 18')
mpl.show()

#The Cancer Rate of people at the ages of 18-45 of breast cancer and lung cancer in various states of USA represented in a bar graph
mpl.bar(df['State'], df['Rates.Age.18-45'])
mpl.xlabel('State')
mpl.ylabel('Cancer Rates at Ages of 18-45')
mpl.title('Cancer Rate of people at the ages of 18-45')
mpl.show()

#The Cancer Rate of people at the ages of 45-64 of breast cancer and lung cancer in various states of USA represented in a bar graph
mpl.bar(df['State'], df['Rates.Age.45-64'])
mpl.xlabel('State')
mpl.ylabel('Cancer Rates at Ages of 45-64')
mpl.title('Cancer Rate of people at the ages of 45-64')
mpl.show()

#The Cancer Rate of people at the ages above 64 of breast cancer and lung cancer in various states of USA represented in a bar graph
mpl.bar(df['State'], df['Rates.Age.> 64'])
mpl.xlabel('State')
mpl.ylabel('Cancer Rates at Ages above 64')
mpl.title('Cancer Rate of people at the ages above 64')
mpl.show()

df2 =pd.read_csv('cancerrate2014-2022.csv')

mpl.plot(df2['Year'], df2['Cancer.Rate'])
mpl.xlabel('Year')
mpl.ylabel('Cancer Rate')
mpl.title('Plot graph showing average increase in Cancer Rate over the years')
mpl.show()
Usa_cancer_rate_yearwise = {
    "2007-2013":"190.65",
    "2014": "143.99",
    "2015": "141.50",
    "2016": "145.80",
    "2017": "146.16",
    "2018": "153.02",
    "2019": "151.29",
    "2020": "156.34",
    "2021": "155.86",
    "2022": "157.81",
}
a = 2.49 #2014-2015
b = 4.3  #2015-2016
c = 0.36 #2016-2017
d = 6.86 #2017-2018
e = 1.73 #2018-2019
f = 5.05 #2019=2020
g = 0.48 #2020-2021
h = 1.92 #2021=2022


average_2014_2022 = (a+b+c+d+e+f+g+h)/8
y = round(average_2014_2022 , 3)

print("The average increase in Cancer Rate in USA is" + ' ' + str(y))
cr_2023_high = 157.81 + y
cr_2023_low = 157.81 - y
print("So in the coming years the change in the rate of cancer is")
print('Peak value: ' + ' ' + str(cr_2023_high))
print('Least value: ' + ' ' + str(cr_2023_low))