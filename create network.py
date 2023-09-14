import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import pickle

df = pd.read_excel('data/10k_enron_sample.xlsx')

df = df[['Date','X-From','X-To','X-cc','X-bcc','Subject','text']]
df.columns = [i.replace('X-', '') for i in df.columns]


# Create a directed graph
G = nx.DiGraph()

# Add nodes (email addresses) to the graph
all_email_addresses = set(df['From'].unique())
for recipients in df['To']:
    recipients = recipients.split(', ')
    all_email_addresses.update(recipients)
for recipients in df['cc']:
    recipients = recipients.split(', ')
    all_email_addresses.update(recipients)
for recipients in df['bcc']:
    recipients = recipients.split(', ')
    all_email_addresses.update(recipients)

G.add_nodes_from(all_email_addresses)

# Add edges (email interactions) to the graph
for index, row in df.iterrows():
    sender = row['From']
    recipients = row['To'].split(', ') + row['cc'].split(', ') + row['bcc'].split(', ')
    for recipient in recipients:
        if sender != '':
            G.add_edge(sender, recipient)

with open('data/10k_extract_network.p', 'wb') as file:
    pickle.dump(G, file)

#
# pos = nx.spring_layout(G)
# plt.figure(figsize=(10, 10))
# nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=8)
# plt.title("Email Network")
# plt.show()