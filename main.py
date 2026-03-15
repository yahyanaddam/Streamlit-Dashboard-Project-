import pandas as pd
import streamlit as st

data = pd.read_excel("Analytics 2025.xlsx", sheet_name=None)
youtube = data["You Tube"]#  Views, Subscribers, Impressions, Likes, Unique Viewers. 
instagram = data["Instagram"] # Views, Followers, Interactions, Likes, Unique Viewers.
tiktok = data["TikTok"]# Views, Followers, Impressions, Likes, Unique Viewers.
facebook = data["Facebook"]# Views, Followers, Interactions, Likes, Unique Viewers.

# Options Menu 
platform_choice = st.multiselect("Platform:",["All","Youtube", "Instagram", "TikTok", "Facebook"], default=["All"])
analysis_col = st.multiselect("Metric",["All",
                                        "Views",
                                         "Subscribers/Followers", 
                                         "Impressions/Interactions",
                                         "Likes",
                                         "Unique Viewers"], default=["All"])

# Title & Col1/Col2
st.title("Social Media Growth Dashboard")
col1, col2 = st.columns(2)

# Youtube
if "Youtube" in platform_choice or "All" in platform_choice : 
    col1.header("Youtube")

    if  "Views" in analysis_col or "All" in analysis_col  : 
        col1.subheader("Youtube Views Growth")
        col1.line_chart(youtube.set_index("Ending")["Views"])

    if "Subscribers/Followers" in analysis_col or "All" in analysis_col   : 
        col1.subheader("Youtube Subscribers Growth")
        col1.line_chart(youtube.set_index("Ending")["Subscribers"])

    if "Impressions/Interactions" in analysis_col  or "All" in analysis_col  : 
        col1.subheader("Youtube Impressions Growth")
        col1.line_chart(youtube.set_index("Ending")["Impressions"])

    if  "Likes" in analysis_col  or "All" in analysis_col : 
        col1.subheader("Youtube Likes Growth")
        col1.line_chart(youtube.set_index("Ending")["Likes"])

    if "Unique Viewers" in analysis_col  or "All" in analysis_col : 
        col1.subheader("Youtube Unique Viewers Growth")
        col1.line_chart(youtube.set_index("Ending")["Unique Viewers"])

# Instagram 
if "Instagram" in platform_choice or "All" in platform_choice: 
    col2.header("Instagram")

    if "Views"in analysis_col or "All" in analysis_col  : 
        col2.subheader("Instagram Views Growth")
        col2.line_chart(instagram.set_index("Ending")["Views"])

    if  "Subscribers/Followers" in analysis_col or "All" in analysis_col  : 
        col2.subheader("Instagram Followers Growth")
        col2.line_chart(instagram.set_index("Ending")["Followers"])

    if  "Impressions/Interactions" in analysis_col or "All" in analysis_col  : 
        col2.subheader("Instagram Interactions Growth")
        col2.line_chart(instagram.set_index("Ending")["Interactions"])

    if  "Likes" in analysis_col or "All" in analysis_col : 
        col2.subheader("Instagram Likes Growth")
        col2.line_chart(instagram.set_index("Ending")["Likes"])

    if "Unique Viewers" in analysis_col or "All" in analysis_col : 
        col2.subheader("Instagram Unique Viewers Growth")
        col2.line_chart(instagram.set_index("Ending")["Unique Viewers"])

# Tiktok
if "TikTok" in platform_choice or "All" in platform_choice :
    col1.header("TikTok")
    
    if  "Views" in analysis_col or "All" in analysis_col  :
        col1.subheader("TikTok Views Growth")
        col1.line_chart(tiktok.set_index("Ending")["Views"])

    if  "Impressions/Interactions" in analysis_col or "All" in analysis_col : 
        col1.subheader("TikTok Impressions Growth")
        col1.line_chart(tiktok.set_index("Ending")["Impressions"])

    if  "Subscribers/Followers" in analysis_col or "All" in analysis_col :
        col1.subheader("TikTok Followers Growth")
        col1.line_chart(tiktok.set_index("Ending")["Followers"])

    if  "Likes" in analysis_col or "All" in analysis_col : 
        col1.subheader("TikTok Likes Growth")
        col1.line_chart(tiktok.set_index("Ending")["Likes"])

    if  "Unique Viewers" in analysis_col or "All" in analysis_col : 
        col1.subheader("TikTok Unique Viewers Growth")
        col1.line_chart(tiktok.set_index("Ending")["Unique Viewers"])

# Facebook 
if "Facebook" in platform_choice or "All" in platform_choice : 
    col2.header("Facebook")
    if  "Views" in analysis_col or "All" in analysis_col : 
        col2.subheader("Facebook Views Growth")
        col2.line_chart(facebook.set_index("Ending")["Views"])

    if  "Impressions/Interactions" in analysis_col or "All" in analysis_col : 
        col2.subheader("Facebook Interactions Growth")
        col2.line_chart(facebook.set_index("Ending")["Interactions"])

    if  "Subscribers/Followers" in analysis_col or "All" in analysis_col  :
        col2.subheader("Facebook Followers Growth")
        col2.line_chart(facebook.set_index("Ending")["Followers"])

    if  "Likes"in analysis_col or "All" in analysis_col : 
        col2.subheader("Facebook Likes Growth")
        col2.line_chart(facebook.set_index("Ending")["Likes"])

    if  "Unique Viewers" in analysis_col or "All" in analysis_col : 
        col2.subheader("Facebook Unique Viewers Growth")
        col2.line_chart(facebook.set_index("Ending")["Unique Viewers"])

st.set_page_config(layout="wide")