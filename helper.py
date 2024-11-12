from urlextract import URLExtract
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from textblob import TextBlob

extract=URLExtract()
def fetch_stats(selected_user,df):
    if selected_user!="overall":
        df=df[df["users"]==selected_user]
        #1fetching total number of messages
    num_message=df.shape[0]
        #2 fetching total number of words
    words=[]
    for message in df['message']:
        words.extend(message.split())
    #3 fetch number of media message
    num_media=df[df['message']=='<Media omitted>'].shape[0]
    
    #4 fetch number of link shared
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return num_message,len(words),num_media,len(links)
#5 fething active user
def most_active_user(df):
    top_users = df['users'].value_counts().head(5)
    df=round((df['users'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'users':'name','count':'percentage%'})
    return top_users,df
def most_common_words(selected_user, df):
    f=open('stop_hinglish.txt','r')
    stop_words=f.read()
    # Filter the DataFrame based on the selected user
    if selected_user != "overall":
        df = df[df["users"] == selected_user]
    
    tem_df=df[df['users']!='Group Notification']
    tem_df=df[df['message']!='<Media omitted>']
    word=[]
    for message in tem_df['message']:
        for words in message.lower().split():
            if words not in stop_words:
                word.append(words)
    most_common_df=pd.DataFrame(Counter(word).most_common(20))
    return most_common_df
def monthly_timeline_activity(selected_user,df):
    if selected_user!='overall':
        df=df[df["users"]==selected_user]
    timeline=df.groupby(['year','month','month_num']).count()['message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time']=time
    timeline=timeline.sort_values(by=['year','month_num'])
    return timeline
    
# date timeline activity
def date_timeline_activity(selected_user,df):
    if selected_user!='overall':
        df=df[df["users"]==selected_user]
    
    only_dates=df.groupby(['only_date']).count()['message'].reset_index().sort_values(by=['only_date'])
    
    return only_dates
def month_wise_analysis(selected_user,df):
    if selected_user!='overall':
        df=df[df["users"]==selected_user]
    only_months=df['month'].value_counts().reset_index()
    return only_months
def day_wise(selected_user,df):
    if selected_user!='overall':
        df=df[df["users"]==selected_user]
    only_day=day_name=df.groupby(['day_name']).count()['message'].reset_index()
    return only_day

def sentiment_analysis(selected_user,df):
    if selected_user!="overall":
        df=df[df["users"]==selected_user]
    tem_df=df[df['users']!='Group Notification']
    tem_df=df[df['message']!='<Media omitted>']
    sentiments = []
    for message in tem_df['message']:
        blob = TextBlob(message)
        sentiments.append(blob.sentiment.polarity)
    tem_df['sentiment'] = sentiments
    return tem_df