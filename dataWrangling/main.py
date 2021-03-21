import json
import glob
import os
import pandas as pd
import numpy as np

file1 = open("tweet-json.txt","r")

tweets = []
for line in file1:
    tweets.append(json.loads(line))

print(tweets)
tweets[len(tweets)-1]

df = pd.DataFrame(data=tweets)

df.to_csv("tweet-json.csv",index=0)
