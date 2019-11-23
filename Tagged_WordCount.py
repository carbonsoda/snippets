import os, csv
from collections import defaultdict
import pandas as pd


folder = "" # desired root folder here

files = []
objects = []

with os.scandir(folder) as root:
    for file in root:
        if file.name.endswith('csv') and file.is_file():
            files.append(file.path)

wordcount = defaultdict(lambda: defaultdict(int))

for file in files:
    with open(file, 'r+') as f:
        csvfile = csv.reader(f, delimiter=',')
        obj = os.path.splitext(os.path.split(file)[1])[0]

        for row in csvfile:
            utter = row[3].lower().split(' ')
            for word in utter:
                if len(word) > 0:
                    wordcount[word][obj] += 1

pd.set_option('precision', 1)
df = pd.DataFrame.from_dict(wordcount, orient='index')
df2 = df.fillna(0)

try:
    df2.to_excel(os.path.join(folder, 'counting.xlsx'))
except PermissionError:
    desktoppath = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'counting.xlsx')
    df2.to_excel(desktoppath)