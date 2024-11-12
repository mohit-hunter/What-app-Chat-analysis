import numpy as  np
import pandas as pd
import regex as re

def preprocessor(data):
    pattern = r'(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}\s?[APM]{2}) - (.+)'

    # Lists to store dates and messages
    dates = []
    messages = []

    # Using re.findall() to find all matches in the data
    matches = re.findall(pattern, data)

    # Loop through all matches and separate date and message parts
    for match in matches:
        dates.append(match[0].replace("\u202f", " ").strip())    # Date-time part
        messages.append(match[1].strip())   # Message part

    #creating data frame
    df=pd.DataFrame({"Dates":dates,"Message":messages})
    df['Dates']=pd.to_datetime(df['Dates'],format='%m/%d/%y, %I:%M %p')
    user=[]
    messages=[]
    for message in df['Message']:
        entry=re.split(r'([\w\W]+?):\s',message)
        if entry[1:]:
            user.append(entry[1])
            messages.append(entry[2])
        else:
            user.append('Group Notification')
            messages.append(entry[0])
    df['users']=user
    df['message']=messages
    df.drop(columns=['Message'],inplace=True)
    df['year']=df['Dates'].dt.year
    df['month']=df['Dates'].dt.month_name()
    df['Day']=df['Dates'].dt.day
    df['hours']=df['Dates'].dt.hour
    df['minute']=df['Dates'].dt.minute
    df['month_num']=df['Dates'].dt.month
    df['only_date'] = pd.to_datetime(df['Dates'].dt.date,errors='coerce')
    df['day_name']=df['Dates'].dt.day_name()
    return df