import re

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False

# Initialize list to store tweet counts
[word1, word2, word3, word4] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('word1', row['text'])
    trump += word_in_text('word2', row['text'])
    machine += word_in_text('word3', row['text'])
    data += word_in_text('word4', row['text'])
	
# Import packages
import matplotlib.pyplot as plt
import seaborn as sns


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['word1', 'word2', 'word3', 'word4']

# Plot histogram
ax = sns.barplot(cd,[word1, word2, word3, word4])
ax.set(ylabel="count")
plt.show()
