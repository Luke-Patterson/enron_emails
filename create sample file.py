import pandas as pd

df = pd.read_excel('data/full_enron_extract.xlsx')
df = df.sample(10000)
df.to_excel('data/10k_enron_sample.xlsx')