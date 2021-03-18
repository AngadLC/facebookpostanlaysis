import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import time
import altair as alt
#reading the data 
'''
# READING DATA FROM FACEBOOK
'''
df = pd.read_json('your_posts_1.json')
# df
#renaming the columns 
df.rename(columns={'timestamp': 'date'},inplace=True)
# df
#droping the unwanted posts
df = df.drop(['attachments', 'title', 'tags'],axis=1)
# df
pd.to_datetime(df['date'])
# df
df = df.set_index('date')
post_counts = df['data'].resample('MS').size()
# post_counts
'Reading data please wait until it completes...'

# Add a placeholder
# latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

st.line_chart(post_counts, width=500, height=0, use_container_width=True)
# c = alt.Chart(post_counts).mark_circle().encode(
#     x='a', y='data', size='c', color='c', tooltip=['a', 'data', 'c'])
# st.altair_chart(c, use_container_width=True)