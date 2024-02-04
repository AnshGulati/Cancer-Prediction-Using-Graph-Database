import pandas as pd
import matplotlib.pyplot as mpl
from prettytable import PrettyTable

# Read the CSV file into a pandas dataframe
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
print("To refer the graphs use the table above !")
#The rate of Lung and breast cancer in the states of USA using scatter plot
mpl.scatter(df['State'], df['Total.Rate'])
mpl.xlabel('State')
mpl.ylabel('Total.Rate')
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