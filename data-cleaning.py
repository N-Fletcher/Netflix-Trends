# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv,pandas as pd
data_raw = pd.read_csv('netflix-data-raw.csv')
print(len(data_raw))

def complete(row):
    for value in row[:15]:
        if value == '':
            return False

    for value in row[17:]:
        if value == '':
            return False
        
    return True

with open('netflix-data-raw.csv', 'r') as inp, open('netflix-data-clean.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        new_row = row[:20]
        if complete(new_row):
            writer.writerow(new_row)

raw = pd.read_csv('netflix-data-raw.csv')
clean = pd.read_csv('netflix-data-clean.csv')
print(len(raw), len(clean))