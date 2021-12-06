import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
col_list =["Text"]
df = pd.concat(
    map(pd.read_csv, ['AmazonPay.csv', 'AmazonPay2.csv', 'GooglePay.csv', 'GooglePay2.csv', 'paytm.csv', 'paytm2.csv', 'PhonePe.csv', 'PhonePe2.csv']), ignore_index=True)
real = 0
nos =[]
tweetsscraped=10000
nosfound=0
for index,row in df['Text'].iteritems():
    nos.append(re.findall(r'\d{10}',str(row)))
for s in nos:
    for j in s:
        nosfound+=1
        real+=1

fakepercentage = (nosfound - real/3000)*100
realpercentage = (tweetsscraped-nosfound+real/3000)*100
print(fakepercentage)
y = np.array([fakepercentage,realpercentage])
mylabels = ["Numbers found", "Non malicious found"]
plt.pie(y, labels = mylabels, autopct= '%.1f%%')
plt.show() 
print(type(texts))