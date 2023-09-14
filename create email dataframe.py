import pandas as pd
import os
from utils import parse_email
import pdb
rootdir = "data/maildir/"
df = pd.DataFrame()
file_counter = 0
data_dicts = []
for root, dirs, files in os.walk(rootdir):
    for name in files:
        with open(root + '/' + name, 'r') as f:
            text = f.read()
        data = parse_email(text)
        data_dicts.append(data)
        file_counter += 1
        if file_counter % 1000 == 0:
            print('completed', file_counter, 'files')

    # df2 = df.T.reset_index(drop = True)
    # df2.to_excel('data/sample_extract.xlsx', index = False)
df = pd.DataFrame(data_dicts)
df.to_excel('data/full_enron_extract.xlsx', index = False)

