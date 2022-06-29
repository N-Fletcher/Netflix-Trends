# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' Utilize pandas to import original data file '''
import csv,pandas as pd
data_raw = pd.read_csv('netflix-data-raw.csv')

'''
'complete' function scans whether or not a row of data has missing values.
The function returns a boolean; true if the row contains all necessary values,
and false if it doesn't. In this case, I decided to keep rows where the 15th
and 16th values are missing because for those rows, missing values are assumed
to be 0.
'''
def complete(row):
    for value in row[:15]:
        if value == '':
            return False

    for value in row[17:]:
        if value == '':
            return False
        
    return True

''' Open the original data file and a new one for the cleaned data '''
with open('netflix-data-raw.csv', 'r') as inp, open('netflix-data-clean.csv', 'w') as out:
    writer = csv.writer(out)
    titles = []
    
    '''
    Transfer data to the new file row by row. Using the complete function, 
    filter out incomplete rows, also deleting some choice columns at the end.
    Lastly, keep track of titles to get rid of duplicate entries
    '''
    for row in csv.reader(inp):
        new_row = row[:20]
        title = new_row[0]
        if complete(new_row) and title not in titles:
            writer.writerow(new_row)
            titles.append(title)

''' Open both the old and new datasets, comparing the size of each '''
raw = pd.read_csv('netflix-data-raw.csv')
clean = pd.read_csv('netflix-data-clean.csv')
print(len(raw), len(clean))