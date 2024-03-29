import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.86night.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news = soup.find('div', class_='posting_list with_row_background frontpage')
output = ''

output += f"""
<html>
<head>
<style>
h2 {{
    text-align: center;
    color: #3d3d3d;
    font-size: 28px;
    margin-top: 50px;
}}
.news-item {{
    border: 1px solid #d9d9d9;
    padding: 10px;
    margin-bottom: 20px;
    background-color: #f8f8f8;
}}
.title {{
    margin: 10px 0;
    font-size: 18px;
    color: #3d3d3d;
}}
.summary {{
    font-size: 16px;
    color: #3d3d3d;
}}
.link {{
    margin: 10px 0;
    font-size: 16px;
    color: #3d3d3d;
}}
.link a {{
    color: #ff6600;
    text-decoration: none;
}}
.link a:hover {{
    text-decoration: underline;
}}
</style>
</head>
<body>
<h2>86night.com 资讯</h2>
"""

for item in news.find_all('div', class_='posting_list_item'):
    title = item.find('div', class_='title').find('a').text.strip()
    link = f"{url}{item.find('div', class_='title').find('a')['href']}"

    # Fetch the article and extract the summary
    article_response = requests.get(link)
    article_soup = BeautifulSoup(article_response.text, 'html.parser')

    # Extract the first paragraph as a summary
    summary = article_soup.find('div', class_='posting_content').find('p').text.strip()

    output += f"""
    <div class='news-item'>
        <p class='title'>{title}</p>
        <p class='summary'>{summary}</p>
        <p class='link'>Link: <a href='{link}'>{link}</a></p>
    </div>
    """

output += "</body></html>"

with open('news.html', 'w') as f:
    f.write(output)

print("Output has been written to news.html")
