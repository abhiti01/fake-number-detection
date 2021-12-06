import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
# Creating list to append tweet data to
tweets_list2 = []
tweets_list1 = []
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('amazon pay customer care since:2018-01-01 until:2021-11-30').get_items()):
    #Scrapte upto 10,000 tweets then stop
    if i>10000:
        break
    #If the tweet has a 10 digit number extract it
    matchObj = re.search( r"\d{10}", tweet.content, re.I)
    if matchObj:
        tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.followersCount, tweet.user.id])
#save this information in the CSV file
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Follower Count', 'User ID'])
tweets_df2.to_csv('AmazonPay3.csv', sep=',')
