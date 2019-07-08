#!/usr/bin/env python
# coding: utf-8

# # Exploring a post popularity depending on it's time of creating
# 
# The data for the project was taken here: [Link](https://www.kaggle.com/hacker-news/hacker-news-posts)
# Before running the code, you should extract the data
# 
# Here we're going to explore posts on Hacker News and try to find out the best time to public a post if we want to get the greatest ammount of comments 

# In[27]:


# Importing modules
from csv import reader
import datetime as dt


# In[6]:


# Getting info from the file

opened_file = open('HN_posts_year_to_Sep_26_2016.csv')
hn = list(reader(opened_file))
header = hn.pop(0)
print(header)
print(hn[:4])


# In[7]:


# Calculating how many 'Ask HN', 'Show HN' and other posts
ask_posts = []
show_posts = []
other_posts = []

for post in hn:
    title = post[1].lower()
    if title.startswith('ask hn'): ask_posts.append(post)
    elif title.startswith('show hn'): show_posts.append(post)
    else: other_posts.append(post)
        
print("Number of 'Ask HN' posts is {}".format(len(ask_posts)))
print("Number of 'Show HN' posts is {}".format(len(show_posts)))
print("Number of other posts is {}".format(len(other_posts)))


# In[9]:


# Finding average number of comments on 'Ask HN' posts
total_ask_comments = 0
for post in ask_posts:
    num_comments = int(post[4])
    total_ask_comments += num_comments

avg_ask_comments = total_ask_comments / len(ask_posts)


# Finding average number of comments on 'Show HN' posts
total_show_comments = 0
for post in show_posts:
    num_comments = int(post[4])
    total_show_comments += num_comments

avg_show_comments = total_show_comments / len(show_posts)


# Finding average number of comments on other posts
total_other_comments = 0
for post in other_posts:
    num_comments = int(post[4])
    total_other_comments += num_comments

avg_other_comments = total_other_comments / len(other_posts)


print("Average number of comments on 'Ask HN' posts: ", avg_ask_comments)
print("Average number of comments on 'Show HN' posts: ", avg_show_comments)
print("Average number of comments on other posts: ", avg_other_comments)


# As 'Ask HN' posts receive on average more comments, we'll focus our attention on them. Let's find number of posts by hour and number of comments by hour

# In[25]:


result_list = []
for post in ask_posts:
    result_list.append([post[6], int(post[4])])     # [Time of creating, number of comments]
    
counts_by_hour = {}
comments_by_hour = {}
for item in result_list:
    time = item[0]
    item[0] = dt.datetime.strptime(time, '%m/%d/%Y %H:%M')
    time = dt.datetime.time(item[0])
    hour = time.hour
    if hour in counts_by_hour:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += item[1]
    else:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = item[1]
        
print('Counts by hour:')
print(counts_by_hour)
print('\nComments by hour:')
print(comments_by_hour)


# Now we're going to find average number of comments per post by hour

# In[26]:


avg_by_hour = []

for key in counts_by_hour:
    avg_by_hour.append([key, comments_by_hour[key] / counts_by_hour[key]])
    
sorted_list = sorted(avg_by_hour, key=lambda x:x[1], reverse = True)
for item in sorted_list:
    print("{}:00 {:.2f} average comments per post".format(item[0], item[1]))


# So, as we can see, the best time to post is 15:00
