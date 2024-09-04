""" Using the data from hn_submissions.py, make a bar chart showing the most 
active discussions currently happening on Hacker News. The height of each bar 
should correspond to the number of comments each submission has. The label for 
each bar should include the submission’s title and act as a link to the 
discussion page for that submission. If you get a KeyError when creating a chart, 
use a try-except block to skip over the promotional posts. """


import requests
import plotly.express as express


#
base_url = "https://hacker-news.firebaseio.com/v0/"
request_top_articles = "topstories.json"
respond_top_articles = requests.get(base_url+request_top_articles)
if respond_top_articles.status_code == 200:
    top_articles = respond_top_articles.json()
else:
    print(f"Error: {respond_top_articles.status_code}")
#
comment_nums, submission_titles, link_addresses = [], [], []
#
for article in top_articles[:2]:
    request_article_detail = f"item/{article}.json"
    respond_article_detail = requests.get(base_url+request_article_detail)
    article_detail = respond_article_detail.json()
    submission_titles.append(article_detail['title'])
    comment_nums.append(article_detail['descendants'])
    link_addresses.append(f"https://news.ycombinator.com/item?id={article}")
#
display_x = [f"<a href='{address}'>{title}</a>" for address, title 
             in zip(link_addresses, submission_titles)]
figure = express.bar(x=display_x, y=comment_nums)