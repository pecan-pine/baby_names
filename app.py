import pandas as pd
import matplotlib.pyplot as plt
import os, re

names_dir = './names/'
input_files = [names_dir + f for f in os.listdir(names_dir)]

# regular expression to get the year out of filenames
get_year = re.compile(r'.names/yob(.*)\.txt')

# all names will go into this dataframe
names = pd.DataFrame([], columns=['Name', 'Gender', 'Frequency', 'Year'])

# for each year, put that year's names into a helper dataframe, 
# add the year column to that dataframe, then concatenate with
# the main dataframe
for f in input_files:
    year = int(get_year.findall(f)[0])
    yearly_names = pd.read_csv(f, names=['Name', 'Gender', 'Frequency'])
    yearly_names['Year'] = year
    names = pd.concat([names, yearly_names], ignore_index=True)

# df.loc[(df['Name'] == "Mary") & (df['Gender'] == 'F')].plot(x="Year", y="Frequency")
# plt.show()

print(names)