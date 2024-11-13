import streamlit as st
import regex as re
import pandas as pd
import preprocess
import helper
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
st.header("Welcome to WHAT'S APP CHAT ANALYSIS")
st.sidebar.title("WhatsApp Chat Analyzer")
upload_file = st.sidebar.file_uploader("Choose a file")

if upload_file is not None:
    bytes = upload_file.getvalue()
    data = bytes.decode("utf-8")


    # Call the preprocessor function and store the result in df
    df = preprocess.preprocessor(data)

    
    #fetch unique user
    user_list=df['users'].unique().tolist()
    #user_list.remove('Group Notification')
    user_list.sort()
    user_list.insert(0,'overall')
    selected_user=st.sidebar.selectbox("show analysis wrt",user_list)
    if st.sidebar.button("Show analysis"):
        num_messages,num_words,num_media,num_links=helper.fetch_stats(selected_user,df)
        col1, col2, col3, col4 = st.columns(4)  
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(num_words)
        with col3:
            st.header("Total media shared")
            st.title(num_media)
        with col4:
            st.header("Total links shared")
            st.title(num_links)
        
        #time line activity
        timeline=helper.monthly_timeline_activity(selected_user,df)
        fig,ax=plt.subplots()
        st.title('Time line Activity')
        ax.plot(timeline['time'],timeline['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #date wise activity
        only_dates=helper.date_timeline_activity(selected_user,df)
        only_month=helper.month_wise_analysis(selected_user,df)
        col1,col2=st.columns(2)
        with col1:
            only_dates = helper.date_timeline_activity(selected_user, df)
            fig, ax = plt.subplots()
            st.title("Date-wise Activity")
            ax.plot_date(only_dates['only_date'], only_dates['message'], linestyle='-', marker=None)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        #month wise analysis
        with col2:
            st.title("month-wise-activity")
            st.dataframe(only_month)
        #day_wise
        col1,col2=st.columns(2)
        with col1:
            only_day=helper.day_wise(selected_user,df)
            fig,ax = plt.subplots()
            st.title("Day Wise")
            ax.bar(only_day['day_name'],only_day['message'],color='red')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            df = helper.sentiment_analysis(selected_user,df)
            st.title("Sentiment Analysis")
            st.bar_chart(df.groupby('day_name')['sentiment'].mean())
        #active user
        if selected_user=='overall':
            st.title('most active users')
            x,new_df=helper.most_active_user(df)
            fig,ax=plt.subplots()
            col1,col2=st.columns(2)
            with col1:
                ax.bar(x.index,x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.header('Active %tage')
                st.dataframe(new_df)
        #most common word
        
        most_common_df=helper.most_common_words(selected_user,df)
        
        fig,ax=plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.title("Most common words")
        st.pyplot(fig)
        
