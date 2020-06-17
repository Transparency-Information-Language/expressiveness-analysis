#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import requests
from tqdm import tqdm

print('Importing file...')
file = 'Transparenzinformationen.xlsx'

print('---')

print('Get names of all available sheets...')
x1 = pd.ExcelFile(file)
sheets = x1.sheet_names
print(sheets)

print('---')

print('Print all available data controllers (companies)...')
df = pd.read_excel(file, sheet_name=sheets[0])
controllers = [df['Unnamed: %s' % (i)][3] for i in range(7, 37)]
print(controllers)

print('---')

print('Read every single sheet for each and every data controller...')
sheets = [pd.read_excel(file, sheet_name=sheets[i]) for i in tqdm(range(5, 35))]

print('---')

print('Extract the policy URL for each company...')
policies = []
count = 0
for sheet in sheets:
    try:
        p = sheet[controllers[count]][0]
        policies.append(p)
        print(p)
    except:
        print('URL could not be extracted.')
    count += 1

print('---')

print('Download all privacy policies...')

for url in tqdm(policies):
    try:
        response = requests.get(url, timeout=5)
        f = open('download/%s.html' % (url[12:25].replace('/', '-')), 'w')
        f.write(response.content)
        f.close()
    except:
        print(url + ' could not be fetched.')