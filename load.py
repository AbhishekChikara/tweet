import json
tweets_data_path='tweets.txt'
# Initialize empty list to store tweets: tweets_data
tweets_data=[]

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns= ['text','lang'])

# Print head of DataFrame
print(df.head())

# Initialize list to store tweet counts
['clinton', 'trump', 'machine', 'data'] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    machine += word_in_text('machine', row['text'])
    data += word_in_text('data', row['text'])
	
# Import packages
import matplotlib.pyplot as plt
import seaborn as sns


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd,[clinton, trump, machine, data])
ax.set(ylabel="count")
plt.show()